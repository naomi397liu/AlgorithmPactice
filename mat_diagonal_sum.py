class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        
        '''
        total = 0
        
        size = len(mat)
        i = size-1
        for j in range(size): # j = [0,1,2] 
            if i == j:
                total += mat[j][j]
            else:
                total += mat[j][j]
                total += mat[j][i]
            i -= 1
        return total