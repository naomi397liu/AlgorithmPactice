
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
        
        prev = self.head
        current = self.head 
        place_holder = self.head
        while(place_holder is not None):
            current = prev.next #current = a, b
            current.next = prev # b->a, current.next
            prev = prev.next
            place_holder = place_holder.next # place_holder = b
            print(f'current = {current.data}, place holder = {place_holder.data} {place_holder.next.data} {place_holder.next.next.data} prev = {prev.data}')
        self.head = self.tail
        return self.printList()
 
    # Utility function to print the linked LinkedList
    def printList(self):
        current = self.head
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


