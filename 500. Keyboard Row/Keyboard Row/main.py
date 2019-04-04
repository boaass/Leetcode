# -*- coding:utf-8 -*-

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American
# keyboard like the image below.

# Example:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Note:
#
# 1. You may use one character in the keyboard more than once.
# 2. You may assume the input string will only contain letters of alphabet.


class Solution(object):
    def __init__(self):
        self.A = [0]*26
        self.A[ord('q') - ord('a')] = 1
        self.A[ord('w') - ord('a')] = 1
        self.A[ord('e') - ord('a')] = 1
        self.A[ord('r') - ord('a')] = 1
        self.A[ord('t') - ord('a')] = 1
        self.A[ord('y') - ord('a')] = 1
        self.A[ord('u') - ord('a')] = 1
        self.A[ord('i') - ord('a')] = 1
        self.A[ord('o') - ord('a')] = 1
        self.A[ord('p') - ord('a')] = 1
        self.A[ord('a') - ord('a')] = 2
        self.A[ord('s') - ord('a')] = 2
        self.A[ord('d') - ord('a')] = 2
        self.A[ord('f') - ord('a')] = 2
        self.A[ord('g') - ord('a')] = 2
        self.A[ord('h') - ord('a')] = 2
        self.A[ord('j') - ord('a')] = 2
        self.A[ord('k') - ord('a')] = 2
        self.A[ord('l') - ord('a')] = 2
        self.A[ord('z') - ord('a')] = 3
        self.A[ord('x') - ord('a')] = 3
        self.A[ord('c') - ord('a')] = 3
        self.A[ord('v') - ord('a')] = 3
        self.A[ord('b') - ord('a')] = 3
        self.A[ord('n') - ord('a')] = 3
        self.A[ord('m') - ord('a')] = 3

        print self.A

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        r_list = []
        for word in words:
            isbreak = False
            last_val = 0
            for l in word:
                if ord(l) < ord('a'):
                    # 大写
                    if last_val == 0:
                        last_val = self.A[ord(l) - ord('A')]
                        continue
                    if last_val != self.A[ord(l) - ord('A')]:
                        isbreak = True
                        break
                else:
                    # 小写
                    if last_val == 0:
                        last_val = self.A[ord(l) - ord('a')]
                        continue
                    if last_val != self.A[ord(l) - ord('a')]:
                        isbreak = True
                        break

            if not isbreak:
                r_list.append(word)
        return r_list


if __name__ == '__main__':
    words = ["Hello","Alaska","Dad","Peace"]
    solution = Solution()
    r_list = solution.findWords(words)

    print r_list