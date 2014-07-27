import numpy as np
import cv2
cap = cv2.VideoCapture('long.mov')
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
#fgbg = cv2.BackgroundSubtractorMOG()
t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

def diffImg(t0, t1, t2):
   d1 = cv2.absdiff(t2, t1)
   d2 = cv2.absdiff(t1, t0)
   #cv2.imshow('d1',d1)
   #cv2.imshow('d2',d2)
   fixframe=cv2.bitwise_and(d1, d2)
   return fixframe
   #cv2.imshow('fixframe',fixframe)
#import ipdb;ipdb.set_trace()
ret,nullmask=cv2.threshold(t,0,255,cv2.THRESH_BINARY)
#nullmask=cv2.cvtColor(nullmask,cv2.COLOR_GRAY2RGB)
                      
#cv2.imshow('aaa',nullmask)

while(1):
    ret, origframe = cap.read()
    if not ret:
       print 'end'
       break
    fixframe = diffImg(t_minus, t, t_plus)
    cv2.imshow('origframe',origframe)
    cv2.imshow('frame',fixframe)
    ret,frame2white=cv2.threshold(fixframe, 40,255,cv2.THRESH_BINARY)
    frame2white=cv2.cvtColor(frame2white,cv2.COLOR_GRAY2RGB)
    #cv2.imshow('2white',frame2white)
    #import ipdb;ipdb.set_trace()
    anded=cv2.bitwise_and(frame2white,origframe,mask=nullmask)
    
    cv2.imshow('anded',anded)
    
    t_minus=t
    t=t_plus
    t_plus=cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    
    key=cv2.waitKey(1)
    #print key
    if key>0 and key<255:
        if chr(key) =='q':
            break
        if chr(key)==' ':
            key2=cv2.waitKey(0)
            
cap.release()
cv2.destroyAllWindows()