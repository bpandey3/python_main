#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#

from typing import List


def twoSum(nums:List[int], target:int) -> List[int]:
        
        
        n = len(nums) -1
        for right in range(n):
            if nums[right] + nums[right + 1] == target:
                return[right,right+1]
        
        return []
        
print(twoSum([3,2,3,7],10))