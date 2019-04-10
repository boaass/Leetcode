# -*- coding:utf-8 -*-

# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.

# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

# Note:
#
# 1. S.length <= 100
# 2. 33 <= S[i].ASCIIcode <= 122
# 3. S doesn't contain \ or "


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S)-1

        s = list(S)  # s: list<str>

        while i <= j:
            if not (ord('A') <= ord(s[i]) <= ord('Z')) and not (ord('a') <= ord(s[i]) <= ord('z')):
                i += 1
                continue

            if not (ord('A') <= ord(s[j]) <= ord('Z')) and not (ord('a') <= ord(s[j]) <= ord('z')):
                j -= 1
                continue

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)


if __name__ == '__main__':
    S = "a-bC-dEf-ghIj"
    solution = Solution()
    r = solution.reverseOnlyLetters(S)

    print r