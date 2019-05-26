import cv2
import numpy as np 

#use convolve2d to flip the matrix horizontally and vertically
from scipy.signal import convolve2d, correlate2d


photo = "E:\Pictures and videos\Images/ash.jpg"
img = cv2.imread(photo)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([ [0,-1,0],
                    [-1,8,-1],
                    [0,-1,0]])

tmp = convolve2d(gray, kernel,mode='valid')
res = np.zeros(gray.shape)
res[:,:] = gray[:,:]
res[1:-1,1:-1] = tmp

rep = True
while rep:
    while True:
        cv2.imshow('Face',img)
		#Esc to change image
        if cv2.waitKey(1)==27:
            break
        #Spacebar to close program
        elif cv2.waitKey(1)==32:
            rep=False

    while True:
        cv2.imshow('Face', res)
		#Esc to change image
        if cv2.waitKey(1)==27:
            break
		#Spacebar to close program
        elif cv2.waitKey(1)==32:
            rep=False