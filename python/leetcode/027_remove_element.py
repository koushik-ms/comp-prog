from typing import List

def log(*s):
    pass

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)
        # nums[right] and later elements are all "val"
        # nums[right-1] and later are not val
        while left < (right-1):
            log(left, right, nums)
            # when nums[right-1] is not val,
            if nums[right-1] == val:
                right -= 1
                continue
            # increment left until left ==right or nums[left] == val
            while left < (right-1) and nums[left] != val:
                left += 1
            log(" >> : ", left, right, nums)
            # swap nums[left] with nums[right-1]
            if left < (right-1):
                temp = nums[left]
                nums[left] = nums[right-1]
                nums[right-1] = temp
                # dec right and continue
                right -= 1
            log(" >> : ", left, right, nums)
        # if left == (right-1) break loop
        return right -1 if (right and nums[right-1] == val) else right
