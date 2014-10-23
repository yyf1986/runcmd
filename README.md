runcmd
======

基于salt的web界面命令执行

使用tornado框架 实现批量执行命令

启动python server.py

也可以使用supervisor来实现多线程

======
需要注意执行的目标minion不能是down的状态，结果是根据所有执行完一起返回。需要优化

