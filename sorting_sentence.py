class Solution:
    def sortSentence(self, s: str) -> str:
        """
        O(2n) where the time limiting step would be the first loop
        """
        sentence = s.split(" ")
        word_order = {}
        for word in sentence:
            word_order[word[-1]] = word[:len(word)-1]
        sort = word_order["1"]
        for i in range(2,len(sentence)+1):
                sort += " " + word_order[f"{i}"]
        return sort

    def sortSentence(self, s: str) -> str:
        """
        O(n)
        """
        sentence = s.split(" ")
        sort = [0]*len(sentence)
        for i, word in enumerate(sentence):
            sort[int(word[-1])-1] = word[:len(word)-1]
        
        return " ".join(sort)