# Hearthstone-script

#### 介绍
炉石传说脚本

待修改bug和优化功能：
1. 每局开始时，查看神秘人在哪边，优先走哪边，后续再动态规划最佳路线
2. 或者每局开始，把所有敌人情况拿到，直接规划最佳路线
3. 考虑使用pyinstaller生成exe方便使用

#### 软件架构
1. 本脚本主要是个人爱好，学习使用，也可以修改为其他模式，自由度比较大
2. 当前匹配的分辨率为1366*768，后续更新为模糊匹配，不限制分辨率
3. 有想法和建议的可以加群，一起学习和进步；QQ群：126894161

核心思路：
1. 匹配tag图片（可以上下左右4个角落），定位到当前属于哪种场面（唯一性）
2. 根据匹配到的场面进行function处理
3. 继续循环

佣兵场面如下：
1. 炉石游戏入口
2. 炉石提示
3. 佣兵战纪入口（点击掉商城等提示）
4. 副本入口（检测仍在后，多点击几次）
5. 副本选择（第二关，普通）
6. 大关卡选择（2-4或2-6）
7. 卡组选择
8. 小关卡选择（优先选择不用打怪的，神秘人等）
9. 小关卡战斗中（回合开始直接结束，点击aoe技能，继续结束）
10. 小关卡战斗结束（多点击几次，直到结束）
11. 小关卡宝藏选择，之后跳转到8（宝藏随机选择，尽量避免不利宝藏）
12. 2轮小战斗结束或者继续
13. 大关卡战斗结束奖励，完成开箱子
14. 之后跳转到6（多点击几次，直到结束）

备注：每完成一轮战斗，记录时间、标志、其他数据等进行展示
检测到一定时间内未完成，重启炉石和战网，循环1-14

#### 安装教程

运行cmd，依次输入以下内容：

0. pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
1. pip install opencv-python
2. pip install pillow
3. pip install pyautogui
4. pip install pywin32
5. pip install win32gui （Python3.10等高级版本不需要安装，已经内置） 

备注：Python3.10等高级版本安装5失败后，就安装4

#### 使用说明

1. 环境安装完成后，直接双击运行stoneMain.py即可
2. 可以根据自己的需求调试相关功能，打开对应开关即可

![运行效果图](https://images.gitee.com/uploads/images/2021/1106/230520_39c51f67_9929826.png "QQ拼音截图20211106230402.png")

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
