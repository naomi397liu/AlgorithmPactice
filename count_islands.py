def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def visit_cell(row, col, grid, seen):
        seen.add((row,col))
        if row + 1 < len(grid) and (row+1, col) not in seen and int(grid[row+1][col]) == 1:
            seen.update(visit_cell(row+1, col, grid, seen))
        if col + 1 < len(grid[0]) and(row, col+1) not in seen and int(grid[row][col+1]) == 1:
            seen.update(visit_cell(row, col+1, grid, seen))
        if row - 1 >= 0 and (row-1, col) not in seen and int(grid[row-1][col]) == 1:
            seen.update(visit_cell(row-1, col, grid, seen))
        if col - 1 >= 0 and (row, col-1) not in seen and int(grid[row][col-1]):
            seen.update(visit_cell(row, col-1, grid, seen))
        return seen
                    
                    
    #create a 'seen' and a 'to be seen':
    island_count = 0
    seen = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (r,c) not in seen and int(cell) != 0:
                seen.update(visit_cell(r, c, grid, seen))
                print(r,c)
                island_count += 1
            
    return island_count