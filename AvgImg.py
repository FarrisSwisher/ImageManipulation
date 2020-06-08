#Image Manipulation: Visualize foot traffic in Ole Miss Starbucks
#Submitted March 2018
#last edited 6/8/20 (updated to work with Python 3 versions) [originally 2.7]
#
#Sum the images, get the average image, get variance & Standard Deviation
#compare the Average Image with Standard Deviation pixel by pixel
#paint the difference on the Average Image based on a threshold given by user
#


from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import glob
from PIL import Image
import os

#create some useful tings
count = 0
imgs = []
path = "./starbucks/"
imgSum = 0
imgVarTemp = 0
imgVar = 0

filenames = os.listdir(path)
pics_only = glob.glob(path + "*.jpg") #get the image files exclusively

#loop through images and put them into a list of matrices; count how many
#images we're working with
for filename in pics_only:
    img = Image.open(filename)
    img = np.float32(img)
    imgs.append(img)
    count += 1

#add each image to a sum value
for pic in imgs:
    imgSum += pic

#create the average image
imgAvg = imgSum/count

#loop through imgs again to sum the value (xi-xmean)*(xi-xmean)
for pic in imgs:
    imgVarTemp = pic - imgAvg
    imgVarTemp = imgVarTemp * imgVarTemp
    imgVar += imgVarTemp

#calculate variance and Std Dev
imgVar = imgVar/count
imgSDev = np.sqrt(imgVar)

#take in int value for change threshold
choice = int(input("Enter change threshold (0-255):\n"))

#check that threshold is valid
if choice < 0 or choice > 255:
    print ("Invalid threshold value!!")
else:  #iterate through average img to compare pixel values with change threshold
    for r in range(0, len(imgAvg)):
        for c in range(0, len(imgAvg[r])):
            SDevMag = np.sqrt(np.square(imgSDev[r,c][0])+np.square(imgSDev[r,c][1])+np.square(imgSDev[r,c][2]))
            if SDevMag >= choice:
                imgAvg[r,c] = [255,0,0]

    imgAvg = np.uint8(imgAvg)
    mplot.title("Change Threshold: " + str(choice))
    mplot.imshow(imgAvg)
    mplot.show()
