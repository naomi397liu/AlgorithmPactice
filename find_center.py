class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''
        edges is an array of lists where the list indicates which nodes are connected
        return center
        
        plan of action:
        iterate through each num and if there is a number that was repeated, return it
        
        edge case: what if there is only 1 node?
        '''
        pair_initial = edges[0]
        if len(edges) > 1 and pair_initial[0] in edges[1]:
            return pair_initial[0]
        else:
            return pair_initial[1]