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
               ('tag8' in tagList) or \
               ('tagRound' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.85)
            if bFind:
                #后续更改名称需要更合理，不用1/2/3等数字
                if func.name=='funcRound':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='func1':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func2':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func3':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func4':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='func6':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func7':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func8':
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='func5':
                    moveAndClick(x+w/2,y+h/2)
                    break
