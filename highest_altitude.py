class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        alt = 0
        each element represents the net gain in alt
        figure out which position did he have the highest alt
        
        create a list of relative alts
        current_alt starts at 0
        the first should be at 0, and then adds the next val in gain and appends
        '''
        alt = 0
        list_alts = [0]
        for diff in gain:
            alt += diff
            list_alts.append(alt)
        return max(list_alts)