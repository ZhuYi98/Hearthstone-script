# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveSelectZone(myScene):
    def __init__(self):
        self.bValid=False
        self.scrollPos=[0,0]
        self.name='PveSelectZone'
        self.path='resource/mercenary/pve/scPveSelectZone'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagFight' in tagList):
                pos=tagList['tagFight']
                self.scrollPos[0]=pos[0]+pos[2]/2+200
                self.scrollPos[1]=pos[1]+pos[3]/2+180
                return True
            else:
                return False
        else:
            return False

    def isZone(self,background,difficulty,zone):
        f='funcSimple1'
        if zone==1:
            if difficulty==1:f='funcSimple1'
            elif difficulty==2:f='funcHard1'
        elif zone==2:
            if difficulty==1:f='funcSimple2'
            elif difficulty==2:f='funcHard2'
        elif zone==3:
            if difficulty==1:f='funcSimple3'
            elif difficulty==2:f='funcHard3'
        elif zone==4:
            if difficulty==1:f='funcSimple4'
            elif difficulty==2:f='funcHard4'
        for func in self.funcPng:
            print(func,f)
            if func.name==f:
                bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                if bFind:
                    for func in self.funcPng:
                        if func.name=='funcStart':
                            bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                            if bFind:
                                moveAndClick(x+w/2,y+h/2,3)
                                return True
        return False

    def proc(self,background):

        difficulty=int(MyGui.gDifficulty)
        zone=int((MyGui.gLevel.replace('\n','').split('-'))[0])

        #判断副本
        if self.isZone(background,difficulty,zone):
            return
        else:
            #滚轮移动
            if zone==1 or zone==2:
                Scroll(self.scrollPos[0],self.scrollPos[1],True,10)
            elif zone==3 or zone==4:
                Scroll(self.scrollPos[0],self.scrollPos[1],False,10)

            #寻找副本
            while True:

                #重新截图判断
                background=SaveScreen()
                if not self.isOwn(background):return
            
                #找到副本
                if self.isZone(background,difficulty,zone):
                    return

                #继续寻找
                f2='funcSelSimple'
                if difficulty==2:
                    f2='funcSelHard'
                f3='funcSimple1'
                if zone==1:
                    f1='funcZone1'
                    if difficulty==1:f3='funcHard1'
                    elif difficulty==2:f3='funcSimple1'
                elif zone==2:
                    f1='funcZone2'
                    if difficulty==1:f3='funcHard2'
                    elif difficulty==2:f3='funcSimple2'
                elif zone==3:
                    f1='funcZone3'
                    if difficulty==1:f3='funcHard3'
                    elif difficulty==2:f3='funcSimple3'
                elif zone==4:
                    f1='funcZone4'
                    if difficulty==1:f3='funcHard4'
                    elif difficulty==2:f3='funcSimple4'
                bNeedClick=False
                for func in self.funcPng:
                    if func.name==f3:
                        bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                        if bFind:
                            for func1 in self.funcPng:
                                if func1.name==f2:
                                    bFind1,x,y,w,h=bFindInBackground(background,func1,0.80)
                                    if bFind1:
                                        moveAndClick(x+w/2,y+h/2)
                                        continue
                                else:
                                    bNeedClick=True
                        else:
                            bNeedClick=True

                #点击副本
                if bNeedClick:
                    for func2 in self.funcPng:
                        if func2.name==f1:
                            bFind,x,y,w,h=bFindInBackground(background,func2,0.80)
                            if bFind:
                                moveAndClick(x+w/2,y+h/2)
                                continue
