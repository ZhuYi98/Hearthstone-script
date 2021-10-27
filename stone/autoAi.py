# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time

from base.scStoneStart import *
from base.scStoneInsure import *
from base.scModeChoose import *

def threadAutoAi():
    ai=autoAi()
    ai.run()

class autoAi(object):
    def __init__(self):
        self.mode=0
        self.scene=[]

    def setScene(self,mode):
        if mode==0:
            self.scene.append(scStoneStart())
            self.scene.append(scStoneInsure())
            self.scene.append(scModeChoose())

    def procScene(self):
        pyautogui.screenshot('resource/big.png')
        background=cv2.imread("resource/big.png",0)
        for scene in self.scene:
            if scene.isOwn(background):
                scene.proc(background)
                break

    def run(self):
        self.setScene(0)
        while True:
            time.sleep(0.1)
            self.procScene()

