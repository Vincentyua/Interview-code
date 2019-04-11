"""
题目： 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
解题思路：1.暴力解法，将所有的可能数字求出来，排序后取最小的。2.将所有的数字变为字符串，然后将字符串以升序排序后进行拼接
"""
#解法1（不可取）：
import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #暴力解法
        if len(numbers)<=0:
            return ""
        str_numbers=[str(i) for i in numbers]
        premu=itertools.permutations(str_numbers)
        res=[''.join(i) for i in premu]
        return min(res)
#注：permutations对容器里的元素形成全排列的迭代器
#解法2：
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) < 0:
            return 0
        str_num = [str(i) for i in numbers]
        res = sorted(str_num,cmp=lambda x,y:cmp(x+y,y+x))
        result = ''.join(res)
        return result
#注：需要说明，sorted中cmp函数是x>y则返回1，将x与y交换位置，x<y,x与y不变。由此看出是升序的两两排序。
