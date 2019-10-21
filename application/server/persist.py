import numpy as np
import pandas as pd

def insert_signature(filename):
    global context, genuine_owner_id
    genuine_owner_id = genuine_owner_id + 1
    context.loc[-1] = [filename, genuine_owner_id]  # adding a row
    context.index = context.index + 1  # shifting index
    context = context.sort_index()  # sorting by index
    context.to_csv('data/data.csv', index=False)
    return "{}".format(genuine_owner_id)

def Get_all_customerid():
    global context, genuine_owner_id
    owner_id = list(context["signature_owner_id"].unique())
    
    #return ",".join(str(v) for v in owner_id)
    return {
        "customer_id" : [str(v) for v in owner_id]
    }

def Get_original_image(id):
    global context, genuine_owner_id
    context_block = context.loc[context["signature_owner_id"]==int(id)]
    #print(context_block.head())
    #return ",".join(str(v) for v in owner_id)
    return context_block["Signature_file"].values[0]


context = pd.read_csv("data/data.csv")
genuine_owner_id = np.max(context["signature_owner_id"].unique())