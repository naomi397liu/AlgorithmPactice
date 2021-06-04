class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        '''
        get the values out of the linked list and put them in an array
        iterate through the array from back to front, adding
        2^index if it's a 1
        [10010]
        
        '''
        
        binary_arr = []
        while head:
            binary_arr.append(head.val)
            head = head.next
        i = len(binary_arr) - 1
        num = 0
        for bit in binary_arr:
            if bit == 1:
                num += 2**i
            i -= 1
        return num