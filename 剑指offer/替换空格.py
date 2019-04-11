"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
思路：思路一：使用python的replace函数；剑指offer思路：1.先计算源字符串数组长度，并统计空格数量 2.新字符串数组长度=源数组长度+2*空格数量 3.在新字符串数组上，从后向前遍历，通过两个index移动并复制
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # method 1:
        #return '%20'.join(s.split(' '))

        # method 2:
        #return s.replace(' ','%20')

        # method 3:
        s = list(s)
        count = 0
        for e in s :
            if e == " ":
                count += 1
        p1 = len(s) - 1
        s += [None]*2*count
        p2 = len(s) - 1
        while p1 >= 0:
            if s[p1] == " ":
                for i in ['0','2','%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s)
