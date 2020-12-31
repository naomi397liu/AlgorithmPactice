
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
        prev = None
        self.tail = self.head
        current = self.head
        while(current is not None):
            prev = current #assign prev to current
            current = current.next #make next value current value
        self.head = prev
 
    # Utility function to print the linked LinkedList
    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node


