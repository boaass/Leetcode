# -*- coding:utf-8 -*-

# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the
# points.
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.

# Notes:
#
# 3 <= points.length <= 50.
# No points will be duplicated.
#  -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.


import math

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def calculateArea(p1, p2, p3):
            """
            :type p1: tuple
            :type p2: tuple
            :type p3: tuple
            :return: int
            """

            p1p2 = math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
            p2p3 = math.sqrt(pow(p3[0] - p2[0], 2) + pow(p3[1] - p2[1], 2))
            p1p3 = math.sqrt(pow(p3[0] - p1[0], 2) + pow(p3[1] - p1[1], 2))

            if p1p2 + p2p3 <= p1p3:
                return 0

            s = (p1p2 + p2p3 + p1p3) / 2
            print s*(s-p1p2)*(s-p2p3)*(s-p1p3)
            return abs(s*(s-p1p2)*(s-p2p3)*(s-p1p3)) ** 0.5

        length = len(points)
        max_area = 0
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    max_area = max(max_area, calculateArea(points[i], points[j], points[k]))

        return max_area


if __name__ == '__main__':
    points = [[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]
    solution = Solution()
    r = solution.largestTriangleArea(points)

    print r