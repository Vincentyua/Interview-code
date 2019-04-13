"""
小Q在进行一个对数字进行拆分的游戏,游戏规如下：小Q最初只有一个整数N,接下来每一轮中,小Q被允许对现有的每个数进行下面两个操作之一：
1、对当前小Q手里的所有数减1
2、把所有数都拆分为更小的两个数之和但是拆分操作只允许使用至多k次,现在小Q想知首把N完全消去需要多少轮操作。
输入描述输入一行包含两个整数N,K,1<N<=100,0<K<=100。输出描述：输出一个整数,表示至少需要的轮数。
case示例：输入5 2，输出4；输入15 4，输出6
解题思路：
每次拆分时，尽量拆分成两个相等或者相差为1的数，这样的话，规则2用完后，所有拆分的数的大小都是差不太多的，这个时候，只用规则1，很容易消去剩下的数。
"""
#!/usr/bin/env python
# coding=utf-8
def test(n,k):
    for i in range(k):
        if n==1:
            return i+1
    #让n每次成为拆分后较大的数
        n = (n+1)//2
    return k+n

if __name__ == '__main__':
    s = [int(x) for x in input().split(' ')]
    print(test(*s))
