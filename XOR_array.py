def integer_to_bitwise(integer):
    bitwise = []
    while integer != 0:
        bitwise.append(str(integer % 2))
        integer = integer//2
    bitwise.reverse()
    return "".join(bitwise)


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        
        get the array
            iterate through start to n
            append to array start+2*i
        iterate through the array translating the integers into their bitwise equivalent
        iterate throught the array XOR as you go saving it to a variable
        translate back into an integer
        
        """
        integers = []
        bitwise_integers = []
        index = 0
        
        while len(integers) != n:
            integers.append(start + 2*index)
            index += 1
        starting_pt = integers[0]
        for i in range(1, len(integers)):
            starting_pt = starting_pt^integers[i]
        return starting_pt