"""
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
解题思路：二叉树，先考虑递归去解决。将二叉搜索树转变成双向链表只要将二叉搜索树的节点指针变成中序遍历的序列指向即可。还是先在左子树，根节点，右子树上考虑。中序的序列中，根节点前面的节点是左子树中最大的，根节点后面的节点是右子树中最小的节点。掌握了这个特性，可以先将左子树递归，然后取出左子树列表的最大的，也是最右端的节点，修改指针。右子树类似操作。最后将整个双向列表的头结点返回（最左边的节点）
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # 采用递归的方法，去解决左右子树
        # 根节点和左子树最大的节点相连，和右子树最小的节点相连
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 递归处理左子树,con_left是转化成链表后的左子树部分
        self.Convert(pRootOfTree.left)
        conv_left = pRootOfTree.left
        # 寻找左子树最大的节点与根节点相连
        if conv_left:
            while(conv_left.right):
                conv_left = conv_left.right
            conv_left.right,pRootOfTree.left = pRootOfTree,conv_left
        # 递归处理右子树
        self.Convert(pRootOfTree.right)
        conv_right  = pRootOfTree.right
        if conv_right:
            while(conv_right.left):
                conv_right = conv_right.left
            conv_right.left,pRootOfTree.right = pRootOfTree,conv_right
        # 找到调整后的头结点
        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
