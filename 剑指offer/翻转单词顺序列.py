"""
解题思路：两次翻转
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
    def ReverseSentence(self, s):
        if s == None or len(s) < 0:
            return ''
        s = list(s)
        s = self.Reverse(s)
        pstart = 0
        pend = 0
        listtmp = []
        while pend < len(s):
            if pend == len(s) -1:
                listtmp.append(self.Reverse(s[pstart:]))
                break
            if s[pstart] == ' ':
                pend += 1
                pstart +=1
                listtmp.append(' ')
            elif s[pend] == ' ':
                listtmp.append(self.Reverse(s[pstart:pend]))
                pstart = pend
            else:
                pend += 1
        result = ''
        for i in listtmp:
            result += ''.join(i)
      return result
