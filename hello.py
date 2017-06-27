#!/usr/bin/env python3
print('判断3个数字的最大是哪一个')
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
c = int(input('请输入第三个数字:'))
if a < b:
    max = b
else:
    max = a
if max < c:
    max = c
print('3个数字中最大的是:',max)