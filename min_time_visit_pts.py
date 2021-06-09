class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        iterate thru the points in the array
        find the distance between points:
            -diagonals is most efficient, so move diagonally until you have to move     
            either horizontally or vertically
            -for example if the difference is [3,5], then you can add 3 to both initial x,y and that would be 3 secs, plus moving up 2 which would be 2 secs
            -
        
        
        '''
        secs = 0
        
        for i, point in enumerate(points):
            if i == len(points)-1:
                break
            x = abs(points[i][0]-points[i+1][0])
            y = abs(points[i][1]-points[i+1][1])
            
            secs += max(x,y)
        return secs