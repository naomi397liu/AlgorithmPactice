class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        '''
        have a list of rectangles and i can cut the rectangles into squares
        I need to return the number of maximum sized squares after cutting from the list
        
        iterate and get the mins from each rectangle updating the max and count
        
        '''
        maximum = 0
        for rec in rectangles:
            minimum = min(rec[0],rec[1])
            if minimum > maximum:
                maximum = minimum
                count = 1
            elif minimum == maximum:
                count += 1
        return count