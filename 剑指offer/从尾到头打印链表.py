"""
题目：输入一个链表，从尾到头打印链表每个节点的值。
思路：思路一：从头到尾遍历链表，append到list中，最后反转。思路二：遍历链表，使用insert插入到list的第一个位置，遍历完成就是从尾到头的
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        res = []
        head = listNode
        while head:
            res.insert(0,head.val)
            head = head.next
        return res
