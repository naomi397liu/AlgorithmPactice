class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        return t or f -> do the arrays represent the same string
        two arrays represent the same string if the array elements concatenated in order forms the same string
        
        """
        return "".join(word1) == "".join(word2)