"""
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：有两个栈stackA,stackB，A为入栈，B为出栈的。入栈时，直接进入A即可，出栈时，先判断B中是否有元素，如果没有肯定不能pop()，应将A中所有元素倒压在B里面，再pop()最上面（后面）的元素，如果有，直接pop()就可以了。两个栈各自先进后出，在一起又实现了队列的新进先出。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
"""
扩展：两个队列实现一个栈
思路：和两个栈实现一个队列一样，一个队列作为中转。队列A（入栈）队列B（出栈），入栈时，元素入队列A，当要出栈时，将队列A除最后一个元素其他的都入队列B，交换AB队列，并把队列B（交换前仅剩一个元素的队列A）出栈。
"""
class Solution:
    def __init__(self):
        self.queueA=[]
        self.queueB=[]

    def push(self,node):
        self.queueA.insert(0,node)
    def pop(self):
        if not self.queueA:
            return None
        while len(self.queueA)!=1:
            self.queueB.insert(0,self.queueA.pop())
        self.queueA,self.queueB=self.queueB,self.queueA
        return self.queueB.pop()
