import os
from os.path import isfile, join
from pathlib import Path
from PIL import Image
from PIL import ImageEnhance
import torchvision.transforms as transforms
import torch.utils.data as utils
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import gc
import torch
import numpy as np

class SignaturesDataset():
    
    def __init__(self, train, genuine_path, training_dir=None, transform=None, enhance_factor=4.5):
        # used to prepare the labels and images path
        self.training_df = train
        self.columns = ["file","signed_file","status"]
        self.training_dir = training_dir    
        self.transform = transform
        self.genuine_path = genuine_path
        self.enhance_factor = enhance_factor

    def _enhance(self, image):
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(self.enhance_factor)

    def __getitem__(self,index):
        
        # getting the image path
        original_path=os.path.join(
            self.genuine_path,
            self.training_df.iloc[index][self.columns[0]])

        compare_path=os.path.join(
            self.training_dir,
            self.training_df.iloc[index][self.columns[1]])
        
        target = torch.from_numpy(
            np.array([int(self.training_df.iloc[index][self.columns[2]])],dtype=np.float32))

        # Loading the image
        original_img = self._enhance(Image.open(original_path))
        compare_img = self._enhance(Image.open(compare_path))

        original_img = original_img.convert("L")
        compare_img = compare_img.convert("L")

        #original_img = np.array(original_img)
        #compare_img = np.array(compare_img)

        data_transform = transforms.Compose([#transforms.ToPILImage(),
                                            transforms.Resize((105,105), Image.ANTIALIAS),
                                            #transforms.Grayscale(1),
                                            #transforms.RandomResizedCrop(224),
                                            #transforms.RandomHorizontalFlip(),
                                            #transforms.RandomVerticalFlip(),
                                            #transforms.RandomRotation(degrees=40), 
                                            transforms.ToTensor(),
                                            #transforms.Normalize(mean=[0.456], std=[0.224])
                                            #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                                            ])
        
        test_transform = transforms.Compose([#transforms.ToPILImage(),
                                            transforms.Resize((105,105), Image.ANTIALIAS),
                                            #transforms.Grayscale(1),
                                            #transforms.Resize(256),
                                            #transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            #transforms.Normalize(mean=[0.456], std=[0.224])
                                            #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                                            ])
        
        # Apply image transformations
        if self.transform == "train":
            original_img = data_transform(original_img)
            compare_img = data_transform(compare_img)
        else:
            original_img = test_transform(original_img)
            compare_img = test_transform(compare_img)
        
        return original_img, compare_img , target
    
    def __len__(self):
        return len(self.training_df)


class SignaturesCompareDataset():
    
    def __init__(self, genuine_path, compare_path, enhance_factor=4.5):
        # used to prepare the labels and images path
        self.genuine_path = genuine_path
        self.compare_path = compare_path
        self.enhance_factor = enhance_factor

    def _enhance(self, image):
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(self.enhance_factor)

    def __getitem__(self):
        
        # getting the image path
        original_path = self.genuine_path
        compare_path = self.compare_path        
        target = torch.from_numpy(np.array([int(0)],dtype=np.float32))

        # Loading the image
        original_img = self._enhance(Image.open(original_path))
        compare_img = self._enhance(Image.open(compare_path))

        original_img = original_img.convert("L")
        compare_img = compare_img.convert("L")

        #original_img = np.array(original_img)
        #compare_img = np.array(compare_img)
        
        test_transform = transforms.Compose([#transforms.ToPILImage(),
                                            transforms.Resize((105,105), Image.ANTIALIAS),
                                            #transforms.Grayscale(1),
                                            #transforms.Resize(256),
                                            #transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            #transforms.Normalize(mean=[0.456], std=[0.224])
                                            #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                                            ])
        
        # Apply image transformations
        original_img = test_transform(original_img)
        compare_img = test_transform(compare_img)
        
        return original_img, compare_img , target

    def __getimages__(self):

        # getting the image path
        original_path = self.genuine_path
        compare_path = self.compare_path        
        target = torch.from_numpy(np.array([int(0)],dtype=np.float32))

        # Loading the image
        original_img = self._enhance(Image.open(original_path))
        compare_img = self._enhance(Image.open(compare_path))

        original_img = original_img.convert("L")
        compare_img = compare_img.convert("L")

        #original_img = np.array(original_img)
        #compare_img = np.array(compare_img)
        
        test_transform = transforms.Compose([#transforms.ToPILImage(),
                                            transforms.Resize((105,105), Image.ANTIALIAS),
                                            #transforms.Grayscale(1),
                                            #transforms.Resize(256),
                                            #transforms.CenterCrop(224),
                                            #transforms.ToTensor(),
                                            #transforms.Normalize(mean=[0.456], std=[0.224])
                                            #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                                            ])
        
        # Apply image transformations
        original_img = test_transform(original_img)
        compare_img = test_transform(compare_img)
        
        return original_img, compare_img