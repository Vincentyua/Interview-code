"""
解题思路：三次翻转
"""
# -*- coding:utf-8 -*-
class Solution:
    def Reverse(self,s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        return s
    def LeftRotateString(self, s, n):
        if s is None or len(s) < 0:
            return ''
        if len(s) <= n:
            return s
        s =list(s)
        listtmp = []
        result = ''
        listtmp.append(self.Reverse(s[0:n]))
        listtmp.append(self.Reverse(s[n:]))
        r_list = sum(listtmp,[])
        return ''.join(self.Reverse(r_list))
