# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveFightFinish(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveFightFinish'
        self.path='resource/mercenary/pve/scPveFightFinish'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcFinish' in funcList:
            pos=funcList['funcFinish']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
