"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：最简单的思路肯定是遍历一遍O(n)，但是没有利用旋转数组的特点，旋转数组的特点就是后面一部分元素比前面一部分元素小，一定程度上是排序的。利用二分查找的思路，三个指针，一个指针指向第一个元素，一个指向最后一个，一个指向中间元素，如果中间元素比第一个元素小，说明中间这个指针位于比较小后半部分，那最小的元素位于中间元素的前面，可以让指向最后元素的指针更新为指向中间这个元素，如果中间元素比最后一个元素大，说明中间这个指针位于比较大的前半部分，最小的元素位于后半部分，所以更新指向第一个元素的的指针指向中间的这个元素。因此第一个指针总是指向前面比较大的部分元素，最后一个指针总是指向后面比较小的部分元素。最终找到最小的元素是第一个指针和最后一个指针相邻。（注意：如果出现第一个元素和最后一个元素想相等的局面，就必须查询了，例如 1 1 1 0 1 1）
"""
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return
        if len(rotateArray)==0:
            return 0
        index1=0
        index2=len(rotateArray)-1
        indexMid=index1
        while (rotateArray[index1]>=rotateArray[index2]):
            if (index2-index1)==1:
                indexMid=index2
                break
            indexMid = (index1+index2)//2
            # 如果index1 index2 indexMid三者相等
            if rotateArray[index1]==rotateArray[index2] and rotateArray[indexMid]==rotateArray[index1]:
                return self.minValue(rotateArray,index1,index2)

            if rotateArray[indexMid]>=rotateArray[index1]:
                index1=indexMid
            if rotateArray[indexMid]<=rotateArray[index2]:
                index2=indexMid

        return rotateArray[indexMid]

    def minValue(self,rotateArray,index1,index2):
        res=rotateArray[index1]
        for i in range(index1+1,index2):
            if res>rotateArray[i]:
                res=rotateArray[i]
        return res
