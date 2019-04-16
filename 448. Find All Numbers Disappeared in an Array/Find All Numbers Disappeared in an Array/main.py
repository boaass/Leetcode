# -*- coding:utf-8 -*-

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra
# space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return list(set([i for i in range(1,len(nums)+1)]) - set(nums)) if len(nums) > 0 else []

        # A = [0] * len(nums)
        # for n in nums:
        #     A[n-1] = 1
        #
        # return [i+1 for i, a in enumerate(A) if a == 0]

        n = len(nums)
        for i in range(n):
            while nums[i] != i+1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp

        return [i+1 for i in range(n) if nums[i] != i+1]


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    r = solution.findDisappearedNumbers(nums)

    print r