# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from math import *
from common import *
from openCv import *

class scPveFightChoose(myScene):
    def __init__(self):
        self.bValid=False
        self.taskPos=[0,0]
        self.name='PveFightChoose'
        self.path='resource/mercenary/pve/scPveFightChoose'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.90)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if (('tagSimple' in tagList) or ('tagHard' in tagList)) and \
               ('tagBack' in tagList) and ('tagVictory' not in tagList):
                return True
            else:
                return False
        else:
            return False

    def bValidButton(self):
        background=SaveScreen()
        funcList={}
        for func in self.funcPng:
             if (func.name=='funcStartInter') or \
                (func.name=='funcStartGoto') or \
                (func.name=='funcStartShow') or \
                (func.name=='funcStartGet') or \
                (func.name=='funcStartSkip'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                if bFind:
                    funcList[func.name]=(x,y,w,h)
                    break
        if 'funcStartInter' in funcList:
            pos=funcList['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,10)
            MyGui.gRunTime=time.time()
            return True
        elif 'funcStartGoto' in funcList:
            pos=funcList['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
            return True
        elif 'funcStartShow' in funcList:
            pos=funcList['funcStartShow']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return True
        elif 'funcStartGet' in funcList:
            pos=funcList['funcStartGet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return True
        elif 'funcStartSkip' in funcList:
            pos=funcList['funcStartSkip']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return True
        else:
            return False

    def proc(self,background):

        #N轮放弃
        if MyGui.gRound>MyGui.gAbandon:
            for func in self.funcPng:
                if (func.name=='funcTeamView'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.90)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2)
                        break
            return

        #已经查看过营火
        if MyGui.gRound==1:
            for func in self.funcPng:
                if (func.name=='funcFire'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        moveAndClick(self.taskPos[0],self.taskPos[1]-210)
                        return

        #查看是否完成任务
        if MyGui.gRound==0:
            #寻找营火
            for func in self.funcPng:
                if (func.name=='funcTask'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        self.taskPos[0]=x+w/2
                        self.taskPos[1]=y+h/2-60
                        moveAndClick(self.taskPos[0],self.taskPos[1])
                        #寻找前往按钮
                        background=SaveScreen()
                        for func in self.funcPng:
                            if (func.name=='funcStartGoto'):
                                bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                                if bFind:
                                    moveAndClick(x+w/2,y+h/2,2)
                                    break
                        break
            MyGui.gRound+=1
            return

        #寻找开始按钮
        funcList2={}
        for func in self.funcPng:
            if (func.name=='funcStartInter') or \
                (func.name=='funcStartGoto') or \
                (func.name=='funcStartShow') or \
                (func.name=='funcStartGet') or \
                (func.name=='funcStartSkip'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.95)
                if bFind:
                    funcList2[func.name]=(x,y,w,h)
                    break
        if 'funcStartInter' in funcList2:
            pos=funcList2['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,10)
            MyGui.gRunTime=time.time()
            return
        elif 'funcStartGoto' in funcList2:
            pos=funcList2['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
            return
        elif 'funcStartShow' in funcList2:
            pos=funcList2['funcStartShow']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return
        elif 'funcStartGet' in funcList2:
            pos=funcList2['funcStartGet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return
        elif 'funcStartSkip' in funcList2:
            pos=funcList2['funcStartSkip']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,3)
            return

        #寻找新关卡（mult匹配）
        allList=[]
        for func in self.funcPng:
            if (func.name=='funcSurprise') or \
                (func.name=='funcSkip1') or \
                (func.name=='funcSkip2') or \
                (func.name=='funcSkip3') or \
                (func.name=='funcSkip4') or \
                (func.name=='funcHeroRed') or \
                (func.name=='funcHeroBlue') or \
                (func.name=='funcHeroGreen') or \
                (func.name=='funcHeroBoss'):
                bFind,okList=bFindMultInBackground(background,func,0.80)
                if bFind:
                    for pos in okList:
                        if (func.name=='funcHeroRed') or \
                            (func.name=='funcHeroBlue') or \
                            (func.name=='funcHeroGreen') or \
                            (func.name=='funcHeroBoss'):
                                pos[3]+=100
                        allList.append([pos[0],pos[1],pos[2],pos[3],func.name])

        #获取有效
        allList.sort(key=lambda x:(x[1],x[0]))
        firstValid=allList[0]
        y=allList[0][1]
        newList=[]
        for pos in allList:
            if not (abs(pos[1]-y)<50):
                firstValid=pos
                break
        for pos in allList:
            if (abs(pos[1]-firstValid[1])<50):
                newList.append(pos)

        #点击操作
        for pos in newList:
            if pos[4]=='funcSurprise':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,1)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcSkip1':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcSkip2':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcSkip3':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcSkip4':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcHeroRed':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcHeroBlue':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcHeroGreen':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList:
            if pos[4]=='funcHeroBoss':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return

        #异常情况
        newList1=[]
        for pos in allList:
            if not (abs(pos[1]-firstValid[1])<50):
                newList1.append(pos)
        for pos in newList1:
            if pos[4]=='funcSurprise':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,1)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcSkip1':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcSkip2':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcSkip3':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcSkip4':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcHeroRed':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcHeroBlue':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcHeroGreen':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return
        for pos in newList1:
            if pos[4]=='funcHeroBoss':
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
                if self.bValidButton():
                    return

