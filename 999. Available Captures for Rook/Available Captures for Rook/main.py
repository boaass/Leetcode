# -*- coding:utf-8 -*-

# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.
#  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
# and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
#  then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite
# colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other
# friendly bishops.
#
# Return the number of pawns the rook can capture in one move.

# Example 1:
#
#
#
# Input:
# [
# [".",".",".",".",".",".",".","."],
# [".",".",".","p",".",".",".","."],
# [".",".",".","R",".",".",".","p"],
# [".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".","."],
# [".",".",".","p",".",".",".","."],
# [".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".","."]]
# Output: 3 Explanation: In this example the rook is able to capture all the pawns. Example 2:
#
#
#
# Input:
# [
# [".",".",".",".",".",".",".","."],
# [".","p","p","p","p","p",".","."],
# [".","p","p","B","p","p",".","."],
# [".","p","B","R","B","p",".","."],
# [".","p","p","B","p","p",".","."],
# [".","p","p","p","p","p",".","."],
# [".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".","."]]
# Output: 0 Explanation: Bishops are blocking the rook to capture any pawn. Example 3:
#
#
#
# Input:
# [
# [".",".",".",".",".",".",".","."],
# [".",".",".","p",".",".",".","."],
# [".",".",".","p",".",".",".","."],
# ["p","p",".","R",".","p","B","."],
# [".",".",".",".",".",".",".","."],
# [".",".",".","B",".",".",".","."],
# [".",".",".","p",".",".",".","."],
# [".",".",".",".",".",".",".","."]]
# Output: 3 Explanation: The rook can capture the pawns at positions b5, d6 and f5.

# Note:
#
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r_row, r_col = 0, 0
        for row in xrange(len(board)):
            isbreak = False
            for col in xrange(len(board[row])):
                if board[row][col] == 'R':
                    r_row = row
                    r_col = col
                    isbreak = True
                    break
            if isbreak is True:
                break

        # print 'r_row: %d --- r_col: %d' % (r_row, r_col)

        num = 0
        for col in reversed(xrange(r_col + 1)):
            if board[r_row][col] == 'B':
                break
            elif board[r_row][col] == 'p':
                # print 'r_row: %d --- col: %d' % (r_row, col)
                num += 1
                break

        for col in xrange(r_col, len(board[r_col])):
            if board[r_row][col] == 'B':
                break
            elif board[r_row][col] == 'p':
                # print 'r_row: %d --- col: %d' % (r_row, col)
                num += 1
                break

        for row in reversed(xrange(r_row + 1)):
            if board[row][r_col] == 'B':
                break
            elif board[row][r_col] == 'p':
                # print 'row: %d --- r_col: %d' % (row, r_col)
                num += 1
                break

        for row in xrange(r_row, len(board[r_row])):
            if board[row][r_col] == 'B':
                break
            elif board[row][r_col] == 'p':
                # print 'row: %d --- r_col: %d' % (row, r_col)
                num += 1
                break

        return num


if __name__ == '__main__':
    board = [
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            ["p","p",".","R",".","p","B","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","B",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
    solution = Solution()
    num = solution.numRookCaptures(board)
    print 'num --- %d' % num
