#coding=gb2312
import os,time

running = True

while running:

    input = raw_input('(s)�ػ�/(q)ȡ����')

    if input=='s':
        os.system('shutdown -s -t 60')
    if input=='q':
        os.system('shutdown -a')
    
