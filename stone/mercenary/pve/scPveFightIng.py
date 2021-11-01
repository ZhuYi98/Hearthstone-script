# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveFightIng(myScene):
    def __init__(self):
        self.bValid=False
        self.name='PveFightIng'
        self.path='resource/mercenary/pve/scPveFightIng'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.80)
                if not bFind:return False
            return True
        else:
            return False

    def proc(self,background):
        funcList={}
        for func in self.funcPng:
            bFind,x,y,w,h=bFindInBackground(background,func,0.80)
            if bFind:funcList[func.name]=(x,y,w,h)

        #准备开始
        if 'funcHeroNone1' in funcList:
            pos=funcList['funcHeroNone1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcHeroNone2' in funcList:
            pos=funcList['funcHeroNone2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcHeroNone3' in funcList:
            pos=funcList['funcHeroNone3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return

        #AOE技能
        if 'funcSkill1' in funcList:
            pos=funcList['funcSkill1']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill2' in funcList:
            pos=funcList['funcSkill2']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill3' in funcList:
            pos=funcList['funcSkill3']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill4' in funcList:
            pos=funcList['funcSkill4']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill5' in funcList:
            pos=funcList['funcSkill5']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill6' in funcList:
            pos=funcList['funcSkill6']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill7' in funcList:
            pos=funcList['funcSkill7']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return
        elif 'funcSkill8' in funcList:
            pos=funcList['funcSkill8']
            moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            return

        #寻找通用技能
        for func in self.funcPng:
            if (func.name=='funcSkillCom'):
                bFind,okList=bFindMultInBackground(background,func,0.80)
                if bFind:
                    diff1=[-10,-50]
                    diff2=[-200,-180]
                    okList.sort()
                    first=okList[0]
                    x0=first[0]+first[2]/2+diff1[0]
                    y0=first[1]+first[3]/2+diff1[1]
                    x1=first[0]+first[2]/2+diff2[0]
                    y1=first[1]+first[3]/2+diff2[1]
                    drag(x0,y0,x1,y1)
                    i=0
                    while i<13:
                        i+=1
                        time.sleep(0)
                        x2=x1+50*i
                        Click(x2,y1)
                    return

        #寻找未释放技能
        for func in self.funcPng:
            if (func.name=='funcSkillNo'):
                bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                if bFind:
                    diff=[-30,60]
                    moveAndClick(x+w/2+diff[0],y+h/2+diff[1])
                    return
 
        #技能释放结束
        if 1:
            if 'funcOk' in funcList:
                pos=funcList['funcOk']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)
            elif 'funcError' in funcList:
                pos=funcList['funcError']
                moveAndClick(pos[0]+pos[2]/2,pos[1]+pos[3]/2)