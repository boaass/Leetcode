# -*- coding:utf-8 -*-

# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
#   Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        # def dfs(s, index, res):
        #     if index == len(s):
        #         res.append(''.join(s))
        #         return
        #     # 不改变大小写的情况
        #     dfs(s, index + 1, res)
        #     # 改变大小写的情况
        #     if s[index].isalpha():
        #         s[index] = chr(ord(s[index]) ^ (1 << 5))
        #         dfs(s, index + 1, res)
        #
        # res = []
        # # 因为python不能改变string类型
        # s = list(S)
        # dfs(s, 0, res)
        # return res

        cur_s = [S]
        for i in range(len(S)):
            next_s = []
            for s in cur_s:
                if s[i].isdigit():
                    next_s.append(s)
                else:
                    next_s.append(s[0:i] + s[i].lower() + s[i + 1:])
                    next_s.append(s[0:i] + s[i].upper() + s[i + 1:])
            cur_s = next_s

        return cur_s


if __name__ == '__main__':
    S = "a1b2"
    solution = Solution()
    r = solution.letterCasePermutation(S)

    print r