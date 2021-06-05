class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        '''
        # create diagonal lists and sort
        diagonals = {} #str of starting row,col
        for i, row in enumerate(mat):
             for j, col in enumerate(row):
                    if i == 0 or j == 0:
                        diagonals[f"{i-j}"] = [col] #starts first value of all diagonals
                    else:
                        diagonals[f"{i-j}"].append(col)
                        
        for key in diagonals:
            diagonals[key].sort(reverse = True)
            
        for i, row in enumerate(mat):
             for j, col in enumerate(row):
                    mat[i][j] = diagonals[f"{i-j}"].pop()
        return mat