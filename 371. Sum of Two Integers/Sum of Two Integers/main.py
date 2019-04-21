# -*- coding:utf-8 -*-

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        # 符号位为0的最大值
        Mask = 0xFFFFFFFF
        # 符号位为1的最大值
        
        while b != 0:
            suma = (a ^ b) & Mask
            carry = ((a & b) << 1) & Mask
            a = suma
            b = carry

        return a if a <= MAX else ~(a ^ Mask)

if __name__ == '__main__':
    a = 1
    b = 2
    solution = Solution()
    r = solution.getSum(a, b)
    print r