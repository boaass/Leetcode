# coding=utf-8


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120 Output: 21 Note: Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
#  when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        new_x, x = 0, abs(x)
        while x:
            new_x = 10 * new_x + x % 10
            x /= 10
        new_x = flag * new_x
        return new_x if 2147483648 > new_x >= -2147483648 else 0


if __name__ == '__main__':
    x = -123
    s = Solution()
    print s.reverse(x)