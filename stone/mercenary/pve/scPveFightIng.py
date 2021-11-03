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
        self.name='PveFightIng'
        self.path='resource/mercenary/pve/scPveFightIng'
        self.tagPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('tag')]
        self.funcPng=[myPng(self.path,png) for png in os.listdir(self.path) if png.startswith('func')]

    def isOwn(self,background):
        if self.bValid:
            for tag in self.tagPng:
                bFind,x,y,w,h=bFindInBackground(background,tag,0.80)
                if not bFind:
                    return False
                else:
                    if tag.name=='tag1':
                        self.enemyPos[0]=x+self.offset[0]
                        self.enemyPos[1]=y+self.offset[1]
            return True
        else:
            return False

    def proc(self,background):

        #循环释放技能
        while True:

            #重新截图判断
            background=SaveScreen()
            if not self.isOwn(background):return

            #准备自动上英雄
            for func in self.funcPng:
                if (func.name=='funcHeroNone1') or \
                    (func.name=='funcHeroNone2'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2,12)
                        return

            #特殊情况，对面全部隐身，直接点结束，后续看看怎么实现
            #...

            #是否技能全部释放完毕
            for func in self.funcPng:
                if (func.name=='funcOk'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        self.bLastSkill=False
                        moveAndClick(x+w/2,y+h/2,10) #战斗至少需要10秒
                        return

            #寻找AOE技能，可以都提前固定好
            bFindAoe=False
            for func in self.funcPng:
                if (func.name=='funcSkill1') or \
                    (func.name=='funcSkill2') or \
                    (func.name=='funcSkill3') or \
                    (func.name=='funcSkill4') or \
                    (func.name=='funcSkill5') or \
                    (func.name=='funcSkill6') or \
                    (func.name=='funcSkill7') or \
                    (func.name=='funcSkill8') or \
                    (func.name=='funcSkill9'):
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
                    bFind,x,y,w,h=bFindInBackground(background,self.lastSkill,0.80)
                    if bFind:
                        #拖动失败，说明为非指向性技能，需要单击
                        moveAndClick(x+40,y+40)
                    else:
                        #拖动成功，需要释放技能
                        bSkill=True

                #随机释放技能
                if bSkill:
                    okList.sort()
                    #pos=okList[random.randint(0,len(okList)-1)]#技能随机
                    #pos=okList[len(okList)-1] #技能优先4,3,2,1
                    pos=okList[0]#默认使用1技能
                    diffHero=[-20,-50]  #技能相对于英雄偏移量
                    diffSkill=[-35,-25] #技能相对于英雄偏移量
                    x=pos[0]+pos[2]/2+diffHero[0]
                    y=pos[1]+pos[3]/2+diffHero[1]
                    self.bLastSkill=True
                    self.lastSkill=SaveCutPng(x+diffSkill[0],y+diffSkill[1],50,50)
                    Drag(x,y,self.enemyPos[0],self.enemyPos[1],1.5)
                    continue
 