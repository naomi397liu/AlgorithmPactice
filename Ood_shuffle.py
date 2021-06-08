import random
import re
def shuffle(deck):
    shuffled = []
    while len(shuffled) != len(deck):
        card = deck[random.randint(0, len(deck)-1)]
        shuffled.append(card)
    return shuffled

def sum_vowel(s):
    
    vowel_weight = {}
    for i, vowel in enumerate(['a','e','i','o','u']):
        vowel_weight[vowel] = i+1
    s = list(s)

    def helper(vowel_sum, s, vowel_weight):
        if s == []:
            return vowel_sum
        char = s.pop()
        if char in vowel_weight.keys():
            vowel_sum += vowel_weight[char]
        return helper(vowel_sum, s, vowel_weight)
    
    return helper(0, s, vowel_weight)

# def find_word(s):
#     if len(s) < 9 and len(s) > 4:
#         return re.compile("oodo").match(s) or re.compile("code").match(s) or re.compile("work").match(s):
#     return False 


# s = "oodo"
# p = re.compile("oodo").match(s)
# print(p)
# print(find_word(s))