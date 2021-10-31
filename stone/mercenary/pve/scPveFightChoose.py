# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

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
                bFind,x,y,w,h=bFindInBackground(background,tag,0.95)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if (('tag1' in tagList) or ('tag11' in tagList)) and \
               ('tag2' in tagList):
                return True
            else:
                return False
        else:
            return False

    def bValidButton(self):
        pyautogui.screenshot('resource/background.png')
        background=cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)
        funcList={}
        for func in self.funcPng:
             if (func.name=='funcStartInter') or \
                (func.name=='funcStartGoto') or \
                (func.name=='funcStartShow') or \
                (func.name=='funcStartGet') or \
                (func.name=='funcStartSkip'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.95)
                if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcStartInter' in funcList:
            pos=funcList['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,15)
            return True
        elif 'funcStartGoto' in funcList:
            pos=funcList['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,8)
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
        if 0:
            funcList1={}
            if 'funcTeamView' in funcList1:
                pos=funcList1['funcTeamView']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
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
                if bFind:funcList2[func.name]=(x,y,w,h)
        if 'funcStartInter' in funcList2:
            pos=funcList2['funcStartInter']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,15)
            return
        elif 'funcStartGoto' in funcList2:
            pos=funcList2['funcStartGoto']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,8)
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
        funcList4={}
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
                if bFind:funcList4[func.name]=okList
        if 'funcSurprise' in funcList4:
            posList=funcList4['funcSurprise']
            for pos in posList:
                allList.append(pos)
        if 'funcSkip1' in funcList4:
            posList=funcList4['funcSkip1']
            for pos in posList:
                allList.append(pos)
        if 'funcSkip2' in funcList4:
            posList=funcList4['funcSkip2']
            for pos in posList:
                allList.append(pos)
        if 'funcSkip3' in funcList4:
            posList=funcList4['funcSkip3']
            for pos in posList:
                allList.append(pos)
        if 'funcSkip4' in funcList4:
            posList=funcList4['funcSkip4']
            for pos in posList:
                allList.append(pos)
        if 'funcHeroRed' in funcList4:
            posList=funcList4['funcHeroRed']
            for pos in posList:
                pos[3]+=100
                allList.append(pos)
        if 'funcHeroBlue' in funcList4:
            posList=funcList4['funcHeroBlue']
            for pos in posList:
                pos[3]+=100
                allList.append(pos)
        if 'funcHeroGreen' in funcList4:
            posList=funcList4['funcHeroGreen']
            for pos in posList:
                pos[3]+=100
                allList.append(pos)
        if 'funcHeroBoss' in funcList4:
            posList=funcList4['funcHeroBoss']
            for pos in posList:
                pos[3]+=100
                allList.append(pos)
        for pos in allList:
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            if self.bValidButton():
                return
