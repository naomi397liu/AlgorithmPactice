def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        tempPrev = prev 
        tempHead = head 
        tempNext = head.next

        head.next = tempPrev
        prev = tempHead 
        head = tempNext
    return prev