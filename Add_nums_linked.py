
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None
 
    # Function to reverse the linked list

    def reverse(self):
        #current is the new order and prev is the previous order
        
        prev = None
        head = self.head
        while head:
            tempPrev = prev 
            tempHead = head 
            tempNext = head.next

            head.next = tempPrev
            prev = tempHead 
            head = tempNext
        return prev
 
    # Utility function to print the linked LinkedList
    def printList(self, node1):
        current = node1
        while(current != None):
            print(current.data)
            current = current.next

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node

        if self.tail is not None: #if the list is not empty
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node


