# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveSelectLevel(myScene):
    def __init__(self):
        self.bValid=False
        self.offset1=[[-260,190],[-30,190],[200,190],[-260,460],[-30,460],[200,460],\
                [-170,210],[120,260],[-50,470]]
        self.offset2=[[-260,190],[-30,190],[200,190],[-260,460],[-30,460],[200,460]]
        self.offset3=[[-260,190],[-30,190],[200,190],[-260,460],[-30,460],[200,460]]
        self.offset4=[[-260,190],[-30,190],[200,190],[-260,460],[-30,460],[200,460],\
                [-170,210],[120,260],[-50,470]]
        self.zone1Pos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.zone2Pos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.zone3Pos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.zone4Pos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.name='PveSelectLevel'
        self.path='resource/mercenary/pve/scPveSelectLevel'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.70)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagReward' in tagList):
                pos=tagList['tagReward']
                zone=int((MyGui.gLevel.replace('\n','').split('-'))[0])
                if zone==1:
                    for i in range(9):
                        self.zone1Pos[i][0]=pos[0]+self.offset1[i][0]
                        self.zone1Pos[i][1]=pos[1]+self.offset1[i][1]
                elif zone==2:
                    for i in range(6):
                        self.zone2Pos[i][0]=pos[0]+self.offset2[i][0]
                        self.zone2Pos[i][1]=pos[1]+self.offset2[i][1]
                elif zone==3:
                    for i in range(6):
                        self.zone3Pos[i][0]=pos[0]+self.offset3[i][0]
                        self.zone3Pos[i][1]=pos[1]+self.offset3[i][1]
                elif zone==4:
                    for i in range(9):
                        self.zone4Pos[i][0]=pos[0]+self.offset4[i][0]
                        self.zone4Pos[i][1]=pos[1]+self.offset4[i][1]
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        zone=int((MyGui.gLevel.replace('\n','').split('-'))[0])
        level=int((MyGui.gLevel.replace('\n','').split('-'))[1])

        bStart=False
        if zone==2 or zone==3:
            if zone==2:
                pos=self.zone2Pos[level-1]
            else:
                pos=self.zone3Pos[level-1]
            moveAndClick(pos[0],pos[1],2)
            bStart=True
        elif zone==1 or zone==4:
            if zone==1:
                pos=self.zone1Pos[level-1]
            else:
                pos=self.zone4Pos[level-1]
            if level>=1 and level<=6:
                for func in self.funcPng:
                    if func.name=='funcNext':
                        bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                        if bFind:
                            moveAndClick(pos[0],pos[1],2)
                            bStart=True
                            break
                        else:
                            for func in self.funcPng:
                                if func.name=='funcPre':
                                    bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                                    if bFind:
                                        moveAndClick(x+w/2,y+h/2,2)
                                        return
            elif level>=7 and level<=9:
                for func in self.funcPng:
                    if func.name=='funcPre':
                        bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                        if bFind:
                            moveAndClick(pos[0],pos[1],2)
                            bStart=True
                            break
                        else:
                            for func in self.funcPng:
                                if func.name=='funcNext':
                                    bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                                    if bFind:
                                        moveAndClick(x+w/2,y+h/2,2)
                                        return

        #开始对战
        if bStart:
            for func in self.funcPng:
                if func.name=='funcStart':
                    bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2,2)
                        return
