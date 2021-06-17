import math




def validate_sudoku(board):
    rowD = {}
    colD = {}
    txtD = {}
    for x in range(9):
        row = board[x]
        for y in range(9):
            #check for empty
            if " " == row[y]:
                continue
            
            #add to row
            if x not in rowD:
                rowD[x] = [row[y]]
            else:
                if row[y] not in rowD[x]:
                    rowD[x].append(row[y])
                else:
                    return False
            
            #add to col
            if y not in colD:
                colD[y] = [row[y]]
            else:
                if row[y] not in colD[y]:
                    colD[y].append(row[y])
                else:
                    return False
            
            #add to 3x3
            rowVal = math.floor(y / 3)
            colVal = math.floor(x / 3)
            if f"{colVal}{rowVal}" not in txtD:
                txtD[f"{colVal}{rowVal}"] = [row[y]]
            else:
                if row[y] not in txtD[f"{colVal}{rowVal}"]:
                    txtD[f"{colVal}{rowVal}"].append(row[y])
                else:
                    return False
    return True

board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))
# True