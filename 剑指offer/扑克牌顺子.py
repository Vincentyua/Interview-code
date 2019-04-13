"""
题目：LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。
解题思路：直观的想法是将数组排序，用0去填空，如果空能够被0填满，就满足顺子，否则不满足。所以需要做的事有三步：对数组排序；统计0的数量；用0去添数组中相邻不连续的空。主要是第三步，如果存在对子，则肯定不是顺子。其次如果数组中相邻数字的间隔总数超过0的个数也不是顺子。
"""
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort() # 排序
        zeros = numbers.count(0) #统计0的个数
        for i,value in enumerate(numbers[:-1]):
            if value :
                # 判断是否有对子
                if value == numbers[i+1]:
                    return False
                # 判断0的个数能否补齐间隔数
                zeros = zeros - (numbers[i+1] - value - 1)
                if zeros < 0:
                    return False
        return True
