"""
题目：输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
解题思路：二叉树，先考虑递归解决，同样可以拆分分成左右子树递归去做，找出左子树中满足值减去根节点值得所有路径，右子树也是同样，这样将根节点和左右子树所有满足条件的序列组合，就是最终的所有路径。所有路径都放在list中，所以递归的底层是判断是否满足是叶节点并且值和传递进来的相等。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        # 按递归的方法，主要讲递归最底层的判断条件写清楚就好了
        if not root :
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        result = []
        # 递归的判断左右子树
        re_left = self.FindPath(root.left,expectNumber-root.val)
        re_right = self.FindPath(root.right,expectNumber-root.val)
        # 将左右子树中的所有路径与根节点合并为最终路径
        for i in re_left + re_right:
            result.append([root.val]+i)
        return result
