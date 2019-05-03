'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。说明:初始化 nums1 和 nums2 的元素数量分别为 m 和 n。你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
  输入:
  nums1 = [1,2,3,0,0,0], m = 3
  nums2 = [2,5,6],       n = 3
  输出: [1,2,2,3,5,6]
思路：这个题的一个主要的特点就是不用辅助空间，直接合并到num1里，如果可以使用辅助空间的话，直接挨个比较两个数组的值，往辅助空间里放就行。解法一：不使用辅助空间也是可以的，思路也是类似，从后往前，不是使用辅助空间的从前往后了，比较两个数组最后的数值大小，放到nums1的最后，随着m和n的变小，会将两个数组中的 一个比较完，如果nums1先遍历完，说明nums2剩下的数都比nums1小， 直接放到前面，如果nums2遍历完，说明nums1剩下的数也是小的，直接不用动就好了。总而言之，放到后面的数都是大的数，记住这个就ok。解法二：将nums2放到nums1中然后排序。
'''
#解法一：
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:#若nums1完了，nums2还没完
        nums1[:n]=nums2[:n]#把剩下nums2的数放到nums1最开始
