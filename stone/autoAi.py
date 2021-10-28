# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time

#基础
from base.scStoneStart import *
from base.scStoneInsure import *
from base.scModeChoose import *

#佣兵PVE

#佣兵PVP
from mercenary.pvp.scPvpSelectCard import *
from mercenary.pvp.scPvpSurrender import *

def threadAutoAi():
    ai=autoAi()
    ai.run()

class autoAi(object):
    def __init__(self):
        self.mode=None
        self.scene=[]

        #基础
        self.scene.append(scStoneStart())
        self.scene.append(scStoneInsure())
        self.scene.append(scModeChoose())

        #佣兵PVE

        #佣兵PVP
        self.scene.append(scPvpSelectCard())
        self.scene.append(scPvpSurrender())

    def setMode(self,mode):
        if mode=='modePvpSurrender':
            for scene in self.scene:
                if   scene.name=='StoneStart':scene.enable()
                elif scene.name=='StoneInsure':scene.enable()
                elif scene.name=='ModeChoose':scene.enable()
                elif scene.name=='PvpSelectCard':scene.enable()
                elif scene.name=='PvpSurrender':scene.enable()

    def procScene(self):
        pyautogui.screenshot('resource/big.png')
        background=cv2.imread("resource/big.png",0)
        for scene in self.scene:
            if scene.isOwn(background):
                scene.proc(background)

    def run(self):
        self.setMode('modePvpSurrender')
        while True:
            time.sleep(0.1)
            self.procScene()

