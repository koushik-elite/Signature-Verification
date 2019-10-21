# Signature Verification
Signature Verification App for doodleblue

## Task:

A person’s signature is representative of his identity. For us at the Bank, a signed document by a customer is an instruction from him for carrying out an approved transaction for him.

On on-boarding a customer we capture an image of his signature in our systems, and on receiving a signed document (Cheques, DDs, and others) from him we match the signature on the document with the one recorded in the database before proceeding with the instruction.

In the case of skilled forgeries, it becomes very difficult to verify the identity of the customer.

We want you to build a system that can help us distinguish forgeries from actual signatures. This system should be able to study signature parameters as strokes, curves, dots, dashes, writing fluidity & style, in a Writer-Independent manner and create features for identification of the signature.

The system should not use any existing APIs and should be completely self-developed.

How should it work?

The system shall work in 2 steps:

Step 1: Accept & Store Genuine Signature Image: Take actual signature scanned image of the onboarding customer and store it in a database against a unique Customer ID

Step 2: Accept & Compare Signature Images: Accept inputs of Customer ID and corresponding signature image. Compare with the signature stored in DB against the given Customer ID, and return a Confidence Match Score between the two signature images.

## Architecture

![flow_1](assets/flow.png?raw=true "flow_1")

UI and Backend code with pretrained model is available in

<root>/application
<root>/application/signatureVerify (Angular 6 Code)
<root>/application/server (Python Flask Code)
<root>/application/model (Deep learning models)

Download the pretrained deep learning model from the google drive. since github is limited to 100mb
Download [Model.zip](https://drive.google.com/drive/folders/1lnBTFY5MdfzPlvL3qcg4d7APILLvuOB3?usp=sharing)

Extract the model to 
<root>/application/model (Deep learning models)

API is in python and UI is in angular 6 so both the servers need to be started saperately.

Start Angular Server

got to <root>/application/signatureVerify

install Node and NPM (both stable version)

run on command-prompt/shell
```
npm install
ng serve
```

Start Python Flask Server

got to <root>/application/server

Create a environment and install python flask, follow [installation](/installation) document


run on command-prompt/shell
```
python server.py
```

## Background

### Creating Deep Learning Model

This problem comes under One Shot Classification problem where 2 images will be compared directly and find similarity between them. these kind of clasification are mainly used to compare Human Faces, Signature etc.

### Siamese Networks

Siamese networks are a special type of neural network architecture. Instead of a model learning to classify its inputs, the neural networks learns to differentiate between two inputs. It learns the similarity between them.

### Networks architecture

![architecture_1](assets/network-architecture.jpg?raw=true "architecture_1")

### Contrastive Loss function

Here i defined a custom loss function which is used to calculate the euclidean distance between 2 output from the model

![loss_1](assets/loss.jpg?raw=true "loss_1")

### Equation 1.0 Explanation

Y is either 1 or 0. If the inputs are from the same class , then the value of Y is 0 , otherwise Y is 1

i used Softmax on the difference of 2 outputs and generate probability of Y, Sum of probability is 1

## Training

The training is done in the jupyter notepad [Signature Training.ipynb](/Signature Training.ipynb) using the sample signature images given with the task [sample task.zip](https://drive.google.com/file/d/1cfYpsc16CSqM1qGrMe4Ujx0MIyQc5AAb/view) in email

download and extract the "sample_Signature" folder in the same notebook folder

Folder Path

<Root>/sample_Signature
<Root>/sample_Signature/forged
<Root>/sample_Signature/genuine
<Root>/Signature Training.ipynb
<Root>/prepare.py

run the [prepare.py](/prepare.py) python code for data preparation

A CSV file "train_final.csv" will be created in "sample_Signature" folder 

Run the jupyter notepad [Signature Training.ipynb](/Signature Training.ipynb) for training.

# Reference

[One Shot Learning with Siamese Networks in PyTorch hackernoon](https://hackernoon.com/one-shot-learning-with-siamese-networks-in-pytorch-8ddaab10340e)
[Siamese Neural Networks for One-shot Image Recognition PDF](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
[Siamese Networks for Visual Tracking medium](https://medium.com/intel-student-ambassadors/siamese-networks-for-visual-tracking-96262eaaba77)
[Deploy your PyTorch model to Production medium](https://medium.com/datadriveninvestor/deploy-your-pytorch-model-to-production-f69460192217)



