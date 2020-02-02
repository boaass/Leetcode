# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the
# array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        addition = 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + addition
            if s == 10:
                digits[i] = 0
                addition = 1
            else:
                digits[i] = s
                addition = 0
                break
        if addition == 1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    r = s.plusOne([1,2,9])
    print r