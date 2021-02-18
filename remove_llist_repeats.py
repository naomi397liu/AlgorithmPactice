def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # while head is not none:
    # check to see if the number is the same as the prev and if it is, then repoint the prev to the one after the number you're on and then check that number
    #return the head
    
    if not head or not head.next:
        return head

    top, prev, current = head, head, head.next
    seen = {prev.val}
    
    while current:
        if current.val in seen:
            prev.next, current = current.next, current.next
            
        else:
            seen.add(current.val)
            current, prev = current.next, prev.next

    return top
            