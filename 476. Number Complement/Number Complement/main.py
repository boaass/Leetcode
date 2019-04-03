# -*- coding:utf-8 -*-

# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary
# representation.
#
# Note: 1. The given integer is guaranteed to fit within the range of a 32-bit signed integer. 2. You could assume no
# leading zero bit in the integer’s binary representation. Example 1: Input: 5 Output: 2 Explanation: The binary
# representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2. Example 2:
# Input: 1 Output: 0 Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is
# 0. So you need to output 0.


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.complement(num)

    def complement(self, num):
        # b_str = bin(num)[2:]
        # mask = '1'*len(b_str)
        mask = '1'*self.maxBitLength(num)

        return num ^ int(mask, 2)

    def maxBitLength(self, num):

        leng = 1
        while num >= 2:
            num = num/2
            leng += 1

        return leng


if __name__ == '__main__':

    num = 8

    solution = Solution()
    result = solution.findComplement(num)

    print 'result --- %d' % result