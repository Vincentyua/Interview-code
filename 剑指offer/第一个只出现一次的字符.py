"""
题目：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）
解题思路：思路1：利用Python的count特性；思路2：遍历字符串，将字符串建立一个dict（hash表），然后重新遍历字符串，并利用dict来判断出现次数
"""
#解法1：
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s or len(s)<=0:
            return -1
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1

#解法2：
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) <= 0
            return -1
        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        for index,value in enumerate(s):
            if char_dict[value] == 1:
                return index
        return -1
