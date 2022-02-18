#coding:utf-8
#题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

team1 = ['a','b','c']
team2 = ['x','y','z']

match = []

for i in range(len(team1)):
    for j in range(len(team2)):
        match.append(team1[i]+team2[j])

nomatch = ['ax','xa','cx','xc','cz','zc']

lst = [x for x in match if x not in nomatch]
print(lst)