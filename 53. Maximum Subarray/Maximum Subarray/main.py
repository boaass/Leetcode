# -*- coding:utf8 -*-

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane算法
        # return self.maxSubArrayWithKadane(nums)

        # DP
        return self.maxSubArrayWithDP(nums)

    # Kadane算法
    def maxSubArrayWithKadane(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndHere = nums[0]
        maxSoFar = nums[0]
        for n in nums[1:]:
            if maxEndHere < 0:
                maxEndHere = 0
            maxEndHere += n

            if maxSoFar < maxEndHere:
                maxSoFar = maxEndHere

        return maxSoFar

    # DP
    def maxSubArrayWithDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLocal = nums[0]
        maxGlobal = nums[0]
        for n in nums[1:]:
            maxLocal = max(n, maxLocal + n)
            maxGlobal = max(maxGlobal, maxLocal)

        return maxGlobal


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print s.maxSubArray(nums)
