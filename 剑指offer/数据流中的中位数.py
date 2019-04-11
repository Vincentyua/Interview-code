"""
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
解题思路：1.排序后再求中位数。2.使用一个大顶堆，一个小顶堆，大顶堆存数据流的前半部分，小顶堆存储数据流的后半部分，当数据总长度为偶数时，存入小顶堆，奇数时存入大顶堆。当插入小顶堆的数据比大顶堆的部分还要小时，应该先将这个数插入大顶堆，然后将大顶堆最大的数，插入小顶堆。当要插入大顶堆，但是插入的数比小顶堆的部分偏大时，做法和之前类似。这个做法是为了保证数据流的有序。这样整个数据长度为偶数时，中位数时大顶堆和小顶堆根节点的求和平均；如果是奇数，则是小顶堆的根节点（先插入小顶堆）
"""
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def Insert(self, num):
        # 偶数进小顶堆，奇数进大顶堆
        if (len(self.max_heap)+len(self.min_heap)) % 2 == 0:
            if len(self.max_heap) > 0 and num < -self.max_heap[0]:
                # num比大顶堆的部分数字小，先入大顶堆，然后选最大的进小顶堆
                num = -heapq.heappushpop(self.max_heap,-num)
            heapq.heappush(self.min_heap,num)
        else:
            if len(self.min_heap) >0 and num > self.min_heap[0]:
                num = heapq.heappushpop(self.min_heap,num)
            heapq.heappush(self.max_heap,-num)
    def GetMedian(self,data):
        heap_size = len(self.max_heap) + len(self.min_heap)
        if heap_size == 0:
            return o
        median = 0
        if heap_size % 2 == 0:
            median = ((-self.max_heap[0]) + self.min_heap[0])/2.0
        else:
            median = self.min_heap[0]
        return median
