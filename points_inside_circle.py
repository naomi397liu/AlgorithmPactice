class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        '''
        queries is a 2D array who's rows reflect a single circle and columns represent details about the circle (center point and radius)
        return an array of integers that reflect the number of points in or on the circle
        
        
        for each query, evaluate how many of the points are on/in that circle
        to avoid a nested loop of an n^2 runtime, lets consider a mathematical approach so we don't have to check all the points
        
        we can look at a given query and find a range of possible x vals and y.
        since multiple points can have the same coordinates, we could put the points in a dictionary with the key as the point and the value as the number of occurences at that point. we will have to create an empty array to put the answers in and it will need to be in the correct order, so we have to maintain an array for queries. 
        
        what we could also do is collect all the x and y ranges as tuples stores in a 2D list and then iterate through each point to see if it is in range
    
        '''
        num_points = 0
        result = []
        for query in queries:
            for point in points:
                if sqrt((query[0]-point[0])**2 + (query[1]-point[1])**2) <= query[2]:
                    num_points += 1
            result.append(num_points)
            num_points = 0
        return result