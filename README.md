介绍
======
基于salt的web界面命令执行

使用tornado框架，实现批量执行命令

也可以使用supervisor来实现多线程

界面比较简单，只是实现了基本功能，没有添加state配置执行权限

功能
======
批量执行命令，针对node，list，grains

接受、删除key（可以与cmdb结合）

注意
======
执行的目标minion不能是down的状态，结果是所有执行完一起返回。需要优化
