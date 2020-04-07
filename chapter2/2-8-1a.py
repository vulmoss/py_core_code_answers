#!/usr/bin/env python3
#-*-coding:utf-8-*-

arr = input("please input a number: ")
aList = [int(n) for n in arr.split()]

sum_a = sum(aList)
print("sum = %d" % sum_a)
