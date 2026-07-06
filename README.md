Author: Shresth Kumar
Date: 2-Jul-26

Project Name: Custom neural network
Objective: to figure out the math behind a basic feed forward neural network.

-----------------------------------------------------------------------------------------------------------------------------

Description:
this model is called BasicNN_v1, it is the first of hopfully many models to come. BasicNN_v1 is a feed forward neural network
which has een built from scratch (only libraries used were pands and numpy) in python, all the math behind the working of this
model is made from scratch by only reading about how the basic working philosophies about its functioning. (no external help 
was used like LLMs or contact with professionals in this field)

00-Concepts holding the digital projection of the ideas behind the whole workflow of this project for reference while coding
to keep track of what to do next along with code snippets which had to be made out of the necessity of the uniquely 
distributed nature of the code and systems in them. This folder also contain diagrams of how the data flows across the project
before becoming the final output (its a rough projection at best but it get the idea across)

01-initialization_criteria has the csv files which specify the scale and shape of the model and which dataset will be
processed (train and/or test).

02-Training_Data recieves the output csv file of Data_sampling_TrainTestSplit.py for the training spilt of the data in 
the folder 01-initialization_criteria.

03-Testing_Data recieves the output csv file of Data_sampling_TrainTestSplit.py for the training spilt of the data in 
the folder 01-initialization_criteria.

processing foleder contains all the folders an files which are involved in the interanl processing of the neural network
which includes the values of weights, biases and current epoch for coordination throughout the program.

BasicNN_v1.py acts as as a library of fucntions which is used to construct the neural network and establish generalized
formulae for processing done by the nodes in each layer.

Data_sampling_TrainTestSplit.py spilts the input data from 01-initialisation_criteria into training and testing data and 
puts them in their respective folders. The train test split to assign training and testing data (K-fold cross validation
will be added in the future).

Gradient_Descent_v1.py is the loss funtion and backpropgation for all models build in this architecture. It calculates rms
(root mean square) error and runs a custion made gradient descent function on it to update weights (bias update will be added later) at the end of each epoch. The 00-Concepts folder contains a word document explaining the working of the math
behind the code.

Test_NN.py is a model testing program which runs a "trained" model to compare its output to the actual answer to evaluate its
accuracy and to show the results to the user.

Train_NN.py is a model training program which uses the assests of BasicNN_v1.py and Gradient_Descent.py to to create the model according to the specifications given in 01-initialization_criteria 
accuracy and to show the results to the user.

initiator_v1.py is an intialization script which calibrates the processing folder as per the 01-initialization_criteria
and initializes the weights by giving them a random value (bias support will be added later, for the time being, all biases are set to 0 as this modell is a proof of concept).

(all other files which have not beena mentioned above are temporarily present to help in development and testing)

-----------------------------------------------------------------------------------------------------------------------------

Conclusion:
The model does work in theory but it has not been put through many the testcases and it needs some optimization, but besides that, it should be a decent first attempt at devloping artificial neural networks.
