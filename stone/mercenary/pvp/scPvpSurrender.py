# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPvpSurrender(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PvpSurrender'
        self.path='resource/mercenary/pvp/scPvpSurrender'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if not bFind:return False
            return True
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.90)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcSurrender' in funcList:
            pos=funcList['funcSurrender']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcSet' in funcList and 'funcDis' not in funcList:
            pos=funcList['funcSet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2) 
