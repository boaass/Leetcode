# coding:utf-8 -*-

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
#  of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as
# nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        v_dict = {}
        for i, n in enumerate(nums):
            try:
                v_dict[n].append(i)
            except:
                v_dict.setdefault(n, [i])

        shortest = 50000
        max_v = 0
        for k, v in v_dict.items():
            if len(v) > max_v:
                max_v = len(v)
                shortest = v[-1]-v[0]+1
            elif len(v) == max_v:
                shortest = min(shortest, v[-1]-v[0]+1)

        return shortest


if __name__ == '__main__':
    nums = [1,2,2,3,1,4,2]
    solution = Solution()
    r = solution.findShortestSubArray(nums)
    print r