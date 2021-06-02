class Node:
    def __init__(self, nex=None, prev=None, data=None):
        self.next = nex
        self.prev = prev
        self.data = data
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data): #adds to the top/front of the list
        
        new_node = Node(data=new_data) #creates a node to start with that is none
        new_node.next = self.head #next node is what was previously the head
        new_node.prev = None #top is none
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    
    def delete(self, node_to_delete):
        
        if self.head is None or node_to_delete is None:
            return
     
        if node_to_delete.next:
           
            node_to_delete.next.prev = node_to_delete.prev
        if node_to_delete.prev: 
            
            node_to_delete.prev.next = node_to_delete.next
        
        
   
      
    def index_to_data(self, val):
        i = 0
        node_head = self.head
        while node_head.data != val:
            node_head = node_head.next
        return node_head
    
    def data_to_index(self, val):
        i = 0
        node_head = self.head
        while node_head.data != val.data:
            node_head = node_head.next
            i+=1
        return i
    
    def printllist(self):
        node_head = self.head
        while node_head:
            print(node_head.data)
            node_head = node_head.next
            
    
    
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        P = [1,m]
        max of i is len(queries)-1
        resulting P is the answer
        
        queries[i] is the value of the item we want to move
        
        plan of action:
        create P
        save P.index(queries[i]) to a var

        use P.pop(P.index(queries[i]))
        then P.insert(0, var)

        maybe make it a linked list
        """
#         take the new data from the current node and push() then prev.next = head.next where head is the current node
        llist = LinkedList()
        for i in range(m, 0, -1):
            llist.push(i)
    
        result = []
        for i in range(len(queries)):
            node_to_move = llist.index_to_data(queries[i])
            new_node = node_to_move
            #add index of value in P == queries[i]
            index = llist.data_to_index(node_to_move)
            result.append(index)
            #adjust llist
            llist.push(new_node.data)
            llist.delete(node_to_move)
            
            
        
            
        return result
        