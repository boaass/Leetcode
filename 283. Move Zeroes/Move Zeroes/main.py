# -*- coding:utf-8 -*-

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        slow = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[slow], nums[cur] = nums[cur], nums[slow]
                slow += 1



if __name__ == '__main__':
    nums = [0, 1, 0]
    solution = Solution()
    solution.moveZeroes(nums)
    print nums