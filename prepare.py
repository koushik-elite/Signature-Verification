"""
FILE STRUCTURE:
1.genuines : genuine signatures of 30 people, 5 sample each.
2.forged : forged signature of the same 30 people as in genuine folder, 5 sample each.

Naming of files : NFI-XXXYYZZZ
explaination    XXX - ID number of a person who has done the signature. 
		YY - Image smaple number.
		ZZZ - ID number of person whose signature is in photo. 

for example: NFI-00602023 is an image of signature of person number 023 done by person 006. 
             This is a forged signature.
	         NFI-02103021 is an image of signature of person number 021 done by person 021. 
             This is a genuine signature.   

"""

import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from PIL import Image
import progressbar
import gc

import numpy as np
import pandas as pd

def get_ownername(x):
    # NFI-01005010.png
    x = x[9:12]
    return int(x)

def get_signed_owner(x):
    # NFI-01005010.png
    x = x[4:7]
    return int(x)

def get_sample_number(x):
    # NFI-01005010.png
    x = x[7:9]
    return int(x)

def preprocess(dataset, dtype):
    if dtype == "train":
        dataset["owner_id"] = dataset["file"].apply(get_ownername)
        dataset["genuine_sample_number"] = dataset["file"].apply(get_sample_number)
        dataset["signature_owner_id"] = dataset["file"].apply(get_signed_owner)
        dataset["signed_file"] = "genuine/" + dataset["file"]
    else:
        dataset["owner_id"] = dataset["forged_file"].apply(get_ownername)
        dataset["sample_number"] = dataset["forged_file"].apply(get_sample_number)
        dataset["signature_owner_id"] = dataset["forged_file"].apply(get_signed_owner)
        dataset["signed_file"] = "forged/" + dataset["forged_file"]
    return dataset

gc.collect()

genuine_path = Path('sample_Signature/genuine')
forged_path = Path('sample_Signature/forged')

size = 224

genuine_files = [f for f in listdir(genuine_path) if isfile(join(genuine_path, f))]
forged_files = [f for f in listdir(forged_path) if isfile(join(forged_path, f))]


train_csv = pd.DataFrame(genuine_files, columns =['file'])
test_csv = pd.DataFrame(forged_files, columns =['forged_file'])

train_csv = preprocess(train_csv, "train")
test_csv = preprocess(test_csv, "test")

genuine_owner_id = train_csv["owner_id"].unique()

print(genuine_owner_id)

row_count = len(genuine_owner_id)
#row_count = 1
print(row_count)
bar = progressbar.ProgressBar(maxval=row_count, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

final_data = pd.DataFrame()

for i in range(row_count):
    #id = genuine_owner_id[i]
    genuine_block = train_csv.loc[train_csv['owner_id'] == genuine_owner_id[i]]
    genuine_block_head = genuine_block[["file", "owner_id", "genuine_sample_number"]]
    genuine_block = genuine_block.drop(columns=["file"])

    genuine_block = genuine_block.rename(columns={
    "genuine_sample_number": "sample_number"}, errors="raise")

    forged_block = test_csv.loc[test_csv['owner_id'] == genuine_owner_id[i]]

    #print(forged_block['owner_id'])
    genuine_data = pd.merge(genuine_block_head, genuine_block, on=['owner_id'], how='left').drop_duplicates().reset_index(drop=True)
    genuine_data["status"] = 0
    forged_data = pd.merge(genuine_block_head, forged_block, on=['owner_id'], how='inner').drop_duplicates().reset_index(drop=True)
    forged_data["status"] = 1

    #genuine_data = genuine_data.query('owner_id == signature_owner_id and genuine_sample_number != sample_number') 

    #forged_block["signed_file"] = forged_block["forged_file"].values
    #forged_block = pd.merge(genuine_block, forged_block, on=['signed_owner'], how='left').drop_duplicates().reset_index(drop=True)
    
    #genuine_block["signed_file"] = genuine_block["file"].values
    forged_data = forged_data.drop(columns=["forged_file"])

    final_data = pd.concat([forged_data, genuine_data, final_data], ignore_index=True)
    bar.update(i+1)
    gc.collect()

#train_csv = pd.merge(train_csv, test_csv, on=['signed_owner'], how='inner').drop_duplicates().reset_index(drop=True)
final_data = final_data.sort_values(by=['owner_id', 'genuine_sample_number', 'signature_owner_id','sample_number'])

#final_data = final_data[(final_data.owner_id != final_data.signature_owner_id) and (final_data.genuine_sample_number != final_data.sample_number) ]

#final_data = final_data.query('owner_id == signature_owner_id and genuine_sample_number != sample_number') 

bar.finish()
print(final_data.head())
#print(test_csv.head())


final_data.to_csv("sample_Signature/train_final.csv", index=False)

#train_csv.to_csv("sample_Signature/train.csv", index=False)
#test_csv.to_csv("sample_Signature/test.csv", index=False)

gc.collect()
