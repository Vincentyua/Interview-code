"""
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
解题思路：只考虑特殊情况：正负号。普通数字的使用10乘list中这个数字的index，从左到右累加
"""
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        sum_n = 0
        label = 1
        for i in range(len(s)):
            if i == 0:
                if s[i] == '-':
                    label = -1
                    continue
                elif s[i] == '+':
                    continue
            if s[i] in numbers:
                sum_n = sum_n*10 + numbers.index(s[i])
            else:
                return 0
        return sum_n*label
