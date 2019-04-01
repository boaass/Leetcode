# -*- coding: utf-8 -*-

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(self.reversedStr(word) for word in s.split(" "))


    def reversedStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_l = list(s)
        length = len(s)
        for index in range(len(s)/2):
            temp = str_l[index]
            str_l[index] = str_l[length-index-1]
            str_l[length-index-1] = temp

        return "".join(str_l)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution()
    resutl = solution.reverseWords(s)

    print resutl