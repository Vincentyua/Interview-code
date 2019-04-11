"""
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。、
思路：两种解法，但是原理是一样的，都是遍历数组，记录数字出现的频次。一种是使用list来记录，将数字放在list对应位置，如3的频次放在list[3]的位置，遍历数组，得到这个list。然后使用sort，得到最大的频次和数组的一半长度去比较。另一种中是使用dict，遍历，将频次放在value，然后将dict按value排序变为元素为元组的list，取出最大的进行比较
"""
#字典代码：
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num_len = len(numbers)
        num_dict = {}
        for i in numbers:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] = num_dict[i] + 1
        a = sorted(num_dict.items(),key = lambda x:x[1],reverse=True)
        if a[0][1] > num_len/2:
            return a[0][0]
        else:
            return 0
#list代码：
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numlen=len(numbers)
        halflen=numlen//2
        maxans=0
        ans=[0 for i in range(0,1000)]
        for i in range(0,len(numbers)):
            ans[numbers[i]]=ans[numbers[i]]+1
            # 选出最大频次的数字
            if ans[numbers[i]]>maxans:
                maxans=numbers[i]
        ans.sort()
        ans.reverse()
        res=ans[0]
        if res>halflen:
            return maxans
        else:
            return 0
