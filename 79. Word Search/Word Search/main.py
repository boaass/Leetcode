# coding=utf-8
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(r, c, word):
            if len(word) == 0:
                return True

            # 上
            if r - 1 >= 0 and board[r-1][c] == word[0]:
                tmp = board[r][c]
                board[r][c] = '#'
                if dfs(r-1, c, word[1:], 0):
                    return True
                board[r][c] = tmp
            # 下
            if r + 1 <= row - 1 and board[r+1][c] == word[0]:
                tmp = board[r][c]
                board[r][c] = '#'
                if dfs(r+1, c, word[1:], 1):
                    return True
                board[r][c] = tmp
            # 左
            if c - 1 >= 0 and board[r][c-1] == word[0]:
                tmp = board[r][c]
                board[r][c] = '#'
                if dfs(r, c-1, word[1:], 2):
                    return True
                board[r][c] = tmp
            # 右
            if c + 1 <= col - 1 and board[r][c+1] == word[0]:
                tmp = board[r][c]
                board[r][c] = '#'
                if dfs(r, c+1, word[1:], 3):
                    return True
                board[r][c] = tmp
            return False

        # find first word position
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r, c, word[1:]):
                        return True

        return False

if __name__ == '__main__':
    board = [["C","A","A"],
             ["A","A","A"],
             ["B","C","D"]]

    word = "AAB"

    s = Solution()
    print s.exist(board, word)