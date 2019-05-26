import cv2
import numpy as np 
from scipy.signal import correlate2d

photo = "E:\Pictures and videos\Changu Narayan\kdn's snap\Photos - Changunarayan hiking\IMG20190415124809.jpg"
photo = "E:\Pictures and videos\Images/ash.jpg"
img = cv2.imread(photo)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([ [0,-1,0],
                    [-1,8,-1],
                    [0,-1,0]])
# kernel = np.ones((3,3))

tmp = correlate2d(gray, kernel,mode='valid')
res = np.zeros(gray.shape)
res[:,:] = gray[:,:]
res[1:-1,1:-1] = tmp

rep = True
while rep:
    while True:
        cv2.imshow('Face',img)
        if cv2.waitKey(1)==27:
            break

    while True:
        cv2.imshow('Face', res)
        if cv2.waitKey(1)==27:
            break
        elif cv2.waitKey(1)==32:
            rep=False