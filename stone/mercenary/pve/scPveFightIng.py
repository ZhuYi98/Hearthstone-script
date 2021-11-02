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

        #循环释放技能
        while True:

            #重新截图判断
            background=SaveScreen()
            if not self.isOwn(background):return

            #准备自动上英雄（后续所有情景都需要匹配到，例如剩余0/1时）
            for func in self.funcPng:
                if (func.name=='funcHeroNone1') or \
                    (func.name=='funcHeroNone2') or \
                    (func.name=='funcHeroNone3'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2)
                        return

            #是否技能全部释放完毕
            for func in self.funcPng:
                if (func.name=='funcOk'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
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
                    (func.name=='funcSkill8'):
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
                moveAndClick(x+diffHero[0],y+diffHero[1])
                continue

            #寻找可释放技能（多图匹配）
            for f in self.funcPng:
                if f.name=='funcSkillCom':
                    func=f
                    break
            bFind,okList=bFindMultInBackground(background,func,0.70)
            if bFind:
                #特定数字，高效，需要根据自己界面调整（魔幻数字是真恶心）
                xOri=843                #第一个技能x坐标
                yOri=559                #第一个技能y坐标
                diffHero=[-10,-50]      #第一个技能相对于英雄偏移量
                diffEnemy=[100,-180]    #第一个技能相对于敌人偏移量
                Drag(xOri+diffHero[0],yOri+diffHero[1],xOri+diffEnemy[0],yOri+diffEnemy[1],1.5)
                continue

                #随机技能待调试
                if 0：
                    okList.sort()
                    pos=okList[random.randint(0,len(okList)-1)] 
                    #pos=okList[0]
                    x=pos[0]+pos[2]/2
                    y=pos[1]+pos[3]/2
                    #moveAndClick(xOri+diff1[0],yOri+diff1[1])
 
                    
