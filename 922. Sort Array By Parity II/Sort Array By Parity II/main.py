# -*- coding: utf-8 -*-

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.

# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Note:
#
# 1. 2 <= A.length <= 20000
# 2. A.length % 2 == 0
# 3. 0 <= A[i] <= 1000


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        B = [0] * len(A)

        # i = 0
        # j = 1
        # for a in A:
        #     if a%2 == 0:
        #         B[i] = a
        #         i += 2
        #     else:
        #         B[j] = a
        #         j += 2
        #
        # return B

        B[0::2] = (a for a in A if a % 2 == 0)
        B[1::2] = (a for a in A if a % 2 == 1)

        return B


if __name__ == '__main__':
    A = [4,2,5,7]
    solution = Solution()
    r_list = solution.sortArrayByParityII(A)

    print r_list