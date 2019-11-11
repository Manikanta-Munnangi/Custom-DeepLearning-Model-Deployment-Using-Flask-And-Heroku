# Keras-Custom-Model-Deployment-Using-Flask-And-Heroku
Basic Guide to land your Machine Learning or Deep Learning Model to production Using the popular web framework Flask and Heroku is a cloud platform to helps you to deploy without much hassle.

![Crop]()

# Introduction.
A routine Life cycle of a data science project is to starting with a use case, picking up data from all sources needed for the type of problem we want to solve, analyse data and performing some feature engineering and building a statistical model to make good generalization on future data and deploy into production and monitoring often for perform measures and in case to retrain the model with new data.

But, most of the time people end up at the stage of building a statistical model, they won’t involve in putting their model over the internet for real-world testing because of new technical skills like front-end, back-end developing needs to learn to deploy a model into a web.but i will shou you how to deploy your model with ease.

# Steps to deploy your web app.

1.Save model weights to disk after training.
2.Setup and installing Flask.
3.Download a nice html5 templates for front-end.
4.Write code and upload it to Github.
5.Deploy it on Heroku.
6.Checkout your model website for any bugs.

# 1. Save Model weights.

Most of the folks know about this step and often call this as serializing. After training the model of some problem-solving use cases. Every one usually saves their entire model(architecture + weights + optimizer state) or just weights with python or API library (Pickle, Keras) of their choice to prevent the training model again.

``` python 
# Two ways of doing it.

"""
1.Using pickle a python library.
2.With keras.
"""

""" 1.Serialzing with pickle."""

with open("path/name.pkl","wb") as file:
    pickle.dump(model,file)  
    
""" 2.Saving model with keras. """

# 1.Entire model saving.
from keras.models import load_model
model.save('model_name.h5')  # create a h5 file 

# 2.Saving model weights with architecture.
# it's is recommended to save architecture first as a json (or) yaml file then save weights. Otherwise you get an
# error "read only mode" while loading.

json_arch=model.to_json() # after getting architecture write as json file to disk for loading with weights in future.
for open("model_arch.json","wb") as file:
    file.write(json_arch)
model.save_weights("model_weights.h5")

# Note: It is not recommended to use pickle for saving keras model.

```
# 2.Set up & Installing Flask.

To Install Flask you need to have either pip or conda (if you installed already). Before installing flask you need to create a virtual environment for your flask project because not to conflict with the libraries. we only use whatever library required for our project with their preferred version. so, creating a virtual env will be pretty useful.

``` shell
# make directory and navigate to it.
mkdir project && cd project/
 
# create virtual envrionment for your project.
python3 -m venv myvenv
pip install flask

# activate your virtualenv
source activate name_of_your_env

# deactivate after work
deactivate
```
# 3. Download UI template for your project.

You may want to showcase your project as a professional one in UI. then you need to do a front-end part. luckily we have all bunch of readymade code available over the internet some of them listed below completely free.
Twitter Bootstrap is a toolkit that uses CSS and Javascript / jQuery. It’s a front-end framework with all built-in CSS classes you just need to import one it will do all styling to your website. you can start working on it without much knowledge of CSS. It also creates a responsive website. Of course, you have to know HTML (Basics of website building).


