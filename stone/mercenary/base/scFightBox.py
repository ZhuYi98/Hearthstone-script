# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

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
                bFind,x,y,w,h=bFindInBackground(background,tag,0.70)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
                    break
            if ('tagBox1' in tagList) or \
               ('tagBox2' in tagList) or \
               ('tagBox3' in tagList) or \
               ('tagBox4' in tagList) or \
               ('tagBox5' in tagList) or \
               ('tagPass1' in tagList) or \
               ('tagPass2' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #开完宝箱
        for func in self.funcPng:
            if (func.name=='funcPass1') or \
               (func.name=='funcPass2'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.70)
                if bFind:
                    SaveAwardPng()
                    moveAndClick(x+w/2,y+h/2,5)
                    return

        #开宝箱
        allList=[]
        funcList={}
        for func in self.funcPng:
            if (func.name=='funcBox1') or \
               (func.name=='funcBox2') or \
               (func.name=='funcBox3') or \
               (func.name=='funcBox4') or \
               (func.name=='funcBox5'):
                bFind,okList=bFindMultInBackground(background,func,0.70)
                if bFind:funcList[func.name]=okList
        if 'funcBox1' in funcList:
            posList=funcList['funcBox1']
            for pos in posList:
                allList.append(pos)
        if 'funcBox2' in funcList:
            posList=funcList['funcBox2']
            for pos in posList:
                allList.append(pos)
        if 'funcBox3' in funcList:
            posList=funcList['funcBox3']
            for pos in posList:
                allList.append(pos)
        if 'funcBox4' in funcList:
            posList=funcList['funcBox4']
            for pos in posList:
                allList.append(pos)
        if 'funcBox5' in funcList:
            posList=funcList['funcBox5']
            for pos in posList:
                allList.append(pos)
        for pos in allList:
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
