"""
一天,小Q得到了一个包含n个数字的数组,他想对这个数组进行K次如下的操作：
首先找出数组中最小的非0数字x,输出它,然后把数组中的所有非零数字都减去x;如果数组中的数字都是0,那么直接输出0。
输出描述：第一行两个数字n和k,用一个空格分隔;第二行n个数字,每两个数字之间用一个空格分隔。满足1<=n,k<=10^5,数组中的所有数字a(满足1<=a<=10^9).输出描述：k行,每行一个整数。
case示例：
输入：
4 1 
5 5 7 2
输出：
2
解题思路：
将数组按升序排序完成后，第一个数就是最小的，使用一个标记x来记录从数组最小端开始遇到的0，这样的话，每次减去最小得，x后向后移动，如果遇到的不是x，说明下一轮可以继续减，在数组中，每轮因为是一个一个的操作，数组中每个元素在每一轮减去的数是不一样，越往后，减去的就越大，因为他累计的轮数越多，减去的值是之前减去值的和，用sum来记录总共减去的数值。
"""
#!/usr/bin/env python
# coding=utf-8
def test(n,k,array):
    array.sort()
    x = 0
    sum = 0
    for i in range(k):
        while x < len(array):
            if array[x] - sum == 0:
                x += 1
            else:
                break
        if x==len(array):
            print(0)
        else:
            value = array[x]-sum
            print(value)
            sum+=value


if __name__ == '__main__':
    s = [int(x) for x in input().split(' ')]
    arra = [int(x) for x in input().split(' ')]=
    test(s[0],s[1],arra)
