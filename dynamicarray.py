import ctypes

class DynamicArray(object):
    
    #
    def __init__(self):
        
        self.no_of_elements = 0 #number of elements in the array
        self.capacity = 1 # capacity of the array
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.no_of_elements
    
    def __getitem__(self, index):
         
        if not 0 <= index < self.no_of_elements:
            return IndexError('Index out of bounds')
        return self.A[index] 
    
    def append(self, element):
        if self.no_of_elements == self.capacity:
            self._resize(2*self.capacity) #2x if capacity is reached
        
        self.A[self.no_of_elements] = element
        self.no_of_elements += 1
        
    def _resize(self, new_capacity):
        
        B = self.make_array(new_capacity)
        
        for k in range(self.no_of_elements):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_capacity
        
    def make_array(self, new_capacity):
        
        return (new_capacity * ctypes.py_object)()
    
if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(1)
    print(len(arr))
    arr.append(7)
    print(arr[1])