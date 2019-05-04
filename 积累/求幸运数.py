'''
小明同学学习了不同的进制之后，拿起了一些数字做起了游戏。小明同学知道，在日常生活中我们最常用的是十进制数，而在计算机中，二进制数也很常用。现在对于一个数字x，小明同学定义出了两个函数f(x)和g(x)。 f(x)表示把x这个数用十进制写出后各个数位上的数字之和。如f(123)=1+2+3=6。 g(x)表示把x这个数用二进制写出后各个数位上的数字之和。如123的二进制表示为1111011，那么，g(123)=1+1+1+1+0+1+1=6。 小明同学发现对于一些正整数x满足f(x)=g(x)，他把这种数称为幸运数，现在他想知道，小于等于n的幸运数有多少个？
  测试样例：
  21
  返回：3
思路：其实就是10进制和2进制的转化问题
'''
def luckynumber(n):
    count = 0
    res =[]
    for i in range(1,n+1):
        sum_10 = 0
        sum_2 = 0
        ni = i
        n2 = i
        while i > 0:
            sum_10 = sum_10 + i % 10
            i = i//10
        while ni >0:
            sum_2 = sum_2 + ni % 2
            ni = ni//2
        if sum_10 == sum_2:
            count += 1
            res.append(n2)
    print(res)
    return count

if __name__=="__main__":
    n = int(input())
    print(luckynumber(n))
