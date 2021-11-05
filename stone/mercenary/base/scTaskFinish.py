# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scTaskFinish(myScene):
    def __init__(self):
        self.bValid=False
        self.quitPos=[0,0]
        self.name='TaskFinish'
        self.path='resource/mercenary/base/scTaskFinish'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.80)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagFire' in tagList):
                pos=tagList['tagFire']
                self.quitPos[0]=pos[0]+w/2
                self.quitPos[1]=pos[1]-50
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        runTime=time.time()
        while True:

            #重新截图判断
            background=SaveScreen()
            if not self.isOwn(background):return

            #超时
            if ((time.time()-runTime)>5):
                moveAndClick(self.quitPos[0],self.quitPos[1])
                return

            #检测
            for func in self.funcPng:
                if func.name=='funcFinish':
                    bFind,x,y,w,h=bFindInBackground(background,func,0.70)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2)
                        return
        
