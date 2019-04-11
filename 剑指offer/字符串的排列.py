"""
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。（输入描述：输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。）
解题思路：递归的思路，序列分成两部分，第一个字符是一部分，之后的所有字符是一部分。我只要求出第二部分所有的排列加上第一个部分就是以第一部分开头的所有序列。将第一部分和后面每个字符调换位置，再采用同样的处理方式就可以得到其他字符开头的所有排列。
"""
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        result = []
        list_ss = list(ss)
        for i in list_ss:
            temp = list_ss[:]
            temp.remove(i)
            for j in self.Permutation(''.join(temp)):
                result.append(i+j)
        return sorted(list(set(result)))
