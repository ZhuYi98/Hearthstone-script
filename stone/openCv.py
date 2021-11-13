# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import time
import random
import numpy as np
from common import *
from myGui import *

def myNms(dets,thresh):
    x1=dets[:,0]
    y1=dets[:,1]
    x2=dets[:,2]
    y2=dets[:,3]
    scores=dets[:,4]
    areas=(x2-x1+1)*(y2-y1+1)
    order=scores.argsort()[::-1]
    keep=[]
    while order.size>0:
        i=order[0]
        keep.append(i)
        xx1=np.maximum(x1[i],x1[order[1:]])
        yy1=np.maximum(y1[i],y1[order[1:]])
        xx2=np.minimum(x2[i],x2[order[1:]])
        yy2=np.minimum(y2[i],y2[order[1:]])
        w=np.maximum(0.0,xx2-xx1+1)
        h=np.maximum(0.0,yy2-yy1+1)
        inter=w*h
        ovr=inter/(areas[i]+areas[order[1:]]-inter)
        inds=np.where(ovr<=thresh)[0]
        order=order[inds+1]
    return keep

gDebug=1
gShow=0

def bFindInBackground(background,tempPng,threshold=0.80):
    w,h=tempPng.data.shape[::-1]
    result=cv2.matchTemplate(background,tempPng.data,cv2.TM_CCOEFF_NORMED)
    minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
    if maxVal>threshold:
        handle = win32gui.FindWindow("UnityWndClass", "炉石传说")
        if handle > 0:
            left, top, right, bottom = win32gui.GetWindowRect(handle)
            x = maxLoc[0] + left
            y = maxLoc[1] + top
        else:
            x = maxLoc[0]
            y = maxLoc[1]
        if gDebug:
            MyGui.gLog=tempPng.path+' S='+str(round(maxVal,2))
            print(MyGui.gLog)
            print(x,y,w,h)
            if gShow:
                img=cv2.imread("resource/background.png",1)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
                cv2.imshow("single matched",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        return True,x,y,w,h
    else:
        if gDebug:
            MyGui.gLog=tempPng.path+' NS='+str(round(maxVal,2))
            print(MyGui.gLog)
        return False,0,0,0,0

def bFindMultInBackground(background,tempPng,threshold=0.80):
    w,h=tempPng.data.shape[::-1]
    result=cv2.matchTemplate(background,tempPng.data,cv2.TM_CCOEFF_NORMED)
    minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
    loc=np.where(result>threshold)
    score=result[result>threshold]

    xmin=np.array(loc[1])
    ymin=np.array(loc[0])
    xmax=xmin+w
    ymax=ymin+h
    xmin=xmin.reshape(-1,1)
    xmax=xmax.reshape(-1,1)
    ymax=ymax.reshape(-1,1)
    ymin=ymin.reshape(-1,1)
    score=score.reshape(-1,1)
    data_hlist=[]
    data_hlist.append(xmin)
    data_hlist.append(ymin)
    data_hlist.append(xmax)
    data_hlist.append(ymax)
    data_hlist.append(score)
    data_hstack=np.hstack(data_hlist)
    keep_dets=myNms(data_hstack,0.3)
    dets=data_hstack[keep_dets]

    i=0
    okList=[]
    for pt in dets:
        handle = win32gui.FindWindow("UnityWndClass", "炉石传说")
        if handle > 0:
            left, top, right, bottom = win32gui.GetWindowRect(handle)
            x = int(pt[0]) + left
            y = int(pt[1]) + top
        else:
            x = int(pt[0])
            y = int(pt[1])
        okList.append([x,y,w,h])
        i+=1
    
    if i>=1:
        if gDebug:
            MyGui.gLog=tempPng.path+' M'
            print(MyGui.gLog)
            if gShow:
                img=cv2.imread("resource/background.png",1)
                for p in okList:
                    x=int(p[0])
                    y=int(p[1])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
                cv2.imshow("mult matched",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        return True,okList
    else:
        if gDebug:
            MyGui.gLog=tempPng.path+' NM='+str(round(maxVal,2))
            print(MyGui.gLog)
        return False,okList
