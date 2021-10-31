# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time
from common import *
from openCv import *
from myGui import *

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
    ai=AutoAi()
    ai.run()

class AutoAi(object):
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

    def disScene(self,name):
        for scene in self.allScene:
            if scene.name==name:
                scene.dis()
                break

    def enableScene(self,name):
        for scene in self.allScene:
            if scene.name==name:
                scene.enable()
                break

    def setMode(self,mode):
        if mode=='modePvpSurrender':
            self.enableScene('StoneStart')
            self.enableScene('StoneInsure')
            self.enableScene('ModeChoose')
            self.enableScene('PointChoose')
            self.enableScene('SelectCard')
            self.enableScene('SingleHand')
            self.enableScene('FightBox')
            self.enableScene('PvpSurrender')
        elif mode=='modePve':
            self.enableScene('StoneStart')
            self.enableScene('StoneInsure')
            self.enableScene('ModeChoose')
            self.enableScene('PointChoose')
            self.enableScene('SelectCard')
            self.enableScene('PveSelectZone')
            self.enableScene('PveSelectLevel')
            self.enableScene('PveFightChoose')
            self.enableScene('PveFightIng')
            #self.enableScene('PveFightQuit')
            self.enableScene('PveSelectTreasury')
            self.enableScene('PveSelectSurprise')
            self.enableScene('FightBox')
            self.enableScene('PveFightFinish')
            self.enableScene('SingleHand')

    def procScene(self):
        pyautogui.screenshot("resource/background.png")
        background=cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)
        for scene in self.allScene:
            if scene.isOwn(background):
                scene.proc(background)
                if   scene.name=='PveFightChoose':
                    self.disScene('StoneStart')
                    self.disScene('StoneInsure')
                    self.disScene('ModeChoose')
                    self.disScene('PointChoose')
                    self.disScene('PveSelectZone')
                    self.disScene('PveSelectLevel')
                    self.disScene('SelectCard')
                elif scene.name=='PveFightIng':
                    self.disScene('PveFightChoose')
                    self.disScene('PveFightQuit')
                    self.disScene('PveSelectTreasury')
                    self.disScene('PveSelectSurprise')
                    self.disScene('FightBox')
                    self.disScene('PveFightFinish')
                elif scene.name=='SingleHand':
                    self.enableScene('PveFightChoose')
                    self.enableScene('PveFightQuit')
                    self.enableScene('PveSelectTreasury')
                    self.enableScene('PveSelectSurprise')
                    self.enableScene('FightBox')
                    self.enableScene('PveFightFinish')
                    self.enableScene('PveSelectLevel')
                    self.enableScene('SelectCard')
                elif scene.name=='PveFightFinish':
                    self.enableScene('PveSelectLevel')
                    self.enableScene('SelectCard')
                break

    def run(self):
        while True:
            if MyGui.gReboot:
                #self.setMode('modePvpSurrender')
                self.setMode('modePve')
                MyGui.gReboot=0
            MyGui.gWait=0.1
            time.sleep(0.1)
            self.procScene()
