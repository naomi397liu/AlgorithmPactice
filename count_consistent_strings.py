class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        assume elements in word are unique
        
        
        """
        
        count = 0
        
        for word in words:
            letter_count = 0
            for letter in word:
                if letter in allowed:
                    letter_count += 1
                else:
                    break
            if letter_count == len(word):
                count += 1
        return count