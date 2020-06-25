import os
from pathlib import Path
from shutil import copy2

import tkinter
from tkinter import filedialog 

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator


root = tkinter.Tk() # Initialize tkinter window
root.withdraw() # hide the window

currdir = os.getcwd() # get current working directory

# Select directory of images
# image_dir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

# if len(image_dir) > 0:
    # print("Selected {} as image directory".format(str(image_dir)))

# Get web scraped images
image_dir = "./Input Images/"
output_dir = "./Output Images/"

# Saved model directory
model_dir = "./CNN/Trained/IntelImages"

# Load the trained model
cnn = tf.keras.models.load_model(model_dir,compile=False)

# Class labels of trained model
CLASS_LABELS = ['sea', 'forest', 'mountain', 'glacier', 'buildings', 'street'] 

IDG = ImageDataGenerator(rescale=1./255)

img_generator = IDG.flow_from_directory(
    directory=image_dir,
    target_size=(150, 150),
    color_mode="rgb",
    class_mode=None,
    shuffle=False
)

# Get all filepaths
files = []
for file in img_generator.filepaths:
    files.append(file)

img_generator.reset()

# Predict class labels for images
pred_labels = cnn.predict(img_generator)

# Save labels in a list
labels = []

# Make a new dir with label name for each image 
# And copy image into new dir
for i in range(len(pred_labels)):
    label = CLASS_LABELS[pred_labels[i].argmax()]
    labels.append(label)
    dest_path = output_dir+label
    Path(dest_path).mkdir(parents=True, exist_ok=True)
    copy2(files[i], dest_path)













