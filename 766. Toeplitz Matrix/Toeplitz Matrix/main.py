# -*- coding:utf-8 -*-

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# Example 1:
#
# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:
#
# Input:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
# Note:
#
# 1. matrix will be a 2D array of integers.
# 2. matrix will have a number of rows and columns in range [1, 20].
# 3. matrix[i][j] will be integers in range [0, 99].

# Follow up:
#
# 1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of
# the matrix into the memory at once? 2. What if the matrix is so large that you can only load up a partial row into
# the memory at once?


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        # max_row = len(matrix)
        # max_col = len(matrix[0])
        #
        # for row in range(max_row):
        #     temp_row = row
        #     temp_col = 0
        #     val = matrix[temp_row][temp_col]
        #     while temp_row < max_row and temp_col < max_col:
        #         print matrix[temp_row][temp_col]
        #         if val is not matrix[temp_row][temp_col]:
        #             return False
        #         temp_row += 1
        #         temp_col += 1
        #
        # for col in range(1, max_col):
        #     temp_row = 0
        #     temp_col = col
        #     val = matrix[temp_row][temp_col]
        #     while temp_row < max_row and temp_col < max_col:
        #         if val is not matrix[temp_row][temp_col]:
        #             return False
        #         temp_row += 1
        #         temp_col += 1
        #
        # return True

        vals = {}
        for row, r_val in enumerate(matrix):
            for col, c_val in enumerate(r_val):
                if (row-col) not in vals:
                    vals[row-col] = c_val
                elif vals[row-col] != c_val:
                    return False
        return True


if __name__ == '__main__':
    matrix = [
      [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]
    ]
    solution = Solution()
    isToeplitz = solution.isToeplitzMatrix(matrix)

    print 'isToeplitz --- %d' % isToeplitz