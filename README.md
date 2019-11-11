# Keras-Custom-Model-Deployment-Using-Flask-And-Heroku
Basic Guide to land your Machine Learning or Deep Learning Model to production Using the popular web framework Flask and Heroku is a cloud platform to helps you to deploy without much hassle.


![](https://github.com/Manikanta-Munnangi/Keras-Custom-Model-Deployment-Using-Flask-And-Heroku/tree/master/Demo/Crop.mkv)

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
<h>Most of the folks know about this step and often call this as serializing. After training the model of some problem-solving use cases. Every one usually saves their entire model(architecture + weights + optimizer state) or just weights with python or API library (Pickle, Keras) of their choice to prevent the training model again. </h>
