# -*- coding:utf-8 -*-

# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output
# “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        A = []
        for num in range(1, n+1):
            if num % (3*5) == 0:
                A.append('FizzBuzz')
            elif num % 3 == 0:
                A.append('Fizz')
            elif num % 5 == 0:
                A.append('Buzz')
            else:
                A.append(str(num))
        return A


if __name__ == '__main__':
    n = 15
    solution = Solution()
    r_list = solution.fizzBuzz(n)

    print r_list