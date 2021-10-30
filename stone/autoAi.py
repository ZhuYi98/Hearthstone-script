# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time
from common import *
from openCv import *

#基础
from base.scStoneStart import *
from base.scStoneInsure import *
from base.scModeChoose import *

#佣兵
from mercenary.base.scPointChoose import *
from mercenary.base.scSelectCard import *
from mercenary.base.scFightBox import *
from mercenary.base.scSingleHand import *

#佣兵PVE
from mercenary.pve.scPveSelectZone import *
from mercenary.pve.scPveSelectLevel import *
from mercenary.pve.scPveFightChoose import *
from mercenary.pve.scPveFightIng import *
from mercenary.pve.scPveSelectTreasury import *
from mercenary.pve.scPveSelectSurprise import *
from mercenary.pve.scPveFightQuit import *
from mercenary.pve.scPveFightFinish import *

#佣兵PVP
from mercenary.pvp.scPvpSurrender import *

def threadAutoAi():
    ai=autoAi()
    ai.run()

class autoAi(object):
    def __init__(self):
        self.mode=None
        self.allScene=[]

        #基础
        self.allScene.append(scStoneStart())
        self.allScene.append(scStoneInsure())
        self.allScene.append(scModeChoose())

        #佣兵
        self.allScene.append(scPointChoose())
        self.allScene.append(scSelectCard())
        self.allScene.append(scFightBox())
        self.allScene.append(scSingleHand())

        #佣兵PVE
        self.allScene.append(scPveSelectZone())
        self.allScene.append(scPveSelectLevel())
        self.allScene.append(scPveFightChoose())
        self.allScene.append(scPveFightIng())
        self.allScene.append(scPveSelectTreasury())
        self.allScene.append(scPveSelectSurprise())
        self.allScene.append(scPveFightQuit())
        self.allScene.append(scPveFightFinish())

        #佣兵PVP
        self.allScene.append(scPvpSurrender())

    def setMode(self,mode):
        if mode=='modePvpSurrender':
            for scene in self.allScene:
                if   scene.name=='StoneStart':scene.enable()
                elif scene.name=='StoneInsure':scene.enable()
                elif scene.name=='ModeChoose':scene.enable()
                elif scene.name=='PointChoose':scene.enable()
                elif scene.name=='SelectCard':scene.enable()
                elif scene.name=='SingleHand':scene.enable()
                elif scene.name=='FightBox':scene.enable()
                elif scene.name=='PvpSurrender':scene.enable()
        elif mode=='modePve':
            for scene in self.allScene:
                if   scene.name=='StoneStart':scene.enable()
                elif scene.name=='StoneInsure':scene.enable()
                elif scene.name=='ModeChoose':scene.enable()
                elif scene.name=='PointChoose':scene.enable()
                elif scene.name=='SelectCard':scene.enable()
                elif scene.name=='FightBox':scene.enable()
                elif scene.name=='SingleHand':scene.enable()
                elif scene.name=='PveSelectZone':scene.enable()
                elif scene.name=='PveSelectLevel':scene.enable()
                elif scene.name=='PveFightChoose':scene.enable()
                elif scene.name=='PveFightIng':scene.enable()
                elif scene.name=='PveFightQuit':scene.enable()
                elif scene.name=='PveSelectTreasury':scene.enable()
                elif scene.name=='PveSelectSurprise':scene.enable()
                elif scene.name=='PveFightFinish':scene.enable()

    def procScene(self):
        pyautogui.screenshot("resource/background.png")
        background=cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)
        for scene in self.allScene:
            if scene.isOwn(background):
                scene.proc(background)
                break

    def run(self):
        #self.setMode('modePvpSurrender')
        self.setMode('modePve')
        while True:
            time.sleep(1.5)
            self.procScene()
