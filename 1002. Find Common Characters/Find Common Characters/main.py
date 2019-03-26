# -*- coding: utf-8 -*-

# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all
# strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not
# 4 times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.


# Example 1:
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]

# Note:
#
# 1. 1 <= A.length <= 100
# 2. 1 <= A[i].length <= 100
# 3. A[i][j] is a lowercase letter

import collections

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        # arr = []
        # for str in A:
        #     a = [0]*26
        #     for s in str:
        #         a[ord(s)-ord('a')] += 1
        #     arr.append(a)
        #
        # result = []
        # for s in list(set(A[0])):
        #     min_num = arr[0][ord(s)-ord('a')]
        #     for index in xrange(1, len(arr)):
        #         if arr[index][ord(s)-ord('a')] == 0:
        #             min_num = 0
        #             break
        #         min_num = min_num if min_num < arr[index][ord(s)-ord('a')] else arr[index][ord(s)-ord('a')]
        #
        #     if min_num > 0:
        #         for i in xrange(min_num):
        #             result.append(s)
        #
        # return result

        c = collections.Counter(A[0])
        for i in xrange(1, len(A)):
            c &= collections.Counter(A[i])

        return list(c.elements())


if __name__ == '__main__':
    A = ["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"]
    solution = Solution()
    result = solution.commonChars(A)

    print 'result --- %s' % result