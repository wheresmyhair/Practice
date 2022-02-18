#coding:utf-8
#题目：按逗号分隔列表。

#join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
L = [1,2,3,4,5]
print(','.join(str(n) for n in L))