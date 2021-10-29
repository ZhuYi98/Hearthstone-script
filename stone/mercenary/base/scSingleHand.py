# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scSingleHand(myScene):
    def __init__(self):
        self.bValid=False
        self.name='SingleHand'
        self.path='resource/mercenary/base/scSingleHand'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if ('tag1' in tagList) or \
               ('tag2' in tagList) or \
               ('tag3' in tagList) or \
               ('tag4' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'func1' in funcList:
            pos=funcList['func1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func2' in funcList:
            pos=funcList['func2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func3' in funcList:
            pos=funcList['func3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func4' in funcList:
            pos=funcList['func4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
