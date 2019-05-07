# -*- coding:utf-8 -*-

# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements
# equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # min_v = min(nums)
        # max_v = max(nums)
        # diff = max_v - min_v
        # isFirstMaxValue = True
        # if diff != 0:
        #     for i in range(len(nums)):
        #         if nums[i] == max_v and isFirstMaxValue:
        #             isFirstMaxValue = False
        #         else:
        #             nums[i] += diff
        #     return diff + self.minMoves(nums)
        #
        # return diff

        # s_nums = sorted(nums)
        # r = 0
        # while len(s_nums) > 1:
        #     r += s_nums.pop() - s_nums[0]
        #
        # return r

        # min_v = min(nums)
        # r = 0
        # for i in range(len(nums)):
        #     r += nums[i] - min_v
        # return r

        r = 0
        min_v = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= min_v:
                r += nums[i]-min_v
            else:
                r += i*(min_v-nums[i])
                min_v = nums[i]

        return r



if __name__ == '__main__':
    nums = [3,2,1]
    solution = Solution()
    r = solution.minMoves(nums)
    print r