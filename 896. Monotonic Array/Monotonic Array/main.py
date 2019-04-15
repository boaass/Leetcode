# -*- coding:utf-8 -*-

# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i
# <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.

# Example 1:
#
# Input: [1,2,2,3]
# Output: true
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
# Example 3:
#
# Input: [1,3,2]
# Output: false
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
# Example 5:
#
# Input: [1,1,1]
# Output: true

# Note:
#
# 1. 1 <= A.length <= 50000
# 2. -100000 <= A[i] <= 100000


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        increase = decrease = True
        for i in range(len(A) - 1):
            if A[i + 1] > A[i]:
                decrease = False
            elif A[i + 1] < A[i]:
                increase = False

        return decrease or increase

        # if len(A) <= 2:
        #     return True
        #
        # isMonotonic = None
        # for i in range(len(A)-1):
        #     if A[i+1] != A[i] and isMonotonic is None:
        #         isMonotonic = A[i+1] > A[i]
        #     elif A[i+1] == A[i]:
        #         continue
        #     elif (A[i+1] > A[i]) != isMonotonic:
        #         return False
        #
        # return True


if __name__ == '__main__':
    A = [2,2,2,1,4,5]
    solution = Solution()
    r = solution.isMonotonic(A)
    print r