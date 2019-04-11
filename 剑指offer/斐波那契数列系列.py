"""
主要是递归的思想，无论是跳台阶还是覆盖这类题，递归的思想去表示，就能找到满足的数列规律，一般都是斐波那契数列的变种。
题目一：斐波那契数列
题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39。n=0时，f(n)=0， n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)
思路；解法一：基于递归。解法二：基于循环，维护两个值，交替的往后走；
"""
#代码（递归）：
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        elif n==1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)
#代码（循环）：
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        small=0
        big=1
        if n<=0:
            return 0
        if n==1:
            return 1
        for i in range(2,n+1):
            small,big = big,small + big
        return big
"""
题目二：跳台阶
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：找出地推表达式，n>2时，f(n)=f(n-1)+f(n-2)
"""
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        small,big=1,2
        for i in range(2,number):
            sum_i=small+big
            small=big
            big=sum_i
        return big
"""
扩展：变态跳台阶
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：数学归纳法
"""
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=0:
            return 0
        return 2**(number-1)
"""
扩展：矩形覆盖
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？ 
思路：这道题本质上还是斐波那契数列问题，注意分析n=0,1,2,3,...的值的情况。
"""
