class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        '''
        if b,d,f,h are white
        and if 2, 4,6,8 are white
        if either the letter or the number are white than the square is white
        but if both or neither are white than the square is black
        
        this describes an xor -> off set than true/white
        
        
        '''
        dic_white = {"a":False, "b":True, "c":False, "d":True, "e":False, "f":True, "g":False, "h":True, "1": False, "2":True, "3":False, "4":True, "5":False, "6": True, "7":False, "8": True}
        coordinates = list(coordinates)
        letter_color = dic_white[coordinates[0]]
        num_color = dic_white[coordinates[1]]
        
        return letter_color^num_color