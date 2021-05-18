class OrderedStream:
    """
    n pairs of key value pairs
    idkey is a unique key between 1 and n 
    value is a string
    return values in increasing order according to keys as a list after each insertion

    self.x declares an instance variable x on the instance self
    """
    def __init__(self, n: int):
        self.n = n
        self.early_entries = {}
        self.i = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        '''
        taken in idkey and value pairs. if id 1 isn't yet inserted, return []
        else return the value in order of smallest to largest idkey
        
        first keep track of all the pairs
        if there is no idKey 1, return []
        if there is, then add the new value in the correct spot
        then return the pairs in the right order 
        '''
       
        idKey -= 1
        result = []
        if idKey == self.i:
            result.append(value)
            self.i += 1
        else:
            self.early_entries[idKey] = value
        while self.i in self.early_entries: #O(n)
            result.append(self.early_entries[self.i])
            self.i += 1
        return result
        
        

           
      
       

class OrderedStream:
    """
    n pairs of key value pairs
    idkey is a unique key between 1 and n 
    value is a string
    return values in increasing order according to keys as a list after each insertion

    self.x declares an instance variable x on the instance self
    """
    def __init__(self, n: int):
    
        self.i = 0
        self.arr = [False]*(n+1)

    def insert(self, idKey: int, value: str) -> List[str]:
        '''
        taken in idkey and value pairs. if id 1 isn't yet inserted, return []
        else return the value in order of smallest to largest idkey
        
        first keep track of all the pairs
        if there is no idKey 1, return []
        if there is, then add the new value in the correct spot
        then return the pairs in the right order 
        '''
       
        
        
        
        arr = self.arr
        i = self.i #class variable i starts at 0 each time this method is called
        self.arr[idKey - 1] = value
        
        if self.arr[self.i]: #no value at index 0, pass O(n) -> time limiting step
            self.i = arr.index(False, i+1) #reset class variable i to the index of the next false seen starting at the next index
        return arr[i:self.i] #then return the array from the index of this method to the index O(self.i-i) -> O(n)
        
           
      
       
