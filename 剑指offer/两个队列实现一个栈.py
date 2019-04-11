"""
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
