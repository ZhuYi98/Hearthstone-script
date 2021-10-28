# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scPveSelectSurprise(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveSelectSurprise'
        self.path='resource/mercenary/pve/scPveSelectSurprise'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if ('funcHero1Sel' in funcList or \
            'funcHero2Sel' in funcList) \
            and 'funcStart' in funcList:
            pos=funcList['funcStart']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcHero1' in funcList:
            pos=funcList['funcHero1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcHero2' in funcList:
            pos=funcList['funcHero2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
