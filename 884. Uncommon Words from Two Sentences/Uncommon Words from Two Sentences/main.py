# -*- coding:utf-8 -*-

# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of
# lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.


# Example 1:
#
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
#
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]


import collections


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        C = {}
        for i, word in enumerate(A.split(" ") + B.split(" ")):
            if C.has_key(word):
                C.update({word: 1})
            else:
                C.update({word: 0})

        return [word for word in C if C[word] == 0]


if __name__ == '__main__':
    A = "s z z z s"
    B = "s z ejt"
    solution = Solution()
    uncommon_words = solution.uncommonFromSentences(A, B)

    print uncommon_words
