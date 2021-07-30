def searchMatrix(mat, value):
    for x in range(len(mat)):
        #quick finish
        if mat[x][0] == value:
            return True
        
        #check next array first value
        if x + 1 < len(mat):
            if mat[x+1][0] > value:
                if value in mat[x]:
                    return True
                return False
        
        #check this array if there is no next array
        if x == len(mat) - 1:
            if value in mat[x]:
                return True
            return False
    return False
  
mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True

print(searchMatrix(mat, 8))
# True