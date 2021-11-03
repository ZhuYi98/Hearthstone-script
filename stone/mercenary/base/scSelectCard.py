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
                    break
            if ('tag1' in tagList) or \
               ('tag2' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #需要修改为根据'选择一名英雄'的偏移量来计算卡组位置，不能使用绝对值
        #选择卡组
        oriPos=[[[645,395],[835,395],[1025,395]],
                [[645,505],[835,505],[1025,505]],
                [[645,615],[835,615],[1025,615]]]
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
