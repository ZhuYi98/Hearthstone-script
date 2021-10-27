# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

from tkinter import *
from threading import Thread
import time
from common import *
from autoAi import *
from monitor import *

#隐藏控制台
if 1:
    import ctypes
    hWnd=ctypes.windll.kernel32.GetConsoleWindow()
    if hWnd!=0:
        ctypes.windll.user32.ShowWindow(hWnd,0)
        ctypes.windll.kernel32.CloseHandle(hWnd)

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

        #菜单
        win=Tk()
        win.title('炉石佣兵战纪AI--by琴弦上的宇宙') #标题
        win.attributes('-alpha',0.9) #透明度
        win.attributes('-topmost',True) #置顶
        win.geometry("700x100+600+10") #大小和位置

        #运行时间
        watch=Watch(win)
        watch.start()

        #启动监控线程
        t1=Thread(target=threadMonitor)
        t1.setDaemon(True)
        t1.start()

        #启动AI线程
        t2=Thread(target=threadAutoAi)
        t2.setDaemon(True)
        t2.start()

        #运行
        win.mainloop()

    #启动
    main()