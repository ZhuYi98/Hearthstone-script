# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scSelectTreasury(myScene):
    def __init__(self):
        self.name='PvpSelectCard'
        self.path='resource/mercenary/pvp/scPvpSelectCard'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcDis' in funcList and 'funcTreasury' in funcList:
            pos=funcList['funcTreasury']
            pos1=[150,360,570]
            moveAndClick(pos[0]+pos[2]/2+pos1[random.randint(0,2)],pos[1]+pos[3]/2)
            return
        else:
            if 'funcSelOk' in funcList:
                if 'funcGet' in funcList:
                    pos=funcList['funcGet']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
                elif 'funcReplace' in funcList:
                    pos=funcList['funcReplace']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
                elif 'funcHold' in funcList:
                    pos=funcList['funcHold']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                    myScene.gTreasury=myScene.gTreasury+1
            elif 'funcTreasury' in funcList:
                pos=funcList['funcTreasury']
                pos1=[150,360,570]
                moveAndClick(pos[0]+pos[2]/2+pos1[random.randint(0,2)],pos[1]+pos[3]/2)