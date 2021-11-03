# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *
from myGui import *

class scSelectCard(myScene):
    def __init__(self):
        self.bValid=False
        self.firstPos=[0,0]
        self.offset=[-190,95]
        self.cardGroup=[190,110]
        self.name='SelectCard'
        self.path='resource/mercenary/base/scSelectCard'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
                    self.firstPos[0]=x+self.offset[0]
                    self.firstPos[1]=y+self.offset[1]
                    break
            if ('tag1' in tagList) or \
               ('tag2' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #选择卡组
        oriPos=[[[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0]]]
        for i in range(3):
            for j in range(3):
                oriPos[i][j][0]=self.firstPos[0]+self.cardGroup[0]*(j%3)+self.cardGroup[0]/2
                oriPos[i][j][1]=self.firstPos[1]+self.cardGroup[1]*(i%3)+self.cardGroup[1]/2
        card=MyGui.gCard.replace('\n','').split('-')
        pos=oriPos[int(card[0])-1][int(card[1])-1]
        moveAndClick(pos[0],pos[1])

        #点击确定
        for func in self.funcPng:
            if (func.name=='funcStart1') or \
                (func.name=='funcStart2'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                if bFind:
                    MyGui.gRound=0
                    moveAndClick(x+w/2,y+h/2,6)
                    break

        #点击锁定
        background=SaveScreen()
        for func in self.funcPng:
            if (func.name=='funcLock'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                if bFind:
                    MyGui.gRound=0
                    moveAndClick(x+w/2,y+h/2,6)
                    break
