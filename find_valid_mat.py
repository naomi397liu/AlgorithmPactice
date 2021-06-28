class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        '''
        
        
        '''
        num_r = len(colSum)
        num_c = len(rowSum)
        mat = []
        
        for i in range(num_c):
            mat.append([0]*num_r)
            
        for i, r in enumerate(mat):
            for j, c in enumerate(r):
                if rowSum[i] < colSum[j]:
                    mat[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                if rowSum[i] >= colSum[j]:
                    mat[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        return mat