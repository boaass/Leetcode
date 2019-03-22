# -*- coding: utf-8 -*-


# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
# also in sorted non-decreasing order.

# Example
# 1:
#
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
# Example
# 2:
#
# Input: [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non - decreasing order.


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        arr = []
        for a in A:
            arr.append(a*a)
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         if arr[i] > arr[j]:
        #             temp = arr[j]
        #             arr[j] = arr[i]
        #             arr[i] = temp

        # for i in range(len(arr)):
        #     for j in range(1, len(arr)-i):
        #         if arr[j] < arr[j-1]:
        #             temp = arr[j-1]
        #             arr[j-1] = arr[j]
        #             arr[j] = temp

        self.quickSort(arr, 0, len(A)-1)
        return arr

    def quickSort(self, A, left, right):

        if left > right:
            return

        i, j = left, right
        temp = A[left]

        while i != j:
            while A[j] >= temp and i < j:
                j -= 1
            while A[i] <= temp and i < j:
                i += 1

            if i < j:
                A[i], A[j] = A[j], A[i]

        A[left] = A[i]
        A[i] = temp
        self.quickSort(A, left, i-1)
        self.quickSort(A, i+1, right)


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    solution = Solution()
    result = solution.sortedSquares(A)

    print result