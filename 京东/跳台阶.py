'''
题目：有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或者二级，要走上m级，共有多少走法？注：规定从一级到一级有0种走法。给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100。为了防止溢出，请返回结果Mod 1000000007的值。
  测试样例：3
  返回：2
思路：这个题和上面的跳台阶不同的是，这个是站在第一个台阶上开始，之前的是都是在第0个台阶开始，所以题中说明，从第一级到第一级有0种走法。因此知道了不同后，n=1 ，0走法，n=2，1中走法，n=3,2种走法，（这就是相当于把第一级台阶当成标准跳台阶的第0个台阶）,>3的台阶，可以先跳一个，剩下n-1级，也可以先跳2个，剩下n-2个。所以，相当于是标准的跳台阶,不同的是前面开始的时候跳的不同
'''
class GoUpstairs:
    def countWays(self, n):
        res = [1, 2]
        while len(res) < n-1:
            res.append(res[-1] + res[-2])
        return res[-1] % 1000000007
