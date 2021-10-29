# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

from threading import Thread
from myGui import *
from autoAi import *
from monitor import *

#隐藏控制台
if 0:
    import ctypes
    hWnd=ctypes.windll.kernel32.GetConsoleWindow()
    if hWnd!=0:
        ctypes.windll.user32.ShowWindow(hWnd,0)
        ctypes.windll.kernel32.CloseHandle(hWnd)

#主函数
if __name__=='__main__':
    def main():

        #菜单
        myGui=MyGui()

        #启动监控线程
        t1=Thread(target=threadMonitor)
        t1.setDaemon(True)
        t1.start()

        #启动AI线程
        t2=Thread(target=threadAutoAi)
        t2.setDaemon(True)
        t2.start()

        #运行
        myGui.win.mainloop()

    #启动
    main()
