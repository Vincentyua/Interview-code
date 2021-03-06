"""
连续输入字符串(输入字符串个数为N,每个字符串长度不大于100,输入字符串间按照空格键分隔),请按长度为8拆分每个字符串后输出到新的字符串数组,输出的字符串按照升序排列。长度不是8整数倍的字符串请在后面补数字0,空字符串不处理
输入描述:
输入内容:2 abc 123456789
输入说明:输入两个字符串(以空格分隔),其中一个为abc,另一个为123456789
输出描述:
输出结果:12345678 90000000 abc00000
输出说明abc字符串需要再后边补零,12345789拆分为12345679与9000000,0所有的字符串需要升序排列后输出(以空格分隔)
思路：先补全0，然后按8切割，输出前sort一下
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
def test(n,num):
#     num.sort(key = lambda x:len(x),reverse=True)
    num.sort()
    #print(num)
    result = []
    for i in num:
        add = len(i)% 8
        #print(add)
        i = i + "0"*(8 - add)
        #print(i)
        while(len(i)) > 0:
            result.append(i[0:8])
            i = i[8:]
    result.sort()
    print(" ".join(result))

if __name__ == '__main__':
    s = [str(x) for x in input().split(' ')]
#     test(s[0],s[1:int(s[0])+1])
    test(s[0],s[1:])
