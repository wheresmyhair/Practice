#coding:utf-8
#题目：暂停一秒输出，并格式化当前时间。

import time
sec = int(input('Iterations: '))
for i in range(sec):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)