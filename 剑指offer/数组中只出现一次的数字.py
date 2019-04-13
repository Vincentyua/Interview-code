"""
题目：一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
解题思路：使用异或操作对数组里所有的数字进行操作，得到的结果使用移位得到异或操作为1的那位，根据这一位将数组分为两组，再使用异或操作可以得道这两个数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array)<2:
            return
        resultEOR=0
        for i in array:
            resultEOR =resultEOR^ i

        index=self.FindFirstBit(resultEOR)

        res1,res2=0,0
        for j in array:
            if self.IsBit(j,index):
                res1^=j
            else:
                res2^=j
        return [res1, res2]


    def FindFirstBit(self,num):
        '''
        用于在整数num的二进制表示中找到最右边是1的位
        '''
        indexBit=0
        while(num&1==0 and indexBit<32):
            num=num>>1
            indexBit+=1
        return indexBit


    def IsBit(self,num,indexBit):
        '''
        用于判断在num的二进制表示中从右边起的indexBit位是否为1
        '''
        num = num >> indexBit
        return (num&1)
