"""
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
解题思路：解法1：设置一个变量记录遇到的丑数个数，在循环里挨个判断是否是丑数。解法2：空间换取时间。不去关注不是丑数的数，而是将丑数计算出来放在list中去取。核心在于计算丑数，保证丑数的顺序。设置三个标志，存储现有丑数序列中乘以因子倍数后刚好大于当前最大丑数的list序号，新的丑数在这三个新计算出的丑数中找最小值。
"""
#解法2代码：
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        next_index = 0
        while(next_index < index):
            min_n = min(res[t2]*2,res[t3]*3,res[t5]*5)
            res.append(min_n)
            # while保证了t记录了每个乘以因子倍数刚好大于当前最大丑数的标记
            while(res[t2]*2 <= min_n):
                t2 += 1
            while(res[t3]*3 <= min_n):
                t3 += 1
            while(res[t5]*5 <= min_n):
                t5 += 1
            next_index += 1
      return res[index-1]
