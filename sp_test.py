shape=(256,256)
import cv2
import numpy as np
import dlib
path_model="./deploy.prototxt.txt"
path_weigths="./res10_300x300_ssd_iter_140000.caffemodel"
net = cv2.dnn.readNetFromCaffe(path_model, path_weigths)
def get_face_image(image):
  (h, w) = image.shape[:2]
  blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
  net.setInput(blob)
  detections = net.forward()
  ti_face=False
  for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
      ti_face=True
      box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
      (startX, startY, endX, endY) = box.astype("int")
      distanceX=abs(endX-startX)
      distanceY=abs(endY-startY)
      startY-=distanceY*0.2
      endY+=distanceY*0.1
      endX+=distanceX*0.5
      startX-=distanceX*0.5
      startX=int(max(startX,0))
      startY=int(max(startY,0))
      endX=int(min(endX,w))
      endY=int(min(endY,h))
      text = "{:.2f}%".format(confidence * 100)
      y = startY - 10 if startY - 10 > 10 else startY + 10
      image=image[startY:endY,startX:endX,:]
    if (i > -1) and confidence>0.5:
      break  
  return cv2.resize(image,(256,256)),ti_face 


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./NN3W.dat")


def get_painted(image):
  
  size=(256,256)
  image2=image[:,:,:].copy()
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  val=False
  rects = detector(gray, 1)
  for (i, rect) in enumerate(rects):
        val=True
        print("image")
        if(i>0):
          break  
        features = predictor(gray, rect)
        face=[]
        eye1=[]
        eye2=[]
        eye1u=[]
        eye2u=[]
        nose=[]
        mouth=[]
        mouth2=[]   
        for b in range(68):
            p1=[features.part(b).x,features.part(b).y]
            if(b<17):
              face.append(p1)
            if(b>=22 and b<=26):
              eye1u.append(p1) 
            if(b>=17 and b<=21):
              eye2u.append(p1)   
            if(b>=36 and b<=41):
              eye1.append(p1)
            if(b>=27 and b<=35):
              nose.append(p1)  
            if(b>=42 and b<=47):
              eye2.append(p1)
            if(b>=48 and b<=59):
              mouth.append(p1) 
            if(b>=60 and b<=68):
              mouth2.append(p1)
              
            #cv.line(image,tuple(p1),tuple(p2),(0,255,0),3)
            #cv.circle(image, (features.part(b).x,features.part(b).y), 6, (0, 255, 0), -1)  
        
        
        b_image=np.zeros_like(image)
        cv2.fillPoly(b_image,[np.array(face)],(0,255,0))
        cv2.fillPoly(b_image,[np.array(eye1)],(255,255,0))
        cv2.fillPoly(b_image,[np.array(eye2)],(255,255,0))
        
        
        cv2.fillPoly(image,[np.array(eye1)],(255,255,0))
        cv2.fillPoly(image,[np.array(eye2)],(255,255,0))
        
        
        cv2.fillPoly(b_image,[np.array(nose)],(255,0,255))
        cv2.fillPoly(b_image,[np.array(mouth)],(0,0,0))
        cv2.fillPoly(b_image,[np.array(eye1u)],(0,255,255))
        cv2.fillPoly(b_image,[np.array(eye2u)],(0,255,255))
        cv2.fillPoly(b_image,[np.array(mouth2)],(255,0,0))
        mask=cv2.inRange(image,(255,255,0),(255,255,0))
       
        mask=cv2.bitwise_and(image2,image2,mask=mask)
        G=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
        mask1=cv2.threshold(G,100,250,cv2.THRESH_BINARY)
        mask1=cv2.bitwise_and(255*np.ones_like(image),255*np.ones_like(image),mask=mask1[1])
        mask=cv2.bitwise_or(b_image,mask1)       
  return np.concatenate((image2,mask),axis=1),val      
  #return np.concatenate((cv2.resize(image2,size),cv2.resize(mask,size)),axis=1),val


def prepare_image(image):
  im1,val1=get_face_image(image)
  if(val1):
    im2,val2=get_painted(im1)
    if(val2):
      return im2,True
    else:
      print("Landmarks error")
  else:
    print("Face error")
  return cv2.resize(image,(256,256)),False
  
  
import time  
cap_source=cv2.VideoCapture(0)
window=cv2.namedWindow('Picture')
b=0
while(cap_source.isOpened()):
  for i in range(1):
    start=time.time()
    ret, frame = cap_source.read()
  try:
    if ret == True:
        outp,val=prepare_image(frame)
        if(val):
            b+=1
            
            cv2.imwrite("./dataset/"+str(b)+".jpg",outp)
            cv2.imshow('Picture',outp)
            print(time.time()-start)
            print(val)
  except:
    pass
    
  if cv2.waitKey(25) & 0xFF == ord('q'):
      break

cap_source.release()
cv2.destroyAllWindows()  
  
  
  
  




