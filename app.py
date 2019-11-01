# coding=utf-8
import sys
import os
import glob
import tensorflow as tf
import re
import numpy as np

# Keras
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template,send_from_directory
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
Model_path="models/crop.h5"
global model,graph
model=load_model(Model_path)
graph=tf.get_default_graph()


def model_predict(img_path):
    # load image with target size
    img=image.load_img(img_path,target_size=(256,256))
    # convert to array
    img=image.img_to_array(img)
    # normalize the array
    img/=255
    # expand dimensions for keras convention 
    img=np.expand_dims(img,axis=0)
    
    Classes = ["Potato Early_blight","Potato Late_blight","Potato healthy","Tomato Bacterial_spot","Tomato Early_blight","Tomato Late_blight","Tomato Leaf_Mold","Tomato Septoria_leaf_spot","Tomato Spider_mites Two-spotted_spider_mite","Tomato Target_Spot","Tomato Tomato_mosaic_virus","Tomato healthy"]
    with graph.as_default():
        preds=model.predict_classes(img)
        return Classes[int(preds)]

@app.route('/', methods=['GET','POST'])
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

        # Make prediction
        result=model_predict(img_path)
        
        # return result 
        return render_template('result.html',result=result)
    return None

if __name__ == '__main__':
     app.run(port=5000, debug=True)

