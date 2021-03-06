# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero. The given RPN expression is always valid. That means the
#  expression would always evaluate to a result and there won't be any divide by zero operation. Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        vals = []
        for c in tokens:
            if c == '+':
                vals.append(vals.pop() + vals.pop())
            elif c == '-':
                vals.append(vals.pop(-2) - vals.pop(-1))
            elif c == '*':
                vals.append(vals.pop() * vals.pop())
            elif c == '/':
                quotient, remainder = divmod(vals.pop(-2), vals.pop(-1))
                vals.append(quotient+1 if quotient < 0 and remainder != 0 else quotient)
            else:
                vals.append(int(c))

            # print vals

        return vals[0]


if __name__ == '__main__':
    tokens = ["4","-2","/","2","-3","-","-"]
    s = Solution()
    print s.evalRPN(tokens)