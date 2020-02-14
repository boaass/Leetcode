# coding=utf-8
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        r = [True] * n  # 从1到n
        r[0] = r[1] = False
        for i in range(2, int(pow(n, 0.5))+1):
            for num in range(i*i, n, i):
                r[num] = False

        return sum(r)


if __name__ == '__main__':
    n = 10
    s = Solution()
    print s.countPrimes(n)