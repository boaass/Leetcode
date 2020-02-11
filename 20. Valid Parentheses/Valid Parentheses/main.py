# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        typeMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in typeMap.keys():
                top_val = stack.pop() if stack else '#'
                if top_val != typeMap[c]:
                    return False
            else:
                stack.append(c)

        return not stack


if __name__ == '__main__':
    c = ""
    s = Solution()
    print s.isValid(c)