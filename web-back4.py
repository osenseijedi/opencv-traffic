import numpy as np
import cv2
cap = cv2.VideoCapture('balcony.mov')

def check_end():
   key=cv2.waitKey(1)
   if key>0 and key<255:
      if chr(key) =='q':
         return False
      if chr(key)==' ':
         key2=cv2.waitKey(0)
   return True

def show_point(event,x,y,flags,param):
   if event==cv2.EVENT_LBUTTONDOWN:
      print x,y   

cv2.namedWindow('origframe')

roi=None
ret,frame = cap.read()
track_window=None
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
print term_crit

def set_roi(event,x,y,flags,param):
   if event!=cv2.EVENT_LBUTTONDOWN:
      return
   global track_window,roi,roi_hist
   size=20
   c,r,w,h=x-size/2,y-size/2,size,size
   track_window = (c,r,w,h)
   
   # set up the ROI for tracking
   roi = frame[r:r+h, c:c+w]
   hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
   roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
   cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

   # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
   

cv2.setMouseCallback('origframe',set_roi)

while True:
   ret, frame = cap.read()
   if not ret:
      break
   if roi is not None:
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
       # apply meanshift to get the new location
       ret, track_window = cv2.CamShift(dst, track_window, term_crit)
       # Draw it on image
       #import ipdb;ipdb.set_trace()
       #pts=cv2.boxPoints(ret)
       #pts=cv2.
       pts=[ret[0],]
       pts=np.int0(pts)
       #print pts,ret
       #import ipdb;ipdb.set_trace()
       #img2 = cv2.polylines(frame, [pts], True, ,2)
       point=tuple([int(r) for r in ret[0]])
       cv2.circle(frame, point, int(ret[2]), (0,0,240,),5)
       
   cv2.imshow('origframe',frame)
   
   if not check_end():break 
           
cap.release()
cv2.destroyAllWindows()