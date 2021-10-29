# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveFightQuit(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveFightQuit'
        self.path='resource/mercenary/pve/scPveFightQuit'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcInsure' in funcList:
            pos=funcList['funcInsure']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcQuit' in funcList:
            pos=funcList['funcQuit']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
