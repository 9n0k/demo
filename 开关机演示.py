#coding=gb2312
import os,time

running = True

while running:

    input = raw_input('(s)关机/(q)取消：')

    if input=='s':
        os.system('shutdown -s -t 60')
    if input=='q':
        os.system('shutdown -a')
    
