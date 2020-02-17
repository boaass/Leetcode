# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
# value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # normal method
        # return self.firstMethod(nums, target)

    def firstMethod(self, nums, target):
        rList = []
        flag = False
        for i in range(len(nums)):
            if nums[i] > target:
                if len(rList) == 1:
                    rList.append(i - 1)
                    return rList
                else:
                    return [-1, -1]

            if nums[i] == target:
                if len(rList) == 0:
                    rList.append(i)
                    flag = True
            else:
                if flag:
                    rList.append(i)
                    return rList

        if len(rList) == 1:
            rList.append(len(nums) - 1)
            return rList
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = [1]
    target = 1
    s = Solution()
    print s.searchRange(nums, target)