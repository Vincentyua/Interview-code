# -*- coding:utf-8 -*-
"""
题目： 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
思路：思路一：两层遍历，时间复杂度比较高；思路二：从左上角或者右下角开始比较，这样可以最大限度的判断目标是否在这一行，时间复杂度在O(n)
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m,n=len(array),len(array[0])
        row=0
        col=n-1
        while(row<m and col>=0):
            if array[row][col]<target:
                row+=1
            elif array[row][col]>target:
                col-=1
            else:
                return True
        return False 
