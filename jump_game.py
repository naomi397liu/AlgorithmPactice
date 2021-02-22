def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
    def help_me(arr, start, already_visited):
        if start >= len(arr) or start < 0 or start in already_visited:
            return False
        if arr[start] == 0: 
            return True
        already_visited.add(start)
        return help_me(arr, start + arr[start], already_visited) or help_me(arr, start - arr[start], already_visited) 
    
    already_visited = set()
    
    return help_me(arr, start, already_visited)