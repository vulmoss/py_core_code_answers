#!/usr/bin/env python3
#-*-coding:utf-8-*-

arr = input("please input a number: ")
num = [int(n) for n in arr.split()]
sum = 0
for i in range(len(num)):
    sum += num[i]
print(sum)
