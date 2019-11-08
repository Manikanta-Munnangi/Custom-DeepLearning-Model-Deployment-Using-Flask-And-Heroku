# coding=utf-8
import tensorflow as tf
import numpy as np
import keras
import os
import time

# SQLite for information
import sqlite3

# Keras
from keras.models import load_model, model_from_json
from keras.preprocessing import image
from PIL import Image

# Flask utils
from flask import Flask, url_for, render_template, request,send_from_directory,redirect
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# load json file before weights
loaded_json = open("models/crop.json", "r")
# read json architecture into variable
loaded_json_read = loaded_json.read()
# close file
loaded_json.close()
# retreive model from json
loaded_model = model_from_json(loaded_json_read)
# load weights
loaded_model.load_weights("models/crop_weights.h5")
model1 = load_model("models/one-class.h5")
global graph
graph = tf.get_default_graph()


def info():
    conn = sqlite3.connect("models/crop.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM crop")
    rows = cursor.fetchall()
    return rows


def leaf_predict(img_path):
    # load image with target size
    img = image.load_img(img_path, target_size=(256, 256))
    # convert to array
    img = image.img_to_array(img)
    # normalize the array
    img /= 255
    # expand dimensions for keras convention
    img = np.expand_dims(img, axis=0)

    with graph.as_default():
        opt = keras.optimizers.Adam(lr=0.001)
        loaded_model.compile(optimizer=opt, loss='mse')
        preds = model1.predict(img)
        dist = np.linalg.norm(img - preds)
        if dist <= 20:
            return "leaf"
        else:
            return "not leaf"


def model_predict(img_path):
    # load image with target size
    img = image.load_img(img_path, target_size=(256, 256))
    # convert to array
    img = image.img_to_array(img)
    # normalize the array
    img /= 255
    # expand dimensions for keras convention
    img = np.expand_dims(img, axis=0)

    with graph.as_default():
        opt = keras.optimizers.Adam(lr=0.001)
        loaded_model.compile(
            optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
        preds = loaded_model.predict_classes(img)
        return int(preds)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        img_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(img_path)
        leaf = leaf_predict(img_path)
        if leaf == "leaf":
            # Make prediction
            preds = model_predict(img_path)
            rows = info()
            res = np.asarray(rows[preds])
            value = (preds == int(res[0]))
            if value:
                ID, Disease, Pathogen, Symptoms, Management = [i for i in res]
            return render_template('result.html', Pathogen=Pathogen, Symptoms=Symptoms, Management=Management, result=Disease, filee=f.filename)
        else:
            return render_template('index.html', Error="ERROR: UPLOADED IMAGE IS NOT A LEAF (OR) MORE LEAVES IN ONE IMAGE")
        # return result
    return None

@app.route('/predict/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)



if __name__ == '__main__':
    app.run()

