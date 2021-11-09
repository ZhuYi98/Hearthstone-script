# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveSelectSurprise(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveSelectSurprise'
        self.path='resource/mercenary/pve/scPveSelectSurprise'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagVisit' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #匹配图片
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.90)
            if bFind:funcList[func.name]=(x,y,w,h)

        #选择完毕
        if 'funcSel' in funcList and 'funcStart' in funcList:
            pos=funcList['funcStart']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            MyGui.gRound=99
            return

        #指定英雄碎片
        if 'funcHero1' in funcList:
            pos=funcList['funcHero1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return

        #寻找随机碎片
        for func in self.funcPng:
            if (func.name=='funcVisit'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                if bFind:
                    rand=[[-210,180],[10,180],[230,180]]
                    pos=rand[random.randint(0,2)]
                    moveAndClick(x+w/2+pos[0],y+h/2+pos[1])
                    return
