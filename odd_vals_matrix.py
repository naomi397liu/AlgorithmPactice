class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        '''
        r = row that should increment
        c = col that should increment
        
        m = 2, n = 3, indices = [[0,1],[1,1]]
        indices[0] = [0,1] r-> [[1,1,1],[0,0,0]] 
                            c-> [[1,2,1],[0,1,0]]
                    [1,1] r-> [[1,2,1],[1,2,1]]
                          c-> [[1,3,1],[1,3,1]]
        
        
        make the array
        iterate through each cell in the array, if the cell's row num is equal to  indicies[i][0] or if the cell's col num is equal to indicies[i][1] then add 1 to the value
        '''
        
       
        row_indices = {}
        for index in indices:
            if index[0] in row_indices.keys():
                row_indices[index[0]] += 1
            else:
                row_indices[index[0]] = 1
                
        col_indices = {}
        for index in indices:
            if index[1] in col_indices.keys():
                col_indices[index[1]] += 1
            else:
                col_indices[index[1]] = 1
        
        matrix = []
        for i in range(m):
            if i in row_indices.keys():
                matrix.append([row_indices[i]]*n)
            else:
                matrix.append([0]*n)
        #val is the num to add to the element and the key is the col index
        
        count = 0
        for i in range(m):
            for j in range(n):
                if j in col_indices.keys():
                    matrix[i][j] += col_indices[j]
                if matrix[i][j] % 2 != 0:
                    count += 1
            
        return count