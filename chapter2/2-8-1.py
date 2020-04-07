#!/usr/bin/env python2
#-*-coding:utf-8-*-

aList = [12,34,56,34,5]
sum = 0
i = 0

while i < len(aList):
    sum += aList[i]
    i += 1
print("sum = %d" % sum)
