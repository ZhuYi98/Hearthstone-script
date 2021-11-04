# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveSelectZone(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveSelectZone'
        self.path='resource/mercenary/pve/scPveSelectZone'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagFight' in tagList):
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
        if 'funcSimple' in funcList and 'funcStart' in funcList:
            pos=funcList['funcStart']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcHard' in funcList and 'funcSelSimple' in funcList:
            pos=funcList['funcSelSimple']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcForest' in funcList:
            pos=funcList['funcForest']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
