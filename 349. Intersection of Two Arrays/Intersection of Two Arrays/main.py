# -*- coding:utf-8 -*-

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        t_num1 = set(nums1)
        t_num2 = set(nums2)

        dict = {}
        for n in t_num1:
            dict[n] = 1

        return [n for n in t_num2 if n in dict]


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2, 3]
    solution = Solution()
    r = solution.intersection(nums1, nums2)

    print r