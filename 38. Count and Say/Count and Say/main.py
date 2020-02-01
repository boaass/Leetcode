# coding=utf-8
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so
# recursively, in other words from the previous member read off the digits, counting the number of digits in groups
# of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
#
# Input: 4 Output: "1211" Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1",
# "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is
# the concatenation of "12" and "11" which is "1211".


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 递归
        # return self.countAndSayWithRecursion(n)

        # 常规
        return self.countAndSayWithCirculation(n)

    def countAndSayWithCirculation(self, n):
        s = "1"
        for i in range(n-1):
            s = self.countAndSayWithLastSay(s)

        return s

    # 递归
    def countAndSayWithRecursion(self, n):
        if n <= 1:
            return "1"
        last_say = self.countAndSayWithRecursion(n - 1)
        return self.countAndSayWithLastSay(last_say)

    def countAndSayWithLastSay(self, lastSay):
        """
        :param lastSay: str
        :return: str
        """
        s = ""
        last_c = lastSay[0]
        count = 1
        for i in range(1, len(lastSay)):
            c = lastSay[i]
            if last_c is c:
                count += 1
            else:
                s += str(count) + last_c
                count = 1
                last_c = c

        if last_c == lastSay[-1]:
            s += str(count) + last_c
        return s


if __name__ == '__main__':
    s = Solution()
    r = s.countAndSay(4)
    print r
