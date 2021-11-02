# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *
from myGui import *
from monitor import *

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
                bFind,x,y,w,h=bFindInBackground(background,tag,0.85)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
                    break
            if ('tag1' in tagList) or \
               ('tag2' in tagList) or \
               ('tag3' in tagList) or \
               ('tag4' in tagList) or \
               ('tag5' in tagList) or \
               ('tag6' in tagList) or \
               ('tag7' in tagList) or \
               ('tagRound' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.85)
            if bFind:
                funcList[func.name]=(x,y,w,h)
                break
        if 'func1' in funcList:
            pos=funcList['func1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func2' in funcList: #后续更改名称需要更合理，不用1/2/3等数字
            SaveAwardPng()
            pos=funcList['func2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func3' in funcList:
            SaveAwardPng()
            pos=funcList['func3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func4' in funcList:
            pos=funcList['func4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func5' in funcList:
            pos=funcList['func5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func6' in funcList:
            pos=funcList['func6']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'func7' in funcList:
            pos=funcList['func7']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcRound' in funcList:
            pos=funcList['funcRound']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
