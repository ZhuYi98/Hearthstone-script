# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scFightEnd(myScene):
    def __init__(self):
        self.bValid=False
        self.name='FightEnd'
        self.path='resource/mercenary/base/scFightEnd'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcVictory' in funcList:
            pos=funcList['funcVictory']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcDefeat' in funcList:
            pos=funcList['funcDefeat']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue1' in funcList:
            pos=funcList['funcContinue1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue2' in funcList:
            pos=funcList['funcContinue2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue3' in funcList:
            pos=funcList['funcContinue3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcContinue4' in funcList:
            pos=funcList['funcContinue4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)

