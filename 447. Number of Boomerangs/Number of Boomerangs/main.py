# -*- coding:utf-8 -*-

# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that
# the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the
# range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


import collections

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # def sameDistanceCount(p1, p2, p3):
        #     """
        #     :param p1: points
        #     :param p2: points
        #     :param p3: points
        #     :return: int
        #     """
        #     count = 0
        #
        #     # p3, p2, p1
        #     if pow(p3[0]-p1[0], 2)+pow(p3[1]-p1[1], 2) == pow(p3[0]-p2[0], 2)+pow(p3[1]-p2[1], 2):
        #         count += 2
        #     # p1, p2, p3
        #     if pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2) == pow(p1[0]-p3[0], 2)+pow(p1[1]-p3[1], 2):
        #         count += 2
        #     # p2, p1, p3
        #     if pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2) == pow(p2[0]-p3[0], 2)+pow(p2[1]-p3[1], 2):
        #         count += 2
        #
        #     return count
        #
        # count = 0
        #
        # length = len(points)
        # for i in range(length - 2):
        #     for j in range(i+1, length - 1):
        #         for k in range(j+1, length):
        #             count += sameDistanceCount(points[i], points[j], points[k])
        #
        # return count

        count = 0
        for i, p1 in enumerate(points):
            d_dict = {}
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                k = self.distance(p1, p2)
                if k not in d_dict:
                    d_dict[k] = 1
                else:
                    d_dict[k] += 1

            for d in d_dict:
                if d_dict[d] > 1:
                    count += d_dict[d]*(d_dict[d]-1)

        return count

    def distance(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


if __name__ == '__main__':
    points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    solution = Solution()
    r = solution.numberOfBoomerangs(points)
    print r
