#coding:utf-8
#题目：模仿静态变量的用法。

def dummy():
    i=0
    print(i)
    i+=1

class cls:
    i=0
    def dummy(self):
        print(self.i)
        self.i+=1

a=cls()

for i in range(50):
    dummy()
    a.dummy()