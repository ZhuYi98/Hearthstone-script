# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPointChoose(myScene):
    def __init__(self):
        self.bValid=False
        self.pvePos=[0,0]
        self.pvpPos=[0,0]
        self.offsetPve=[160,180]
        self.offsetPvp=[420,230]
        self.name='PointChoose'
        self.path='resource/mercenary/base/scPointChoose'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagMercenary' in tagList):
                pos=tagList['tagMercenary']
                self.pvePos[0]=pos[0]+self.offsetPve[0]
                self.pvePos[1]=pos[1]+self.offsetPve[1]
                self.pvpPos[0]=pos[0]+self.offsetPvp[0]
                self.pvpPos[1]=pos[1]+self.offsetPvp[1]
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #判断当前佣兵模式
        if MyGui.gMercenaryMode=='pveMode':
            moveAndClick(self.pvePos[0],self.pvePos[1])
        elif MyGui.gMercenaryMode=='pvpMode':
            moveAndClick(self.pvpPos[0],self.pvpPos[1],3)
