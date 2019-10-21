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

![screenshot](assets/screenshot.jpg?raw=true "screenshot")

Demo Video [Youtube](https://www.youtube.com/watch?v=LbRdAB0GGMo&list=PL3g74LgzV32_PxmUmbLwtkRzPEmQ_vPS-)

## Architecture

![flow_1](assets/flow.png?raw=true "flow_1")

UI and Backend code with pretrained model is available in

<root>/application

<root>/application/model (Deep learning models)

<root>/application/server (Python Flask Code)

<root>/application/signatureVerify (Angular 6 Code)


## Directory Structure
```bash
.
├── application
│   ├── model
│   │   ├── model.pt
│   │   └── model_v4.pt
│   ├── server
│   │   ├── data
│   │   │   ├── data (copy).csv
│   │   │   ├── data.csv
│   │   │   └── uploads
│   │   │       ├── compare
│   │   │       └── original
│   │   ├── dataset.py
│   │   ├── model.py
│   │   ├── persist.py
│   │   ├── __pycache__
│   │   │   ├── dataset.cpython-36.pyc
│   │   │   ├── model.cpython-36.pyc
│   │   │   └── persist.cpython-36.pyc
│   │   └── server.py
│   └── signatureVerify
│       ├── angular.json
│       ├── browserslist
│       ├── e2e
│       │   ├── protractor.conf.js
│       │   ├── src
│       │   │   ├── app.e2e-spec.ts
│       │   │   └── app.po.ts
│       │   └── tsconfig.json
│       ├── karma.conf.js
│       ├── package.json
│       ├── package-lock.json
│       ├── README.md
│       ├── src
│       │   ├── app
│       │   │   ├── add-signature
│       │   │   │   ├── add-signature.component.css
│       │   │   │   ├── add-signature.component.html
│       │   │   │   ├── add-signature.component.spec.ts
│       │   │   │   ├── add-signature.component.ts
│       │   │   │   └── image-preview.directive.ts
│       │   │   ├── app.component.css
│       │   │   ├── app.component.html
│       │   │   ├── app.component.spec.ts
│       │   │   ├── app.component.ts
│       │   │   ├── app.module.ts
│       │   │   ├── app-routing.module.ts
│       │   │   ├── compare-signature
│       │   │   │   ├── compare-signature.component.css
│       │   │   │   ├── compare-signature.component.html
│       │   │   │   └── compare-signature.component.ts
│       │   │   └── services
│       │   │       └── application.service.ts
│       │   ├── assets
│       │   ├── environments
│       │   │   ├── environment.prod.ts
│       │   │   └── environment.ts
│       │   ├── favicon.ico
│       │   ├── index.html
│       │   ├── main.ts
│       │   ├── polyfills.ts
│       │   ├── styles.css
│       │   └── test.ts
│       ├── tsconfig.app.json
│       ├── tsconfig.json
│       ├── tsconfig.spec.json
│       └── tslint.json
├── assets
│   ├── flow.png
│   ├── loss.jpg
│   └── network-architecture.jpg
├── dataset.py
├── installation
│   └── README.md
├── LICENSE
├── loss.py
├── model
├── model.py
├── prepare.py
├── README.md
├── requirements.txt
├── sample_Signature
│   ├── forged
│   │   └── NFI-08805004.png
│   ├── genuine
│   │   ├── NFI-00101001.png
│   ├── README.txt.txt
│   └── train_final.csv
├── Signature Training.ipynb
├── Signature Training kaggle.ipynb
└── testfiles
    ├── 049
    │   ├── 01_049.png
    │   ├── 02_049.png
    │   ├── 03_049.png
    │   ├── 04_049.png
    │   ├── 05_049.png
    │   ├── 06_049.png
    │   ├── 07_049.png
    │   ├── 08_049.png
    │   ├── 09_049.png
    │   ├── 10_049.png
    │   ├── 11_049.png
    │   └── 12_049.png
    ├── 049_forg
    │   ├── 01_0114049.PNG
    │   ├── 01_0206049.PNG
    │   ├── 01_0210049.PNG
    │   ├── 02_0114049.PNG
    │   ├── 02_0206049.PNG
    │   ├── 02_0210049.PNG
    │   ├── 03_0114049.PNG
    │   ├── 03_0206049.PNG
    │   ├── 03_0210049.PNG
    │   ├── 04_0114049.PNG
    │   ├── 04_0206049.PNG
    │   └── 04_0210049.PNG
    ├── forg
    │   └── NFI-00301001.png
    └── gen
        └── NFI-00101001.png

```

Download the pretrained deep learning model from the google drive. since github is limited to 100mb only

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

Run the jupyter notebook [Signature Training.ipynb](/Signature Training.ipynb) for training.

## Training Kaggle

model_v4 in the <root>/application/model is trained in kaggle with large signature dataset to get more accurate model 

Use the notebook [Signature Training kaggle.ipynb](/Signature Training kaggle.ipynb) upload it to kaggle and use this dataset [signature-verification-dataset](https://www.kaggle.com/robinreni/signature-verification-dataset) for training download the model and use it for production 


# Reference

[One Shot Learning with Siamese Networks in PyTorch hackernoon](https://hackernoon.com/one-shot-learning-with-siamese-networks-in-pytorch-8ddaab10340e)

[Siamese Neural Networks for One-shot Image Recognition PDF](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)

[Siamese Networks for Visual Tracking medium](https://medium.com/intel-student-ambassadors/siamese-networks-for-visual-tracking-96262eaaba77)

[Deploy your PyTorch model to Production medium](https://medium.com/datadriveninvestor/deploy-your-pytorch-model-to-production-f69460192217)





