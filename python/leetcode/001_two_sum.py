from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ti = {}
        for x in range(len(nums)):
            first_value = nums[x]
            complement = target - first_value
            if complement in ti:
                return [ti[complement], x]
            ti[first_value] = x
        return []
