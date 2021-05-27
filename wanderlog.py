# given a  list of names with roman numerals, sort them by name and
# then by roman numeral

def romanToInt(self, s: str) -> int:
        total = 0
        dictionary = {}
        dictionary['I'] = 1
        dictionary['V'] = 5
        dictionary['X'] = 10
        dictionary['L'] = 50
        dictionary['C'] = 100
        dictionary['D'] = 500
        dictionary['M'] = 1000
        for i, char in enumerate(s):
            if i < len(s) - 1 and dictionary[char] < dictionary[s[i+1]]:
                total -= dictionary[char]
            else:
                total += dictionary[char]
        return total