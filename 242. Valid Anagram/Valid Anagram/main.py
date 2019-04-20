# -*- coding:utf-8 -*-

# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        A = {}
        for c in s:
            if c in A.keys():
                A[c] += 1
            else:
                A.setdefault(c, 1)

        for c in t:
            if c not in A.keys():
                return False
            A[c] -= 1
            if A[c] == 0:
                A.pop(c)

        return False if len(A) > 0 else True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    r = solution.isAnagram(s, t)
    print r