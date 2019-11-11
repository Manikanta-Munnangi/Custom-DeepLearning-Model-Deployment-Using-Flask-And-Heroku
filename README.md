# Keras-Custom-Model-Deployment-Using-Flask-And-Heroku.

- Basic Guide to land your Machine Learning or Deep Learning Model to production Using the popular web framework Flask and   Heroku is a cloud platform to helps you to deploy without much hassle. 
- You can find step-by-step detailed explanation in my medium blog
[Here](https://medium.com/@manimannu93/everything-from-your-deep-learning-model-to-a-web-app-279cd733f3d4)

**See Demo of my project build with flask and deployed using Heroku.**
<p align="center">
 <img src="https://github.com/Manikanta-Munnangi/Custom-DeepLearning-Model-Deployment-Using-Flask-And-Heroku/blob/master/Demo/crope.gif" width:1280px; height:600px>
</p>

# Introduction.
<p align="justify">
A routine Life cycle of a data science project is to starting with a use case, picking up data from all sources needed for the type of problem we want to solve, analyse data and performing some feature engineering and building a statistical model to make good generalization on future data and deploy into production and monitoring often for perform measures and in case to retrain the model with new data.</p>
<p align="justify">
But, most of the time people end up at the stage of building a statistical model, they won’t involve in putting their model over the internet for real-world testing because of new technical skills like front-end, back-end developing needs to learn to deploy a model into a web.but i will show you how to deploy your model with ease.
</p>

# Should have to know:

* Python3
* Flask with gunicorn.
* Downloading Html5 template. 
* Basics understanding of Html5 and css.
* Heroku basics.


# Steps to deploy your web app.

1. Save model weights to disk after training.
1. Setup and installing Flask.
1. Download a nice html5 templates for front-end.
1. Write code and upload it to Github.
1. Deploy it on Heroku.
1. Checkout your model website for any bugs.

# 1. Save Model weights.
<p align="justify">
Most of the folks know about this step and often call this as serializing. After training the model of some problem-solving use cases. Every one usually saves their entire model(architecture + weights + optimizer state) or just weights with python or API library (Pickle, Keras) of their choice to prevent the training model again.</p>

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
# 2. Set up & Installing Flask.
<p align="justify">
To Install Flask you need to have either pip or conda (if you installed already). Before installing flask you need to create a virtual environment for your flask project because not to conflict with the libraries. we only use whatever library required for our project with their preferred version. so, creating a virtual env will be pretty useful.</p>

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
<p align="justify">
You may want to showcase your project as a professional one in UI. then you need to do a front-end part. luckily we have all bunch of readymade code available over the internet some of them listed below completely free.
Twitter Bootstrap is a toolkit that uses CSS and Javascript/jQuery. It’s a front-end framework with all built-in CSS classes you just need to import one it will do all styling to your website. you can start working on it without much knowledge of CSS. It also creates a responsive website. Of course, you have to know HTML (Basics of website building).</p>

**Html5up.net**

![Html5 themes](https://github.com/Manikanta-Munnangi/Keras-Custom-Model-Deployment-Using-Flask-And-Heroku/blob/master/static/img/html5.png)

# 4. Write code and push to Github.
<p align="justify">
At first, I will explain the use case that I’m deploying to a web app which will help in detecting the disease of plants only I trained for two categories Tomato & Potato analyze and provide remedies biologically and chemically to overcome the loss and further controlling in affected plants. if you feel confused with agricultural things in remedies I gathered a few videos that help you explaining in practice by videos button located near results.</p>

After writing scripts, We need to push it to gihub cause heroku wants the code for converting it to a slug compression for the execution process. you can also use heroku CLI to upload code in heroku GIT but no option to upload from local machine so i prefer github.

**NOTE:You can refer to app.py and in templates folder.**

# 5.Deploy it on Heroku.
<p align="justify">
It makes the job easier with Heroku cause it takes care of everything because it is a platform as a service (PAAS) meaning it does set up infrastructure, pre-installed OS and redundant servers, run time environment. Except for some steps you should do manually.</p>
<p align ="center">
<img src="https://github.com/Manikanta-Munnangi/Keras-Custom-Model-Deployment-Using-Flask-And-Heroku/blob/master/static/img/heroku%20deploy.jpeg">
</p>

## Steps to follow:
1. Create a Heroku account through the official Heroku website.
1. After login, Create App.
1. Name your project it will be deployed as name.herokuapp.com and set up the Deployment method to Github.
1. Here, we are linking our GitHub account with selecting our project repository.
1. Manual deployment verifies the procfile and installs all libraries in requirements.txt file compress to slug compiler responsible for scaling application to a dynos for execution.if whole project after compressing to slug is more than 300MB your application stop process your app. Because they limited the slug size for free access accounts with limited hours.
1. My slug size is below 300MB and the frameworks used python and git LFS, the files that are linked to Large File System (LFS) are not supported in Heroku.
1. Lastly, hit the deploy button in the deploy section and you are done with your project and available for people accessing over the internet.


Finally,If you get any error it good to address the logs and debug your errors and google it you will surely end up with solution.
# Key points to remember
* Use the flask framework if you are a beginner learn your basics.
* Use the template from the bootstrap or html5.net website they are free. Make changes to the template that fits your   project.
* Get working with Heroku it seems to be easy as you working on often.
* Finally, try to make projects that can level up your skills to advance, get cores fundamentals with small projects then move on to big one.
