class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        '''
        put the paths in a set
        if cityBi is equal to a cityAi, then check if cityAi's cityBi is equal to a cityAi, etc
        once this is not true, return cityBi
        
        the first city has a unique city as cityA
        
       
        '''
        dic_paths = {}
        for path in paths: #O(n) where n is the number of paths
            dic_paths[path[0]] = path[1]
        for end in dic_paths.values(): #O(n)
            if end not in dic_paths.keys(): 
                return end