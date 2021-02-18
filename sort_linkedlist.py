def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    #the linked lists are sorted in increasing order
    new_head = ListNode('delete me')
    current = new_head
    currentl1 = l1
    currentl2 = l2
    while currentl1 and currentl2:
        if currentl1.val <= currentl2.val:
            current.next = currentl1
            current = current.next
            currentl1 = currentl1.next
        elif currentl1.val >= currentl2.val:
            current.next = currentl2
            currentl2 = currentl2.next
            current = current.next
    while currentl2:
        current.next = currentl2
        currentl2 = currentl2.next
        current = current.next
    while currentl1:
        current.next = currentl1
        currentl1 = currentl1.next
        current = current.next
    return new_head.next

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    #the linked lists are sorted in increasing order
    #check to see which is bigger
    # insert
    def help_me(l1,l2,merged_list):
        if l1 and l2:
            if l1.val > l2.val:
                merged_list.next = l2
                l2 = l2.next
            else:
                merged_list.next = l1
                l1 = l1.next
            merged_list = merged_list.next
            return help_me(l1,l2,merged_list)
        elif l1:
            merged_list.next = l1
            return merged_list
        elif l2:
            merged_list.next = l2
            return merged_list
        
    
    merged_list = ListNode(0)
    help_me(l1, l2, merged_list)
    return merged_list.next
        