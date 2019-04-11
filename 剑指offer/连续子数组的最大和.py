"""
题目：输入一个整形数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O（n）
解题思路：使用动态规划的思路，从前往后遍历，维护两个值，一个是当前的累加子数组和，一个是当前的最大子数组和。最重要的是在当前累加子数组和为0时，就丢掉了之前的最大子数组和从新计算。
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array or len(array) <= 0:
            return 0
        cursum = 0
        greatsum = float('-inf')
        for i in array:
            if cursum <= 0:
                cursum = i
            else:
                cursum += i
            if cursum > greatsum:
                greatsum = cursum
        return greatsum
