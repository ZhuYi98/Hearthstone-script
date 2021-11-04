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
                bFind,x,y,w,h=bFindInBackground(background,tag,0.80)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
                    break
            if ('tagRound' in tagList) or \
               ('tagBuff' in tagList) or \
               ('tagNewTask' in tagList) or \
               ('tagAward1' in tagList) or \
               ('tagAward2' in tagList) or \
               ('tagHeroUp' in tagList) or \
               ('tagNewSkill' in tagList) or \
               ('tagBox' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.80)
            if bFind:
                if func.name=='funcRound':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='funcBuff':
                    moveAndClick(x+w/2,y+h/2,4)
                    break
                elif func.name=='funcNewTask':
                    SaveAwardPng()
                    moveAndClick(x+w/2,y+h/2)
                    break
                elif func.name=='funcAward1':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='funcAward2':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='funcHeroUp':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='funcNewSkill':
                    moveAndClick(x+w/2,y+h/2,5)
                    break
                elif func.name=='funcBox':
                    moveAndClick(x+w/2,y+h/2)
                    break
