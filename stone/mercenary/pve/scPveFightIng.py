# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
from common import *
from openCv import *

class scPveFightIng(myScene):
    def __init__(self):
        self.bValid=False
        self.enemyPos=[0,0]
        self.offset=[-480,-320]
        self.bLastSkill=False
        self.lastSkill=None
        self.endPos=[0,0]
        self.name='PveFightIng'
        self.path='resource/mercenary/pve/scPveFightIng'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            tagList={}
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.80)
                if bFind:
                    tagList[tag.name]=(x,y,w,h)
            if ('tagSkull' in tagList):
                self.enemyPos[0]=x+self.offset[0]
                self.enemyPos[1]=y+self.offset[1]
                return True
            else:
                return False
        else:
            return False

    def proc(self,background):

        #循环释放技能
        runTime=time.time()
        while True:

            #重新截图判断
            background=SaveScreen()
            if not self.isOwn(background):return

            #技能释放超时(对面有隐身、自己抉择技能等)，直接点结束
            if ((time.time()-runTime)>30):
                Click(self.endPos[0],self.endPos[1],b='right')
                moveAndClick(self.endPos[0],self.endPos[1],10) #战斗至少需要10秒
                return

            #准备自动上英雄
            for func in self.funcPng:
                if (func.name=='funcHeroNone1') or \
                    (func.name=='funcHeroNone2') or \
                    (func.name=='funcHeroNone3'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.75)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2,12)
                        return

            #是否技能全部释放完毕
            for func in self.funcPng:
                if (func.name=='funcOk'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        self.bLastSkill=False
                        self.endPos[0]=x+w/2
                        self.endPos[1]=y+h/2
                        moveAndClick(x+w/2,y+h/2,10) #战斗至少需要10秒
                        return

            #寻找第一轮就能释放的AOE技能，可以都提前固定好
            bFindAoe=False
            if (MyGui.gSkill=='1') or \
                (MyGui.gSkill=='2') or \
                (MyGui.gSkill=='3') or \
                (MyGui.gSkill=='4') or \
                (MyGui.gSkill=='5') or \
                (MyGui.gSkill=='6'):
                for func in self.funcPng:
                    if (func.name=='funcAoe1') or \
                        (func.name=='funcAoe2') or \
                        (func.name=='funcAoe3') or \
                        (func.name=='funcAoe4') or \
                        (func.name=='funcAoe5') or \
                        (func.name=='funcAoe6') or \
                        (func.name=='funcAoe7'):
                        bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                        if bFind:
                            bFindAoe=True
                            moveAndClick(x+w/2,y+h/2)
                            break
                        else:
                            bFindAoe=False
                if bFindAoe:continue

            #寻找等待一回合的AOE技能，可以都提前固定好
            if (MyGui.gSkill=='1') or \
                (MyGui.gSkill=='2') or \
                (MyGui.gSkill=='3') or \
                (MyGui.gSkill=='4') or \
                (MyGui.gSkill=='5') or \
                (MyGui.gSkill=='6'):
                for func in self.funcPng:
                    if (func.name=='funcAoeWait1') or \
                        (func.name=='funcAoeWait2') or \
                        (func.name=='funcAoeWait3') or \
                        (func.name=='funcAoeWait4') or \
                        (func.name=='funcAoeWait5') or \
                        (func.name=='funcAoeWait6') or \
                        (func.name=='funcAoeWait7') or \
                        (func.name=='funcAoeWait8') or \
                        (func.name=='funcAoeWait9') or \
                        (func.name=='funcAoeWait10'):
                        bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                        if bFind:
                            bFindAoe=True
                            moveAndClick(x+w/2,y+h/2)
                            break
                        else:
                            bFindAoe=False
                if bFindAoe:continue

            #寻找未释放技能英雄（多图匹配）
            func=None
            for f in self.funcPng:
                if f.name=='funcSkillNo':
                    func=f
                    break
            bFind,okList=bFindMultInBackground(background,func,0.70)
            if bFind:
                diffHero=[-30,60]
                okList.sort()
                pos=okList[0]
                x=pos[0]+pos[2]/2
                y=pos[1]+pos[3]/2
                self.bLastSkill=False
                Click(x+diffHero[0],y+diffHero[1],b='right')
                moveAndClick(x+diffHero[0],y+diffHero[1])
                continue

            #寻找可释放技能（多图匹配）
            for f in self.funcPng:
                if f.name=='funcSkillCom':
                    func=f
                    break
            bFind,okList=bFindMultInBackground(background,func,0.70)
            if bFind:

                #释放新技能
                bSkill=False
                if not self.bLastSkill:
                    bSkill=True
                else:
                    #判断上次技能是否拖动成功
                    bFind,x,y,w,h=bFindInBackground(background,self.lastSkill,0.90)
                    if bFind:
                        #拖动失败，说明为非指向性技能，需要单击
                        moveAndClick(x+23,y+23)
                    else:
                        #拖动成功，需要释放技能
                        bSkill=True

                #释放技能
                if bSkill:
                    okList.sort()
                    cnt=len(okList)
                    pos=okList[0]
                    if MyGui.gSkill=='8' and cnt>=2:
                        pos=okList[1]
                    elif MyGui.gSkill=='9' and cnt>=3:
                        pos=okList[2]
                    elif MyGui.gSkill=='10' and cnt>=4:
                        pos=okList[3]
                    elif MyGui.gSkill=='11' and cnt>=5:
                        pos=okList[4]
                    elif MyGui.gSkill=='6':
                        pos=okList[random.randint(0,len(okList)-1)]
                    elif MyGui.gSkill=='12':
                        pos=okList[random.randint(0,len(okList)-1)]
                    diffHero=[-15,-50]
                    diffSkill=[-25,-20]
                    x=pos[0]+pos[2]/2+diffHero[0]
                    y=pos[1]+pos[3]/2+diffHero[1]
                    self.bLastSkill=True
                    self.lastSkill=SaveLastSkillPng(x+diffSkill[0],y+diffSkill[1],46,46)
                    Drag(x,y,self.enemyPos[0],self.enemyPos[1],1.5)
                    continue
 