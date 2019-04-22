# -*- coding:utf-8 -*-

# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0
# to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
# newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
#  the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the
# newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
#
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # if image[sr][sc] == newColor:
        #     return image
        #
        # oldcolor = image[sr][sc]
        # image[sr][sc] = newColor
        # if sr - 1 >= 0 and image[sr - 1][sc] == oldcolor:
        #     self.floodFill(image, sr - 1, sc, newColor)
        # if sr + 1 < len(image) and image[sr + 1][sc] == oldcolor:
        #     self.floodFill(image, sr + 1, sc, newColor)
        # if sc - 1 >= 0 and image[sr][sc - 1] == oldcolor:
        #     self.floodFill(image, sr, sc - 1, newColor)
        # if sc + 1 < len(image[0]) and image[sr][sc + 1] == oldcolor:
        #     self.floodFill(image, sr, sc + 1, newColor)
        #
        # return image

        queue = [(sr, sc)]
        oldcolor = image[sr][sc]
        while len(queue) > 0:
            t_sr, t_sc = queue.pop(0)
            image[t_sr][t_sc] = newColor

            if t_sr - 1 >= 0 and image[t_sr - 1][t_sc] == oldcolor and image[t_sr - 1][t_sc] != newColor:
                queue.append((t_sr - 1, t_sc))
            if t_sr + 1 < len(image) and image[t_sr + 1][t_sc] == oldcolor and image[t_sr + 1][t_sc] != newColor:
                queue.append((t_sr + 1, t_sc))
            if t_sc - 1 >= 0 and image[t_sr][t_sc - 1] == oldcolor and image[t_sr][t_sc - 1] != newColor:
                queue.append((t_sr, t_sc - 1))
            if t_sc + 1 < len(image[0]) and image[t_sr][t_sc + 1] == oldcolor and image[t_sr][t_sc + 1] != newColor:
                queue.append((t_sr, t_sc + 1))

        return image


if __name__ == '__main__':
    image = [[0, 0, 0],
             [0, 0, 1]]
    sr = 1
    sc = 0
    newColor = 2
    solution = Solution()
    r = solution.floodFill(image, sr, sc, newColor)
    print r
