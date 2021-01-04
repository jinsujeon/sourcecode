print('hello')
import numpy as np

n,m,k  = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
print(data)

max_1 = data[-1]
max_2 = data[-2]

if max_1 == max_2:
    output = max_1 * m
else :
    max_1_num = m // k
    max_2_num = m % k
    output = max_1 * max_1_num * k + max_2 * max_2_num

print(output)