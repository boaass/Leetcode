# -*- coding:utf-8 -*-

# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is
# different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to
# each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become
# invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def isInvalidNums(n):
            invalid_nums = [2, 5, 6, 9]
            option_nums = [1, 0, 8]
            isOnlyHasOption = True
            for s in str(n):
                if int(s) not in invalid_nums and int(s) not in option_nums:
                    return False
                elif int(s) in invalid_nums:
                    isOnlyHasOption = False

            if isOnlyHasOption:
                return False

            return True

        # for n in range(1, N + 1):
        #     print '%d, %d' % (n, isInvalidNums(n))

        return len([n for n in range(1, N+1) if isInvalidNums(n)])


if __name__ == '__main__':
    N = 857
    solution = Solution()
    r = solution.rotatedDigits(N)

    print r
