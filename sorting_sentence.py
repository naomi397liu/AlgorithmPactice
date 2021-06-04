class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split(" ")
        word_order = {}
        for word in sentence:
            word_order[word[-1]] = word[:len(word)-1]
        sort = word_order["1"]
        for i in range(2,len(sentence)+1):
                sort += " " + word_order[f"{i}"]
        return sort