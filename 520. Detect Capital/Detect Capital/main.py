# -*- coding:utf-8 -*-

# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# Example 1:
# Input: "USA"
# Output: True
# Example 2:
# Input: "FlaG"
# Output: False
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        last_case_flag = ord('A') <= ord(word[0]) <= ord('Z')
        for w in word:
            if last_case_flag != (ord('A') <= ord(w) <= ord('Z')):
                if w != word[1] or last_case_flag == False:
                    return False
            last_case_flag = (ord('A') <= ord(w) <= ord('Z'))
        return True


if __name__ == '__main__':
    word = "Usa"
    solution = Solution()
    r = solution.detectCapitalUse(word)
    print r
