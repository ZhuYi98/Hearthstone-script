# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *

class scPveFightChoose(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveFightChoose'
        self.path='resource/mercenary/pve/scPveFightChoose'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag.png)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if 'tagDis1' not in tagList and 'tagDis2' not in tagList:
                if ('tag1' in tagList and 'tag2' in tagList) or \
                ('tag11' in tagList and 'tag22' in tagList):return True
            else:
                return False
        else:
            return False

    def bValidButton(self):
        pyautogui.screenshot('resource/background.png')
        background=cv2.imread("resource/background.png",0)
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcStartInter' in funcList:return True
        elif 'funcStartGoto' in funcList:return True
        elif 'funcStartShow' in funcList:return True
        elif 'funcStartGet' in funcList:return True
        elif 'funcStartSkip' in funcList:return True
        else:return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func.png)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 0:
            if 'funcTeamView' in funcList:
                pos=funcList['funcTeamView']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                return
        if 'funcCard' in funcList:
            pos=funcList['funcCard']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        if 'funcComfort' in funcList:
            pos=funcList['funcComfort']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        if 'funcAward' in funcList:
            pos=funcList['funcAward']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcStartInter' in funcList:
            pos=funcList['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcStartGoto' in funcList:
            pos=funcList['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcStartShow' in funcList:
            pos=funcList['funcStartShow']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcStartGet' in funcList:
            pos=funcList['funcStartGet']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        elif 'funcStartSkip' in funcList:
            pos=funcList['funcStartSkip']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,2)
        else:
            allList=[]
            funcList={}
            for func in self.funcPng:
                bFind,okList=bFindMultInBackground(background,func.png)
                if bFind:funcList[func.name]=okList
            if 'funcSurprise' in funcList:
                posList=funcList['funcSurprise']
                for pos in posList:
                    allList.append(pos)
            if 'funcSkip1' in funcList:
                posList=funcList['funcSkip1']
                for pos in posList:
                    allList.append(pos)
            if 'funcSkip2' in funcList:
                posList=funcList['funcSkip2']
                for pos in posList:
                    allList.append(pos)
            if 'funcSkip3' in funcList:
                posList=funcList['funcSkip3']
                for pos in posList:
                    allList.append(pos)
            if 'funcSkip4' in funcList:
                posList=funcList['funcSkip4']
                for pos in posList:
                    allList.append(pos)
            if 'funcHeroRed' in funcList:
                posList=funcList['funcHeroRed']
                for pos in posList:
                    pos[3]+=100
                    allList.append(pos)
            if 'funcHeroBlue' in funcList:
                posList=funcList['funcHeroBlue']
                for pos in posList:
                    pos[3]+=100
                    allList.append(pos)
            if 'funcHeroGreen' in funcList:
                posList=funcList['funcHeroGreen']
                for pos in posList:
                    pos[3]+=100
                    allList.append(pos)
            for pos in allList:
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
                if self.bValidButton():return
