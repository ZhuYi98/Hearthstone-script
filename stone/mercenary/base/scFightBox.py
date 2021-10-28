# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scFightBox(myScene):
    def __init__(self):
        self.bValid=False
        self.name='FightBox'
        self.path='resource/mercenary/base/scFightBox'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag.png)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if ('tag1' in tagList) or \
               ('tag2' in tagList):return True
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcPass' in funcList:
            pos=funcList['funcPass']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcOk' in funcList:
            pos=funcList['funcOk']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcBox1' in funcList:
            pos=funcList['funcBox1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox2' in funcList:
            pos=funcList['funcBox2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox3' in funcList:
            pos=funcList['funcBox3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox4' in funcList:
            pos=funcList['funcBox4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
        elif 'funcBox5' in funcList:
            pos=funcList['funcBox5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
