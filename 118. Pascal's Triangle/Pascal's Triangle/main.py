# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for i in range(numRows):
            if i == 0:
                r.append([1])
            elif i == 1:
                r.append([1, 1])
            else:
                row = [1]
                for j in range(1, i):
                    row.append(r[i-1][j-1] + r[i-1][j])
                row.append(1)
                r.append(row)

        return r


if __name__ == '__main__':
    s = Solution()
    r = s.generate(5)
    print r