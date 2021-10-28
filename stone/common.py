# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time
import random
import numpy as np
from myGui import *

def moveAndClick(x,y,t=0.1):
    if x>10 and x<=1910 and y>10 and y<=1070:
        pyautogui.moveTo(x+random.randint(-5, 5),y+random.randint(-5, 5),duration=0)
        time.sleep(0.01)
        pyautogui.click(clicks=1)
        time.sleep(0.01)
        pyautogui.moveTo(10,10)
        time.sleep(0.01)
        pyautogui.click(clicks=1)
        time.sleep(t)
    else:
        pyautogui.moveTo(10,10)
        pyautogui.click(clicks=1)

def drag(x0,y0,x1,y1):
    if x0>10 and x0<=1910 and y0>10 and y0<=1070 and x1>10 and x1<=1910 and y1>10 and y1<=1070:
        pyautogui.mouseDown(x0+random.randint(-5,5),y0+random.randint(-5,5))
        pyautogui.moveTo(x1+random.randint(-5,5),y1+random.randint(-5,5))
        time.sleep(0.5)
        pyautogui.mouseUp(x1+random.randint(-5,5),y1+random.randint(-5,5))
        pyautogui.moveTo(10,10,)
        pyautogui.click(clicks=1)
    else:
        pyautogui.moveTo(10,10)
        pyautogui.click(clicks=1)

def bFindInBackground(background,png):
    result=cv2.matchTemplate(background,png,cv2.TM_CCOEFF_NORMED)
    w,h=png.shape[::-1]
    minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(result)
    if maxVal>0.85:
        x=maxLoc[0]
        y=maxLoc[1]
        if myScene.gDebug:
            left_top=maxLoc
            right_bottom=(left_top[0]+w,left_top[1]+h)
            img=cv2.imread("resource/background.png",1)
            cv2.rectangle(img,left_top,right_bottom,(0,0,255),2)
            img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
            print('maxVal='),
            print(maxVal)
            cv2.imshow("processed",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return True,x,y,w,h
    else:
        return False,0,0,0,0

def py_nms(dets,thresh):
    x1=dets[:, 0]
    y1=dets[:, 1]
    x2=dets[:, 2]
    y2=dets[:, 3]
    scores=dets[:, 4]
 
    areas=(x2 - x1 + 1) * (y2 - y1 + 1)
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

def bFindMultInBackground(background,png):
    i=0
    okList=[]
    result=cv2.matchTemplate(background,png,cv2.TM_CCOEFF_NORMED)
    w,h=png.shape[::-1]
    loc=np.where(result>0.85)
    score=result[result>0.85]

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
    keep_dets=py_nms(data_hstack,0.3)
    dets=data_hstack[keep_dets]

    if myScene.gDebug:
        img=cv2.imread("resource/background.png",1)
    for pt in dets:
        okList.append([int(pt[0]),int(pt[1]),w,h])
        i+=1
        if myScene.gDebug:
            right_bottom=(int(pt[0])+w,int(pt[1])+h)
            cv2.rectangle(img,pt,right_bottom,(0,0,255),2)
    if myScene.gDebug and i>=1:
        img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if i>=1:
        return True,okList
    else:
        return False,okList

class myPng(object):
    def __init__(self,path,name):
        self.name=name.split('.')[0]
        self.png=None
        if path!='' and name!='':
            p=path+'/'+str(name)
            p.replace("'","\"")
            self.png=cv2.imread(p,cv2.IMREAD_GRAYSCALE)
            #self.png=None

class myScene(object):

    gDebug=0

    def __init__(self):
        self.bValid=False
        self.name=''
        self.path=''
        self.tagPng=[myPng('','')]
        self.funcPng=[myPng('','')]
    
    def enable(self):
        self.bValid=True

    def dis(self):
        self.bValid=False

    def isOwn(self,background):
        if self.bValid:
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag.png)
                if not bFind:
                    return False
            return True
        else:
            return False

    def proc(self,background):None
