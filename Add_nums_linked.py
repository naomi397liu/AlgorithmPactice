class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None

class Solution(object):
    # def reverse(self):
    #     self.head = self.head
    #     self.tail = self.head #tail now points to the head
    #     self.head = self.head.next #head now points to the value after head
    #     current = self.head.next #current is assigned to the value after the head
    #     while current != None: #as long as the next value is not none
    #         self.head = current.next #keep reassigning head to the next value
    def init(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # added_list = []
        # reversel1 = []
        # reversel2 = []
        # #reverse digits
        # while l1.val != None:
        #     reversel1.append(l1.val)
        # reversel1.reverse()
        # l1_num = int("".join(reversel1))
            
        # while l2.val != None:
        #     reversel2.append(l2.val)
        # reversel2.reverse()
        # l2_num = int("".join(reversel2))
            
        # #turn digits into integer
        # #do the same with the next linked list
        # addition = l1_num + l2_num
        # #add the 2 numbers
        # str_sum = str(addition)
        # for digit in str_sum:
        #     self.val = digit
        #     self = next
        
        # #put sum into list with one digit in each position and reverse the order
        # return self
llist = Solution()
llist = ListNode(2)        
llist.next = ListNode(4)
llist.next.next = ListNode(3)
l2_node = ListNode(5)
l2_node.next = ListNode(6)
l2_node.next.next = ListNode(4)
Solution.reverse(llist)
    # addTwoNumbers(l1_node, l2_node)