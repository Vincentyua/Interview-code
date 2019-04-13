"""
题目：统计一个数字在排序数组中出现的次数。、
解题思路：解法1：使用二分查找先找个这个数字，然后向前和向后遍历找到第一个和最后一个，得到他们之间的个数。时间复杂度O(n)，解法2：使用二分查找分别找到这个数字第一次和最后一次出现位置，次数是位置差+1。时间复杂度O(logn)
"""
#解法1：
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        start = 0
        end = len(data) -1
        while(start <= end):
            mid = (start + end)/2
            if data[mid] ==k:
                count = 0
                tmp = mid
                while tmp >= 0 and data[tmp] == k:
                    tmp -= 1
                    count += 1
                tmp = mid+1
                while tmp < len(data) and data[tmp] ==k:
                    tmp += 1
                    count += 1
                return count
            elif data[mid] < k:
                start = mid + 1
            else:
                end = mid -1
        return 0
#解法2：
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        if data !=None and len(data)>0:
            length=len(data)
            first = self.GetFirst(data,length,k,0,length-1)
            last = self.GetLast(data,length,k,0,length-1)
            if first > -1 and last > -1:
                number=last-first+1
        return number


    def GetFirst(self,data,lenth,k,start,end):
        if start>end:
            return -1
        middle = (start+end)//2
        if data[middle]==k:
            if middle>0 and data[middle-1]==k:
                end = middle -1
            else:
                return middle
        elif data[middle]>k:
            end=middle-1
        else:
            start=middle+1
        return self.GetFirst(data,lenth,k,start,end)


    def GetLast(self, data, lenth, k, start, end):
        if start>end:
            return -1
        middle=(start+end)//2
        if data[middle]==k:
            if middle<end and data[middle+1]==k:
                start = middle+1
            else:
                return middle
        elif data[middle]>k:
            end=middle-1
        else:
            start=middle+1
      return self.GetLast(data, lenth, k, start, end)
