# -*- coding:utf-8 -*-

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归加缓存
        # memory = [0] * n
        # return self.climbStairsWithRecursionMemory(n, memory)

        # 递归内存优化
        # memory = [0] * n
        # return self.climbStairsWithRecursionMemory(n, memory)

        # 动态规划
        # return self.climbStairsWithDynamic(n)

        # 斐波那契
        # return self.climbStairsWithFibonacci(n)

        # 优化斐波那契
        # return self.climbStairsWithFibonacciOptimize(n):

        # 斐波那契公式
        return self.climbStairsWithFibonacciFormula(n)

    # 递归内存优化
    # def climbStairsWithRecursionMemory(self, n, memory):
    #     """
    #     :param n: int
    #     :param memory: List<int>
    #     :return: int
    #     """
    #     if n <= 2:
    #         return n
    #     if memory[n-1] > 0:
    #         return memory[n-1]
    #     memory[n-1] = self.climbStairsWithRecursionMemory(n-1, memory) + self.climbStairsWithRecursionMemory(n-2, memory)
    #     return memory[n-1]

    # 动态规划
    # def climbStairsWithDynamic(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 2:
    #         return n
    #
    #     dynamicArray = [0]*n
    #     dynamicArray[0] = 1
    #     dynamicArray[1] = 2
    #
    #     for i in range(2, n):
    #         dynamicArray[i] = dynamicArray[i-1] + dynamicArray[i-2]
    #
    #     return dynamicArray[n-1]

    # 斐波那契
    # def climbStairsWithFibonacci(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 2:
    #         return n
    #
    #     a = 1
    #     b = 2
    #     c = 0
    #     for i in range(2, n):
    #         c = a + b
    #         a, b = b, c
    #
    #     return c

    # 优化斐波那契
    # def climbStairsWithFibonacciOptimize(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 2:
    #         return n
    #
    #     a, b = 0, 1
    #     while n > 0:
    #         n -= 1
    #         b = a + b
    #         a = b - a
    #     return b

    # 斐波那契公式
    def climbStairsWithFibonacciFormula(self, n):
        sqrt5 = pow(5, 0.5)
        fibn = pow((1+sqrt5)/2, n+1) - pow((1-sqrt5)/2, n+1)
        return int(fibn / sqrt5)


if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(5)