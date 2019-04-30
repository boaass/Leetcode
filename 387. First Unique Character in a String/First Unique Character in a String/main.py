# -*- coding:utf-8 -*-

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        v_dict = {}
        for c in s:
            try:
                v_dict[c] = v_dict[c]+1
            except:
                v_dict.setdefault(c, 1)

        print v_dict

        for i, c in enumerate(s):
            if v_dict[c] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    solution = Solution()
    r = solution.firstUniqChar(s)
    print r