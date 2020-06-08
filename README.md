# ImageManipulation
A simple (but useful) image manipulation script with dataset


The third major project in a data science class I took at the University of Mississippi with Dr. Jones (don't copy my code if
you're currently in this class - he'll know!!)

Basically, this python script reads in all of the images in the /starbucks/ directory, first summing them all together then
dividing by the total number of images used to create a mean image. After this, we use some math to find the variance then the
Standard Deviation. After this is done, the script compares each pixel of the AvgImg to the standard dev and paints it red
based on a threshold of 1-255 determined by the user.

The image set was given to me by Dr. Jones and all the images were taken by a security camera in Ole Miss's library facing the 
front of the starbucks inside it. Initially, there were some 'corrupt' files in the mix so I had to go through the set and clean
those images out so that every image run through the script was the same size.
