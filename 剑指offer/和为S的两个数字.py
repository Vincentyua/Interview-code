"""
题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
解题思路：双指针法，从两边向中间来回的移动，判断是否满足条件
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        fst,lst= 0,len(array)-1
        while(fst <= lst):
            nsum = array[fst] + array[lst]
            if tsum == nsum:
                return [array[fst],array[lst]]
            elif tsum < nsum:
                lst -= 1
            else:
                fst += 1
        return []
