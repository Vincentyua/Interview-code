"""
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
解题思路：根据上一个题的解决办法(二叉树的深度)，通过左右子树的差来判断，递归的判断子树是否是平衡二叉树
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left,right)+1
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        diff = abs(left-right)
        if diff > 1:
            return False
      return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
