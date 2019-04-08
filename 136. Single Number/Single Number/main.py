# -*- coding:utf-8 -*-

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1
        # counter = collections.Counter(nums)
        # for k, v in counter.items():
        #     if v == 1:
        #         return k
        # return None

        # Approach 2
        a = 0
        for n in nums:
            a ^= n
        return a

        # Approach 3
        # hash_table = {}
        # for n in nums:
        #     try:
        #         hash_table.pop(n)
        #     except:
        #         hash_table[n] = 1
        #
        # return hash_table.popitem()[0]

        # Approach 4
        # return 2 * sum(set(nums)) - sum(nums)

        # Approach 5
        # r_list = []
        # for n in nums:
        #     if n in r_list:
        #         r_list.remove(n)
        #     else:
        #         r_list.append(n)
        #
        # return r_list[0]


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    solution = Solution()
    result = solution.singleNumber(nums)

    print result