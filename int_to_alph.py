class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = list(string.ascii_lowercase)
        s = list(s)
        results = []
        double = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#' and i==2:
                results.append(alpha[int(s[i-2]+s[i-1])-1])
                results.reverse()
                return "".join(results)
            elif s[i] == '#':
                results.append(alpha[int(s[i-2]+s[i-1])-1])
                double = 1
            elif double == 1 or double == 2:
                double += 1
            elif double == 3:
                double = 0
                results.append(alpha[int(s[i])-1])
            else:
                results.append(alpha[int(s[i])-1])
        results.reverse()
        return "".join(results)