def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        head.next, head, prev = prev, head.next, head
    return prev