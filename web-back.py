import numpy as np
import cv2
cap = cv2.VideoCapture('angle.mov')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
fgbg = cv2.BackgroundSubtractorMOG()

while(1):
    #import ipdb;ipdb.set_trace()
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)


    cv2.imshow('origframe',frame)
    cv2.imshow('frame',fgmask)
    key=cv2.waitKey(1)
    #print key
    if key>0 and key<255:
        if chr(key) =='q':
            break
        if chr(key)==' ':
            key2=cv2.waitKey(0)
            
cap.release()
cv2.destroyAllWindows()