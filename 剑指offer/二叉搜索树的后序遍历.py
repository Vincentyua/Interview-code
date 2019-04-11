"""
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
解题思路：遇到二叉树，首先应该想的是递归来解决，因为它的结构太对称了。二叉搜索树，左子树的节点值都小于根节点值，根节点值都小于右子树的节点值。后序遍历的过程是左子树，右子树，根节点。二叉搜索树的后序遍历得到的序列就满足这几个特性。第一，最后一个值是根节点的值，其次，从序列的第一个值开始，遇到的第一个大于根节点值之前的值都是左子树的，剩下的到根节点之前都是右子树的。这样就把整个二叉树的框架搭建起来了，分清了左子树、右子树，根节点。在每个子树里采取同样的操作递归执行，就可以将左右子树构建为二叉树。递归中，主要的区别就是底层的判断设计，这里是判断是否是后序遍历，则在最底层时，只剩一个节点，直接返回真。
"""
# -*- coding:utf-8 -*-
class Solution:
  def VerifySquenceOfBST(self, sequence):
      # write code here
      if not sequence:
          return False
      if len(sequence) == 1:
          return True
      i = 0
      # 寻找比根节点大的第一个值
      while (sequence[i] < sequence[len(sequence)-1]):
          i += 1
      r_1 = sequence[i]
      j = i
      # 判断左子树所有节点是否比根节点小
      while (j < len(sequence)-1):
          if sequence[j] < sequence[-1]:
              return False
          else:
              j += 1
      # 设置标志来记录左右子树是否是后序遍历
      left = True
      right = True
      # 递归的判断左右子树
      if len(sequence[0:i]) > 0:
          left = self.VerifySquenceOfBST(sequence[0:i])
      if len(sequence[i:len(sequence)-1]) > 0:
          right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
      return left and right
