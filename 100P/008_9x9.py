#coding:utf-8
#题目：输出 9*9 乘法口诀表。

# Pandas
import pandas as pd

table = pd.DataFrame(index=range(1,10),columns=range(1,10))
for i in range(9):
    for j in range(9):
        value = table.index[i]*table.columns[j]
        table.iloc[i,j] = str(table.index[i]) + 'x' + str(table.columns[j]) + '=' + str(value)

print(table)

# Directly
for i in range(1,10):
    for j in range(1,10):
        print(f'{i}x{j}={i*j}', end=' ')
    print()