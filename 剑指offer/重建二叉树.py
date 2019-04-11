"""
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
思路：递归实现，根据前序找到节点，根据根节点在中序的index将中序分成左子树部分和右子树部分，并且也可以将前序分成左子树和右子树部分。递归调用本身
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root=TreeNode(pre[0])
        val=tin.index(pre[0])

        root.left=self.reConstructBinaryTree(pre[1:val+1],tin[:val])
        root.right=self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
        return root
