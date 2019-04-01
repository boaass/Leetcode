# -*- coding: utf-8 -*-

# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of
# the matrix.

# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# Note:
#
# 1. 1 <= A.length <= 1000
# 2. 1 <= A[0].length <= 1000


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        B = []
        for col in xrange(len(A[0])):
            b_row_vals = []
            for row in xrange(len(A)):
                b_row_vals.append(A[row][col])
            B.append(b_row_vals)

        return B



if __name__ == '__main__':
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    solution = Solution()
    r = solution.transpose(A)

    print r