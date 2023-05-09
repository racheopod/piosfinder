'''
   Set up our NAIP dataset. These data are from National Agricultural Imagery Program 2019 
   National Agriculture Imagery Program (NAIP) Digital Object Identifier (DOI) number: /10.5066/F7QN651G
   
   Bands are NIR, G, B

   Resolution: 60 cm
   
   Images are 256x256, hand-labeled using Google Earth Imagery (~156.3 m ground resolution)
   
   Images extracted from quarter-quad images on Google Earth Engine for positive labels and 
   for a random subset of images across Wyoming for negative labels.

   Adapted from:
   Classifier code from Benjamin Kellenberger from CV4Ecology 2022
'''

import os
import json
from torch.utils.data import Dataset
from torchvision.transforms import Compose, Resize, ToTensor
from PIL import Image
import torchvision.transforms as T


class NAIPDataset(Dataset):

    LABEL_CLASSES = {
        'None': 0,
        'Piosphere': 1
    }

    def __init__(self, cfg, split='train', transform=None):
        '''
            Constructor. Here, we collect and index the dataset inputs and labels.
        '''
        self.data_root = cfg['data_root']
        self.anno_root = cfg['anno_root']
        self.split = split
        
        self.transform = transform

        # Define data augmentations
        self.torchtransform = T.Compose([
            T.RandomHorizontalFlip(p=0.5), # Keep defaults of p = 0.5 of each transformation
            T.RandomVerticalFlip(p=0.5), # Horizontal and/or vertical flips
            T.ColorJitter(brightness=(0.95,1.5),contrast=0.01,hue=(-0.01,0.01)), # To mimic washed-out images and different seasons with different vegetation growth
            ToTensor()
        ])

        self.notransform = Compose([ToTensor()])
        
        # index data into list
        self.data = []

        # Get name of annotation file
        if self.split == 'train':
            self.annfile = 'train_annotations.json'
        elif self.split == 'val':
            self.annfile = 'val_annotations.json'
        elif self.split == 'test':
            self.annfile == 'test_annotations.json'

        # load annotation file
        annoPath = os.path.join(
            self.anno_root,
            self.annfile
        )

        meta = json.load(open(annoPath, 'r'))

        images = dict([[i['id'], i['file_name']] for i in meta['images']])          # image id to filename lookup
        labels = dict([[c['id'], idx] for idx, c in enumerate(meta['categories'])]) # custom labelclass indices that start at zero
        
        #  Want to classify if there is a piosphere in the image or not (only take category_id == 0)
        images_covered = set()      # all those images for which we have already assigned a label
        for anno in meta['annotations']:
            imgID = anno['image_id']
            # append image-label tuple to data
            # imgFileName = images[imgID]
            label = anno['category_id']
            if label == 1:
                continue
            # labelIndex = 1
            # data.append([imgFileName, labelIndex])
            images_covered.add(imgID)       # make sure image is only added once to dataset
            
        # Label all images not yet in images_covered as 0 (i.e., empty)
        addimages = set()
        for i in images:
            if i in images_covered:
                continue
            else: 
                # imgFileName = images[i]
                # print(imgFileName)
                addimages.add(i) 
            
        # Put all images into data
        for i in images:
            imgFileName = images[i]
            if i in addimages:
                self.data.append([imgFileName, 0]) # image name and 0 = empty
            elif i in images_covered:
                self.data.append([imgFileName, 1])
        print("Total images in " + split + "split: "+str(len(self.data)))

    def __len__(self):
        '''
            Returns the length of the dataset.
        '''
        return len(self.data)

    
    def __getitem__(self, idx):
        '''
            Returns a single data point at given idx.
            Here's where we actually load the image.
        '''
        image_name, label = self.data[idx]              # see lines above where we added these two items to the self.data list
        
        # load image
        image_path = os.path.join(self.data_root, self.split, image_name)
        img = Image.open(image_path)#.convert('RGB')     # all images are the same, shouldn't need to convert.

        # transform: see lines 31ff above where we define our transformations
        if self.transform:
            img_tensor = self.torchtransform(img)
        else:
            img_tensor = self.notransform(img)

        return img_tensor, label
