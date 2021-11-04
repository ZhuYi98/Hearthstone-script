# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveSelectTreasury(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveSelectTreasury'
        self.path='resource/mercenary/pve/scPveSelectTreasury'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagTreasury' in tagList):
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
        if 'funcDis' in funcList and 'funcArrow' in funcList:
            pos=funcList['funcArrow']
            rand=[150,360,570]
            moveAndClick(pos[0]+pos[2]/2+rand[random.randint(0,2)],pos[1]+pos[3]/2,0)
            return
        else:
            if 'funcSelOk' in funcList:
                if 'funcGet' in funcList:
                    pos=funcList['funcGet']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
                elif 'funcReplace' in funcList:
                    pos=funcList['funcReplace']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
                elif 'funcHold' in funcList:
                    pos=funcList['funcHold']
                    moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
                MyGui.gRound+=1
            elif 'funcArrow' in funcList:
                pos=funcList['funcArrow']
                rand=[150,360,570]
                moveAndClick(pos[0]+pos[2]/2+rand[random.randint(0,2)],pos[1]+pos[3]/2,0)
