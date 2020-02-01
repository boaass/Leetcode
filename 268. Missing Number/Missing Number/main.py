# -*- codg:utf-8 -*-

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # full_nums = [n for n in range(len(nums)+1)]
        # for n in nums:
        #     full_nums.remove(n)
        #
        # return full_nums.pop()

        # full_nums = [0 for _ in range(len(nums)+1)]
        # for n in nums:
        #     full_nums[n] = 1
        #
        # for i in range(len(full_nums)):
        #     if full_nums[i] == 0:
        #         return i
        #
        # return 0

        return len(nums)*(len(nums)+1)//2 - sum(nums)


if __name__ == '__main__':
    nums = [3,0,1]
    solution = Solution()
    r = solution.missingNumber(nums)
    print r