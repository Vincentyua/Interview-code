"""
题目：输入一个整数n,求1~n这n个整数的十进制表示中1出现的次数。例如，输入12，1~12这些整数中包含1的数字有1，10，11，12一共出现了5次。
解题思路：1.效率比较差的解法，对每个数都进行对10取余判断，然后再整除10，计算每个数中包含1的个数，然后将所有数1的个数累加。复杂度O（nlogn）；2.将每个数转化为字符串去判断。时间复杂度也是O（nlogn）
"""
#解法1：
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        totalcount = 0
        for i in range(1,n+1):
            totalcount += self.numcount(i)
        return totalcount
    def numcount(self,n):
        count = 0
        while (n > 0):
            if n % 10 == 1:
                count += 1
            n = n // 10
        return count
#解法2：
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        totalcount = 0
        for i in range(1,n+1):
            for j in str(i):
                if j == '1':
                    totalcount += 1
        return totalcount
