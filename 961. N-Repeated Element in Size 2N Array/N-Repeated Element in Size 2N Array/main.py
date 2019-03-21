# -*- coding: utf-8 -*-

# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.

# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5

# Note:
#
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even


import collections

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # a = [0] * 100000
        # for n in A:
        #     if a[n] is 0:
        #         a[n] = 1
        #     else:
        #         return n

        count = collections.Counter(A)
        for c in count:
            if count[c] > 1:
                return c

if __name__ == '__main__':
    A = [2, 6, 2, 1]
    solution = Solution()
    print "result: %d" % solution.repeatedNTimes(A)
