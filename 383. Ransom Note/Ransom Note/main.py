# -*- coding:utf-8 -*-

# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ; otherwise,
# it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        v_dict = {}
        for c in magazine:
            if c not in v_dict.keys():
                v_dict[c] = 1
            else:
                v_dict[c] += 1

        for c in ransomNote:
            if c not in v_dict.keys():
                return False
            if v_dict[c] <= 0:
                return False
            v_dict[c] -= 1

        return True


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    r = solution.canConstruct(ransomNote, magazine)
    print r