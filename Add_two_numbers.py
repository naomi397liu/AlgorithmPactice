# Definition for singly-linked list.
#medium level
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #reverse both lists
        # iterate thru each list and add the sum the values to a new list
            #add the sum mod 10 to the next linkedlist item
        
        new_headl1 = l1
        new_headl2 = l2
        list_sum_head = ListNode(0)
        list_sum = list_sum_head
        
        while new_headl1 or new_headl2:
            if new_headl1:
                list_sum.val += new_headl1.val
                new_headl1 = new_headl1.next
            if new_headl2:
                list_sum.val += new_headl2.val
                new_headl2 = new_headl2.next
                
            temp_sum = list_sum.val
            list_sum.val = list_sum.val % 10
            
            if (not new_headl2) and (not new_headl1):
                break
                
            list_sum.next = ListNode(temp_sum // 10)    
            list_sum = list_sum.next
        if (temp_sum //10) != 0:
            list_sum.next = ListNode(temp_sum // 10)
        return list_sum_head