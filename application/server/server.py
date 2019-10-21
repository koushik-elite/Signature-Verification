import os
from os import listdir
from os.path import isfile, join

import numpy as np
import pandas as pd
from datetime import timedelta  
from flask import Flask, make_response, request, current_app  
from functools import update_wrapper
import persist as pt

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import io
from dataset import SignaturesCompareDataset
from model import SignaturesNetwork
#from flask.ext.cors import CORS
import base64

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

from flask_cors import CORS

default = Flask(__name__)
#cors = CORS(default)
#cors = CORS(default, resources={r"/upload/*": {"origins": "*"}})

use_cuda = torch.cuda.is_available()

device = torch.device("cpu" if torch.cuda.is_available() else "cpu")
if not use_cuda:
    print('No GPU found. Please use a GPU to train your neural network.')


def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

cwd = os.getcwd()
dir = './uploads'

@default.route('/upload/original', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def upload_original():
    if request.method == 'OPTIONS' or request.method == 'POST':
        dir = 'data/uploads/original'
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(dir,filename))
        genuine_owner_id = pt.insert_signature(filename)
        return genuine_owner_id

@default.route('/allcustomerid', methods=['GET'])
@crossdomain(origin='*')
def Get_all_customerid():
    if request.method == 'GET':
        result = pt.Get_all_customerid()
        return result

@default.route('/upload/compare/<id>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def upload_compare(id):
    if request.method == 'OPTIONS' or request.method == 'POST':
        #print("iam in")
        dir = 'data/uploads/compare'
        id = request.form['id']
        #print(id)
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(dir,filename))
        genuine_image = 'data/uploads/original/{}'.format(pt.Get_original_image(id))
        compare_image = os.path.join(dir,filename)
        #print(genuine_image)
        #print(compare_image)
        result = Compare_Image(genuine_image, compare_image)
        #print(result)
        return result

def Compare_Image(image_path, compare_path):
    model = SignaturesNetwork()
    data = SignaturesCompareDataset(image_path, compare_path)

    #print(image_path, compare_path)

    #print(model)

    #print("----------- Loading Model ---------------")

    model = model.to(device)
    model = torch.nn.DataParallel(model)
    model.load_state_dict(torch.load("../model/model_v4.pt"))

    x0, x1, label = data.__getitem__()

    x0_res, x1_res = data.__getimages__()

    x0, x1 = x0.unsqueeze(0), x1.unsqueeze(0)
    #print(label)
    # onehsot applies in the output of 128 dense vectors which is then converted to 2 dense vectors    
    output1, output2 = model(x0.to(device), x1.to(device))

    eucledian_distance_1 = F.pairwise_distance(output2, output1)    
    res = nn.Softmax(dim=1)(output1.to(device) - output2.to(device))
    result=torch.max(res,1)[1].data[0].tolist()

    eucledian_distance = eucledian_distance_1.cpu().flatten().detach().numpy()[0]
    #print(eucledian_distance_1)
    #print(eucledian_distance_1.cpu().flatten().detach().numpy())
    #res.cpu().flatten().detach().numpy()
    # print(res.cpu().flatten().detach().numpy())
    return {
        "result": result,
        "original": ConverPILtoBase(x0_res),
        "eucledian": str(eucledian_distance),
        "copy": ConverPILtoBase(x1_res),
        "difference" : [str(v) for v in res.cpu().flatten().detach().numpy()]
    }

def ConverPILtoBase(image):
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    contents = base64.b64encode(byte_im).decode()
    return contents

if __name__ == '__main__':
    default.run()
