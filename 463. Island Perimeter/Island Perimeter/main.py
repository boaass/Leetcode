# - coding:utf-8 -*-

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a
# square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.

# Example:
#
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        coincide_count = 0
        island_count = 0
        for i in range(len(grid)):
            for j, val in enumerate(grid[i]):
                if val == 1:
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        coincide_count += 1
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        coincide_count += 1

                    island_count += 1

        return island_count * 4 - coincide_count * 2

if __name__ == '__main__':
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    solution = Solution()
    perimeter = solution.islandPerimeter(grid)

    print 'perimeter --- %d' % perimeter