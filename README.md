Source: https://www.udemy.com/applied-deep-learningtm-the-complete-self-driving-car-course/

Practicing artificial neural network with Python and Keras framework.

## 1/ Introduction (NN)
Artificial neural network are inspired by the brain. The brain is a complex information processing device with incredible pattern recognition abilities. It's able to freely process input from its surrounding environment, categorize them and generate some kind of output. A neural network which is based on a collection of connected nodes processes the information by transmitting it through all over nodes and calculate its values at every nodes.

## 2/ Machine Learning (ML)
### 2.1/Concept
ML is the concept of building computational systems that learn over time based on experience without explicitly programming or hard coded instructions. ML uses a variety of algorithms to describe and analyze data, learn from it to improve then predict accurately, useful outputs.

ML has two most popular techniques: Supervised Learning and Unsupervised Learning. They are a guide to teach algorithm what conclusions it should come up with.
### 2.2/ Supervised vs Unsupervised
Supervised Learning: it typically begins with a dataset that associated with Labelled features which define meaning of our data and find patterns that can be applied to an analytics process.

Unsupervised Learning: Learner gets as tranining as large datasets with no labels and the task is to process that data to find similarities and different in the information.
  
## 3/ Supervised Learning Algorithms
### 3.1/ Linear Regression
Linear regression allows to make predictions based on linearly arranged datasets. Its model is relationship of the dependent variable (response varibale) and the independent variable (explanation variable). The dependent variable is the output we want to predict based on the independent variable.

Example: Predicting price of house based on its size. So the size is independent and the price is dependent on the size.
### 3.2/ Classification
Classification allows to classify data among discrete classes datasets. Its model calculates the likelihood of something that belongs to some class.

Example: Considering two attribates: Blood sugar levels and Age to predict whether of not a person is likely to become diabetic. First thing, we need to represent datasets of diabet and heathy people in a 2-D Cartesian coordinates with the hozirontal axis is Age and the vertical is Blood sugar levels. The next step, we need a model to classify our datasets and the simplest way to do that is drawing a line to separate it. This line is represented by a linear equation.
 
## 4/ Linear Model
Linear equation: y = slope*x + y_intercept. But it will be another form to more understand about Perceptron: 0 = w1*x1 - w2*x2 + bias. x1, x2 are the inputs, bias is y_intercept and w1, w2 are the weights or the parameters define how important the inputs are.

Perceptron implementes Linear model in three steps. First, it starts with a randomly equation. Then, what our algorithm will do is keeping adjusting the weights and bias of linear model unitl it comes up with a optimized line that classifies out data with minimal error. Finally, we use the trained model to predict new unlabelled data.
 
## 5/ Deep Learning
Deep Learning is a ML technique that use a NN for prediction.
### 5.1/ Perceptron
Perceptron is the most basic form of a NN or an algorithm for supervised learning of binary classifiers. It can predict whether or not an output.



