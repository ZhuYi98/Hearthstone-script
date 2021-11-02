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
        bFindAoe=False
        i=0
        xOri=843
        yOri=559
        diff1=[-10,-50]
        diff2=[100,-180]
        while True:
            pyautogui.screenshot("resource/background.png")
            background=cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)
            if not self.isOwn(background):
                return

            #准备开始
            funcList={}
            for func in self.funcPng:
                bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                if bFind:
                    funcList[func.name]=(x,y,w,h)
                    break
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
            
            #寻找技能
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
            if not bFindAoe:
                func=None
                for f in self.funcPng:
                    if f.name=='funcSkillNo':
                        func=f
                        break
                bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                if bFind:
                    diff=[-30,60]
                    moveAndClick(x+w/2+diff[0],y+h/2+diff[1])
                    continue
 
                for f in self.funcPng:
                    if f.name=='funcSkillCom':
                        func=f
                        break
                bFind,okList=bFindMultInBackground(background,func,0.70)
                if bFind:
                    i=0
                    '''
                    pos=okList[random.randint(0,len(okList)-1)]
                    pos=okList[0]
                    x=pos[0]+pos[2]/2
                    y=pos[1]+pos[3]/2
                    '''
                    drag(xOri+diff1[0],yOri+diff1[1],xOri+diff2[0],yOri+diff2[1],1.5)
                    #moveAndClick(xOri+diff1[0],yOri+diff1[1])
                else:
                    for func in self.funcPng:
                        if (func.name=='funcOk'):
                            bFind,x,y,w,h=bFindInBackground(background,func,0.80)
                            if bFind:
                                moveAndClick(x+w/2,y+h/2,10)
                                return
                    x1=xOri+diff2[0]
                    y1=yOri+diff2[1]
                    x2=x1+30*i
                    #moveAndClick(x2,y1)
                    Click(x2,y1,1.5)
                    i+=1
