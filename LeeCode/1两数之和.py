'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
	示例:
	给定 nums = [2, 7, 11, 15], target = 9，因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]
'''
#解法1：将nums排序后，用首尾之和和target的目标值比较，首尾递进的进行查找，复杂度O（nlogn）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_id = sorted(range(len(nums)),key = lambda k:nums[k])
        start = 0
        end = len(nums) - 1
        sum_result = nums[sorted_id[start]] + nums[sorted_id[end]]
        while sum_result != target:
            if sum_result < target:
                start += 1
            elif sum_result > target:
                end -+ 1
            sum_result = nums[sorted_id[start]] + nums[sorted_id[end]]
    return [sorted_id[start],sorted_id[end]]
#解法2：使用字典的解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index,num in enumerate(nums):
            other_num = target - num
            if other_num in num_dict:
                return [num_dict[other_num],index]
            num_dict[num] = index
    return None
