# -*- coding: utf-8 -*-

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        str_x = bin(x).replace('0b', '')
        str_y = bin(y).replace('0b', '')

        num_x = len(str_x)
        num_y = len(str_y)

        if num_x > num_y:
            temp = ""
            for i in range(num_x-num_y):
                temp = temp + "0"
            str_y = temp + str_y
        else:
            temp = ""
            for i in range(num_y-num_x):
                temp = temp + "0"
            str_x = temp + str_x

        num = 0
        for index in range(len(str_x)):
            if (int(str_x[index]) ^ int(str_y[index])) == 1:
                num += 1

        return num

if __name__ == '__main__':
    x = 1
    y = 4
    solution = Solution()
    result = solution.hammingDistance(x, y)

    print result