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
#解法3（不使用sort）：一个数字出现的频次要是超过了数组中个数的一半，那就是这个数字出现的个数比数组中其他数字出现次数的总和还要多，这样的话，让那个数字的频次和其他数字的频次相抵消，最后那个数字的频次应该还是大于等于1的，这样的话，我用一个值记录数组的数字，一个值记录频次，如果这个值和下一个数字相同，频次加1 ，不同的话，频次减1，如果次数为0的话，就让记录数字那个值更换为当下的数字，这样记录数字的值在频次值不为0时，记录的一定是出现次数最多的那个数字，等遍历完数组，如果存在之前提到那样的数，那一定是最后的频次值不为0的数，就意味着，记录数字的那个值就是我们想要的那个值。但是最后还要检验一下这个值得次数是不是满足大于一半数组长度的条件。因为之前的分析，只是分析出现那样的数时，最后的频次一定不为0 ，但是当最后的频次不为0时，并不是一定是满足条件的数。比如，里面存在一个刚好频次是数组长度一半的数，最后的频次就为0，这是的记录值会记录成最后一个值，那这个记录值就不满足我们的要求。
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers)<=0:
            return 0
        res=numbers[0]
        times=1
        for i in range(1,len(numbers)):
            if times==0:
                res=numbers[i]
                times=1
            elif numbers[i]==res:
                times+=1
            else:
                times-=1
        sum=0
        for j in numbers:
            if j==res:
                sum+=1
        return res if sum*2>len(numbers) else 0
