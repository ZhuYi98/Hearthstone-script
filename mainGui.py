# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

from tkinter import *
from threading import Thread
import time
import sys
import os
from common import *
import monitor
import autoAi
from PIL import Image
import pytesseract

#隐藏控制台
import ctypes
hWnd=ctypes.windll.kernel32.GetConsoleWindow()
if hWnd!=0:
    ctypes.windll.user32.ShowWindow(hWnd,0)
    ctypes.windll.kernel32.CloseHandle(hWnd)

#快捷操作
def appShortcut(event):
    if event.keycode==27:
        sys.exit(0) #ESC退出

#时钟
class Watch(Frame):
    msec=1000
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._running=False
        self.timestr=StringVar()
        self._start=time.time()
        self.myRunStatus=runStatus()
        self.makeWidgets()
    def makeWidgets(self):
        l1=Label(self,textvariable=self.timestr,font=("",12))
        l1.pack()
    def _update(self):
        self._settime()
        self.timer=self.after(self.msec,self._update)
    def _settime(self):
        
        hours='{:0>2d}'.format(int((time.time()-self._start)/3600))
        minutes='{:0>2d}'.format(int((time.time()-self._start)/60%60))
        today=str(time.strftime('%m-%d %H:%M:%S',time.localtime(time.time())))+\
            '  已启动:'+hours+'小时'+minutes+'分钟'+\
            '  当前场景:'+str(myScene.gCurrScene)+' '+str(myScene.gFightTotal)+' '+str(myScene.gTreasury)+\
            '  花费时间(s):'+str(int(time.time())-self.myRunStatus.getRunTime())
        self.timestr.set(today)
    def start(self):
        self._update()
        self.place(x=10,y=70)

#主函数
if __name__=='__main__':
    def main():
        win=Tk()
        win.title('炉石佣兵战纪AI--by琴弦上的宇宙') #标题
        #win.overrideredirect(True) #无边框
        win.attributes('-alpha',0.9) #透明度
        win.attributes('-topmost',True) #置顶
        win.geometry("850x100+200+10") #大小和位置

        #标题
        #title=Label(win,text="炉石佣兵战纪AI--by琴弦上的宇宙",font=("",12))
        #title.place(x=10,y=10)

        #运行时间
        watch=Watch(win)
        watch.start()

        #绑定快捷键
        #win.bind("<Key>",appShortcut)

        #启动监控线程
        t1=Thread(target=monitor._monitor)
        t1.setDaemon(True)
        t1.start()

        #启动AI线程
        t2=Thread(target=autoAi._loopAi)
        t2.setDaemon(True)
        t2.start()

        '''
        #img = Image.open('png/333.png')
        #img=cv2.imread("png/111.png",1)
        #img=cv2.imread("png/111.png",0)
        #img=cv2.imread("png/777.png",2)
        img=cv2.imread("png/444.png")
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
        # 调用识别引擎，得到string类型的结果
        #cv2.imshow("processed",img)
        try:
            print(pytesseract.image_to_string((img),lang='chi_sim'))
        except Exception as e:
        # 访问异常的错误编号和详细信息
            print(e.args)
            print(str(e))
            print(repr(e))
        '''

        #运行
        win.mainloop()
    main()