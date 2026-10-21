class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row():
            for i in range(9):
                gadang = set()
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in gadang:
                        return False
                    gadang.add(board[i][j])
            return True

        def column():
            for i in range(9):
                gadang = set()
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] in gadang:
                        return False
                    gadang.add(board[j][i])
            return True

        def cube():
            for i in range(3):
                for j in range(3):
                    gadang = set()
                    for k in range(3):
                        for l in range(3):
                            val = board[i*3 + k][j*3 + l]
                            if val == ".":
                                continue
                            if val in gadang:
                                return False
                            gadang.add(val)
            return True

        return row() and column() and cube()
                    