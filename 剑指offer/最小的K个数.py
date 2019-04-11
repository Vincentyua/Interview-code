"""
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
解题思路：1.排序后选取前k个数，使用快排，复杂度O（nlogn）；2，使用一个k大小的容器，保存k个最小的数字，如果容器没满则放入，满了则取最大的那个进行置换，这样这个容器可以一直维护最小的k个数。这个容器要每次可以直接找到最大的那个数字，可以用最大堆或者红黑树来实现。这样O（1）查找，O（logk）进行删除插入。遍历整个数组，总的复杂度是O（nlogk）。
"""
#解法1代码:
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 时间复杂度为O(nlogn)
        if k > len(tinput) or not tinput:
            return []
        def quick_sort(array):
            if not array:
                return []
            pkey = array[0]
            left = quick_sort([x for x in array[1:] if x < pkey])
            right = quick_sort([x for x in array[1:] if x > pkey])
            return left+[pkey]+right 
        return quick_sort(tinput)[:k]
#解法2：
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        import heapq
        #此方法时间复杂度为O(nlogk)
        if k >len(tinput):
            return []
        return heapq.nsmallest(k,tinput)
