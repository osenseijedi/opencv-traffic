import cv2
import numpy as np
last=None

def threshed(img):
    #print type(img)
    #shape=img.shape()
    #print shape
    #rows,cols,channels=shape
    #roi=img[0:rows, 0:cols]
    return img
    ret,threshed=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
    return threshed

def merged(img):
    global last
    if last is not None:
        new=cv2.addWeighted(img,0.5,last,0.5,0)
        last=new
        return new
    else:
        last=img
        return img

def vid():

    cap=cv2.VideoCapture(0)
    
    
    while 1:
        ret,frame=cap.read()
        
        #grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #grey=threshed(frame)
        grey=merged(frame)
        grey=threshed(frame)
        cv2.imshow('frame',grey)
        key=cv2.waitKey(1)
        print key
        if key>0 and chr(key) =='q':
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
#img1=cv2.imread('test.jpg')
#img2=cv2.imread('test2.jpg')

#dst=cv2.addWeighted(img1,0.4,img2,0.3,0)

#cv2.imshow('dst',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
vid()