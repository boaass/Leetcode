# -*- coding:utf-8 -*-

# Given a string S and a character C, return an array of integers representing the shortest distance from the
# character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# Note:
#
# 1. S string length is in [1, 10000].
# 2. C is a single character, and guaranteed to be in string S.
# 3. All letters in S and C are lowercase.


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # r_list = []
        # c_index_list = []
        #
        # for index, c in enumerate(S):
        #     if c is C:
        #         c_index_list.append(index)
        #
        # for i in range(len(S)):
        #     r_list.append(min(list(abs(c_index_list[j]-i) for j in range(len(c_index_list)))))

        prev = float('-inf')
        r_list = []

        for index, s in enumerate(S):
            if s == C:
                prev = index
            r_list.append(index-prev)

        prev = float('inf')
        for index in xrange(len(S)-1, -1, -1):
            if S[index] == C:
                prev = index
            r_list[index] = min(r_list[index], prev-index)

        return r_list


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    solution = Solution()
    r_list = solution.shortestToChar(S, C)

    print r_list
