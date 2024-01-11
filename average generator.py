import math
import os

n = int(input("Give a number n: "))

    
def average(list):
    aver = sum(list)/len(list)
    return aver

list = []

for i in range(1, n+1):
    list.append(i)
    aver = (average(list))
    print(f'{i},{aver}')

