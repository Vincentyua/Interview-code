"""
题目：输入两个链表，找出它们的第一个公共结点。
解题思路：这个题最重要的就是理解两个具有公共节点单链表的特性。当两个单链表具有公共节点时，意味着公共节点之后的next指针也一样，即公共节点之后的所有节点都一样，可以用倒推的思路从两个链表的后往前找，但是单链表必须要遍历才可以找到尾结点。换个思路，先让长的链表多走几步，然后两个链表一起走，直至走到相同节点。先走那几步就是长链表的长度减去短链表。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)
        if length1 < length2:
            longhead = pHead2
            shorthead = pHead1
        else:
            longhead = pHead1
            shorthead = pHead2
        diff_len = abs(length1 - length2)
        for i in range(diff_len):
            longhead = longhead.next
        while shorthead and longhead and shorthead != longhead:
            shorthead = shorthead.next
            longhead = longhead.next
        return longhead

    def GetLength(self,pHead):
        length = 0
        while pHead:
            length += 1
            pHead = pHead.next
        return length
