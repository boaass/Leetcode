# -*- coding:utf-8 -*-

# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i, c in enumerate(reversed(s)):
            count += (ord(c)-ord('A')+1) * 26**i

        return count

if __name__ == '__main__':
    s = "ZY"
    solution = Solution()
    r = solution.titleToNumber(s)
    print r