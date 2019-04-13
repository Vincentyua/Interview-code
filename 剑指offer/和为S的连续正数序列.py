"""
题目：输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
解题思路：这个题是上一个题的扩展，思路类似，都是使用双指针的思想。使用small和big作为序列的最小值和最大值，当前序列值比给定值大时，增加small，减少序列数字个数；比给定值小，增大big，增加整体序列值得和。small最多走到(s+1)/2的位置。
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small,big = 1,2
        res = []
        cursum = small + big
        mid = (tsum+1)//2
        while(small < mid):
            if cursum == tsum:
                res.append(list(range(small,big+1)))
            while(cursum > tsum and small < mid):
                cursum -= small
                small += 1
                if cursum == tsum:
                    res.append(list(range(small,big+1)))
            big += 1
            cursum += big
        return res
