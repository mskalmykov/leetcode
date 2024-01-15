def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sqrs = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            n = int(board[i][j])

            if n in rows[i]: return False
            if n in cols[j]: return False

            sqrs_idx = (i // 3) * 3 + (j // 3)
            if n in sqrs[sqrs_idx]: return False

            rows[i].add(n)
            cols[j].add(n)
            sqrs[sqrs_idx].add(n)

    return True

board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(board)
print(isValidSudoku(board))
