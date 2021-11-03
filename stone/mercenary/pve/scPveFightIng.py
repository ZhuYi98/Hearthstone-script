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

            #准备自动上英雄
            for func in self.funcPng:
                if (func.name=='funcHeroNone1') or \
                    (func.name=='funcHeroNone2'):
                    bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                    if bFind:
                        moveAndClick(x+w/2,y+h/2,12)
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
                #增加一个右键按下弹起操作，消除卡顿时异常点击自己英雄的情况
                moveAndClick(x+diffHero[0],y+diffHero[1])
                continue

            #寻找可释放技能（多图匹配）
            for f in self.funcPng:
                if f.name=='funcSkillCom':
                    func=f
                    break
            bFind,okList=bFindMultInBackground(background,func,0.70)
            if bFind:

                #特定数字，高效，需要根据自己界面调整
                #需要修改为根据'当前技能'的偏移量来计算位置，不能使用绝对值，然后可以使用任何技能
                xOri=843                #第一个技能x坐标
                yOri=559                #第一个技能y坐标
                diffHero=[-10,-50]      #第一个技能相对于英雄偏移量
                diffEnemy=[100,-180]    #第一个技能相对于敌人偏移量
                Drag(xOri+diffHero[0],yOri+diffHero[1],xOri+diffEnemy[0],yOri+diffEnemy[1],1.5)
                continue

                '''
                随机技能待调试:
                1、全局变量drag=None
                2、判断到drag==None，说明第一次释放技能
                    2.1随机选择一个技能
                    2.2drag=当前技能图标，然后拖动，continue
                3、判断到drag!=None，说明上次有拖动过，将drag图标在全局背景中查找，
                    3.1查找到，说明drag是非指向性技能，进行点击操作，continue
                    3.2未查到，说明drag是指向性技能，已经释放成功，然后
                        3.1.1随机选择一个技能
                        3.1.2drag=当前技能图标，然后拖动，continue
                4、循环直到所有技能释放完毕
                5、技能都释放完毕，重置drag=None
                '''
                if 0:
                    okList.sort()
                    pos=okList[random.randint(0,len(okList)-1)] 
                    #pos=okList[0]
                    x=pos[0]+pos[2]/2
                    y=pos[1]+pos[3]/2
                    #moveAndClick(xOri+diff1[0],yOri+diff1[1])
 
                    
