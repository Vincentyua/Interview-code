'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成
	思路：解法1：快慢指针，两个指针，一开始快慢指针指向同一个位置；快慢指针如果指向的数字相同，则快指针向前移动，如果不同，则快慢指针都移动一步，在慢指针移动完后，将快指针的值赋给慢指针移动后的值。最后快指针走完以后，慢指针的坐标加一就是数组的长度，因为慢指针指向的是最后一个元素的index，数组的长度是最后一个index+1。需要解释一下，为什么不同的时候，需要快慢指针都移动，因为慢指针保证了慢指针之前的都是无重复的值，所以当又出现不同的值后，需要快慢指针都移动，但是先移动慢指针，然后将慢指针指向的值赋成此时还没有移动快指针的值，然后快指针再移动。快慢指针之间的元素都是重复的元素，慢指针指向的是当前最后一个不重复的元素，所以相等时，快指针继续走，不相等时，更新慢指针（慢指针后移，将快指针的值赋到此时慢指针指向的值）和快指针（后移）。解法二：使用一个index，比较当前和下一个是否相等，相等的话，使用del或者pop删除。 
'''
#解法一：
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        cur,pre = 0,0
        while (cur < n):
            if nums[cur] == nums[pre]:
                cur += 1
            else:
                pre += 1
                nums[pre] = nums[cur]
                cur += 1
        return pre + 1
		
#解法二：
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        i = 0
        while(i < n-1):
            if nums[i] ==nums[i+1]:
                del nums[i+1]
                n -= 1
            else:
                i += 1
        return n
