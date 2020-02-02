# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true
# Example 2:
#
# Input: 0
# Output: false
# Example 3:
#
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

import math
import re


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        r_int = round(math.log(n, 10) / math.log(3, 10))
        return pow(3, r_int) == n


if __name__ == '__main__':
    s = Solution()
    r = s.isPowerOfThree(27)
    print r