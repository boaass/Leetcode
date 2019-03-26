# -*- coding:utf-8 -*-

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2,
# b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
# 
# Example 1:
# Input: [1,4,3,2]
# 
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

import collections

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # result = 0
        # sort_num = sorted(nums)
        # for index in xrange(0, len(nums), 2):
        #     result += sort_num[index]

        # return result

        result = 0
        self.mergeSorted(nums, 0, len(nums)-1)
        for index in xrange(0, len(nums), 2):
            result += nums[index]

        return result

    def mergeSorted(self, nums, left, right):

        if left > right:
            return

        temp = nums[left]
        i, j = left, right
        while i != j:
            while temp <= nums[j] and i < j:
                j -= 1
            while temp >= nums[i] and i < j:
                i += 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left] = nums[i]
        nums[i] = temp

        self.mergeSorted(nums, left, i-1)
        self.mergeSorted(nums, i+1, right)


if __name__ == '__main__':
    nums = [1,4,3,2]
    soluion = Solution()
    result = soluion.arrayPairSum(nums)

    print 'result --- %d' %result