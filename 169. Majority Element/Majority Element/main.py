# -*- coding:utf-8 -*-

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊
# n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        max_t = (0, 0)
        for i, a in enumerate(nums):
            if a in dic.keys():
                dic[a] += 1
            else:
                dic.setdefault(a, 1)

            if max_t[1] < dic[a]:
                max_t = (a, dic[a])

        return max_t[0]


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    r = solution.majorityElement(nums)

    print r