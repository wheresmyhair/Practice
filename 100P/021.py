#coding:utf-8
#题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个.第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


def eat(x):
    return (x/2-1)

currentcount = 1
while True:
    count = currentcount
    for i in range(9):
        count = eat(count)
    if count == 1:
        print(currentcount)
        break
    currentcount += 1
    

##########################
peach=1
for i in range(9):
    peach=(peach+1)*2
print(peach)