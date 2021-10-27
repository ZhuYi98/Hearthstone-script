# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import win32gui,win32con
import time
import os
import numpy as np
import random

from sceneInterBattle import *
from sceneInterStone import *
from sceneInterMerce import *
from sceneInterZone import *

from sceneSelectZone import *
from sceneSelectLevel import *
from sceneSelectCard import *
from sceneSelectTreasury import *
from sceneSelectSurprise import *

from sceneFightChoose import *
from sceneFightIng import *
from sceneFightEnd import *
from sceneFightQuit import *
from sceneFightAward import *
from sceneFightBox import *
from sceneFightShow import *
from sceneFightFinish import *

from scenePvpSelectCard import *
from scenePvpSurrender import *

'''
匹配几个额外图片（可以上下左右4个角落），定位到当前属于那种场面

场面：
1、(100%)炉石游戏入口
2、(100%)炉石提示
3、(100%)佣兵战纪入口（点击掉商城等提示）
4、(100%)副本入口（检测仍在后，多点击几次）
5、(100%)副本选择（第二关，普通）
6、(100%)大关卡选择（2-4或2-6）
7、(100%)卡组选择
8、小关卡选择（优先选择不用打怪的，神秘人等）
9、(100%)小关卡战斗中（回合开始直接结束，点击aoe技能，继续结束）
10、(100%)小关卡战斗结束（多点击几次，直到结束）
11、(100%)小关卡宝藏选择，之后跳转到8（宝藏随机选择，尽量避免不利宝藏）
12、2轮小战斗结束，放弃重新开始
13、大关卡战斗结束奖励，之后跳转到6（多点击几次，直到结束）

备注：每完成一轮战斗，记录时间和标志，
检测到一定时间内未完成，重启炉石和战网，循环1-12

步骤：

1、循环检测当前属于哪种场面，未检测到任意场面，继续循环，检测到后记为A场面
2、跳转到A场面处理逻辑（图像检测效果不好，可以先把鼠标移动到右下角，避免影响图像检测）
3、A处理完后，处理后酌情给延时，之后跳转1
'''

class autoAi(object):
    def __init__(self):
        self.scene=[]
        '''
        self.scene.append(sceneSelectZone(''))
        self.scene.append(sceneSelectLevel(''))
        #self.scene.append(sceneSelectCard(''))
        self.scene.append(sceneSelectTreasury(''))
        self.scene.append(sceneSelectSurprise(''))

        self.scene.append(sceneFightChoose(''))
        #self.scene.append(sceneFightIng(''))
        
        self.scene.append(sceneFightQuit(''))
        self.scene.append(sceneFightAward(''))
        self.scene.append(sceneFightBox(''))
        self.scene.append(sceneFightShow(''))
        self.scene.append(sceneFightFinish(''))
        '''

        self.scene.append(sceneInterBattle(''))
        self.scene.append(sceneInterStone(''))
        self.scene.append(sceneInterMerce(''))
        self.scene.append(sceneInterZone(''))
        self.scene.append(scenePvpSelectCard(''))
        self.scene.append(scenePvpSurrender(''))
        self.scene.append(sceneFightEnd(''))
        self.scene.append(sceneFightBox(''))
        self.scene.append(sceneFightShow(''))

    def procScene(self):
        pyautogui.screenshot('png/big.png')
        background=cv2.imread("png/big.png",0)
        for scene in self.scene:
            if scene.isOwn(background):
                scene.proc(background)
                break

    def run(self):
        while True:
            time.sleep(0.1)
            self.procScene()

def _loopAi():
        ai=autoAi()
        ai.run()
