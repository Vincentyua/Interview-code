"""
题目：请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
解题思路：分为两种大情况，模式为p，字符串为s：
pattern中第二位是‘*’
  如果p的第一位与s的第一位匹配（即二者第一位相等或者p的第一位是‘.’），分为三种情况：
    p后移两个字符，'*x'匹配s中0个字符（相当于'*'没用）
    p后移两个字符，s后移两个字符（匹配s中一个字符
    p不动，s后移一个字符（相当于匹配s中多个字符）
  如果p的第一位与s的第一位不匹配，p后移两个字符，s不动（匹配0个字符）
pattern中第二位不是‘*’
  如果p的第一位与s的第一位匹配（即二者第一位相等或者p的第一位是‘.’），则两者同时后移一位，匹配剩余的字符串
  如果p的第一位与s的第一位不匹配，返回false
"""
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
                #第一位相同或者p第一位是.，3种方式：p匹配0位、p匹配一位，p匹配多位
                return self.match(s[1:],pattern) or self.match(s[1:],pattern[2:]) or self.match(s,pattern[2:])
            else:
                #p第2位是*，但是p与s第一位不同，p后移两位，*匹配0位
                return self.match(s,pattern[2:])
        # p第2位不为*，第一位可匹配（相同或p是.），则匹配剩余的，否则false
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
            return self.match(s[1:],pattern[1:])
        else:
            return False
