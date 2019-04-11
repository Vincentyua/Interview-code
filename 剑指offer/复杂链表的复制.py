"""
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
解题思路:三段式解法，第一步现将链表每个节点在原链表中复制一个节点，这样链表就变成了原来的二倍，但是扩充的节点只有next指针，随机指针为空；第二步，将链表中原来节点的随机指针进行复制，新链表节点的随机指针等于原链表节点随机指向节点的next指针。第三步，链表拆分成两个链表，使用两个指针交替改变节点指向，最后得到拆分链表。复制next指针和随机指针的结构很类似，拆分链表时注意两个指针交替进行即可
"""
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.CloneNode(pHead)
        self.ConnectRandomNode(pHead)
        return self.ReconnctNode(pHead)
    def CloneNode(self,pHead):
    # 将链表进行复制
        pNode = pHead
        while (pNode):
            pCloneNode = RandomListNode(pNode.label)
            pCloneNode.next = pNode.next
            pNode.next = pCloneNode
            pNode = pCloneNode.next
    def ConnectRandomNode(self,pHead):
      # 复制节点随机指针
        pNode = pHead
        while (pNode):
            pClone = pNode.next
            if pNode.random :
                pClone.random = pNode.random.next
            pNode = pClone.next
    def ReconnctNode(self,pHead):
    # 拆分链表
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while (pNode):
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead
