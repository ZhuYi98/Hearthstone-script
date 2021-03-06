# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *
from myGui import *

class scPveFightQuit(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveFightQuit'
        self.path='resource/mercenary/pve/scPveFightQuit'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if ('tagGroup' in tagList) and \
               ('tagQuit' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.90)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcInsure' in funcList:
            pos=funcList['funcInsure']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            MyGui.gFinish+=1
        elif 'funcQuit' in funcList:
            pos=funcList['funcQuit']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
