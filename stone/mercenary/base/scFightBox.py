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
                bFind,x,y,w,h=bFindInBackground(background,tag,0.75)
                if bFind:tagList[tag.name]=(x,y,w,h)
            if ('tag1' in tagList) or \
               ('tag2' in tagList) or \
               ('tag3' in tagList) or \
               ('tag4' in tagList) or \
               ('tag5' in tagList) or \
               ('tag6' in tagList) or \
               ('tag7' in tagList):
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.80)
            if bFind:funcList[func.name]=(x,y,w,h)
        if 'funcPass1' in funcList:
            pos=funcList['funcPass1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
        if 'funcPass2' in funcList:
            pos=funcList['funcPass2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,5)
        elif 'funcBox1' in funcList:
            pos=funcList['funcBox1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
        elif 'funcBox2' in funcList:
            pos=funcList['funcBox2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
        elif 'funcBox3' in funcList:
            pos=funcList['funcBox3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
        elif 'funcBox4' in funcList:
            pos=funcList['funcBox4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
        elif 'funcBox5' in funcList:
            pos=funcList['funcBox5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2,0)
