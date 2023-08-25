import ctypes
import sys

# there are two arrays the A array which is the initial array with data and B is the array that extends the A array


class DynamicArray:

    def __init__(self):  # create a dynamic array instance

        self.n = 0  # no of elements held in the array. 
        # we start with zero
        # current capacity of the array. we start with one and it grows with each element
        self.capacity = 1
        # make the actual array and assign it to the A(inital array)
        self.A = self.make_array(self.capacity)

    def __len__(self):  # just return the size of the array when len(x) is called

        return self.n

    def __getitem__(self, k):
        """since we are creating an array we need to access elements using indexing.
        This is done by the __getitem__ special method. 
        We check for index limits and then return fromt the A array.
        k is the index the user is indexing
        Input -> k
        return -> element from A at kth index 
         """

        if not 0 <= k < self.n:
            return IndexError("k is out of bounds")
        else:
            return self.A[k]

    def append(self, value):

        if self.n == self.capacity:
            # when we are appending we check if the current number of elements is at capacity.
            # if yes then we resize the array

            self._resize(2*self.capacity) #_resize is a private function
            
        self.A[self.n] = value # assign it at the last position.
        
        self.n += 1 #increase the number of elements in the array
        
    def _resize(self, new_cap): #dynamic increase of array size
        
        B = self.make_array(new_cap) 
        # B is the new array that is twice the cap of the original array and gets copied to
        
        for k in range(self.n):
            
            B[k] = self.A[k] # copy the elements of original array to extended array
            
        self.A = B # make this the original array
        self.capacity = new_cap #update the capacity of the new array    
        
    def make_array(self, new_cap):
        
        return (new_cap * ctypes.py_object)()
    
    
    
if __name__ == "__main__":
    
    arr = DynamicArray()
    arr.append(8)
    print(arr.capacity)
    # print(sys.getsizeof(arr))
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(3)
    arr.append(9)
    print(arr.capacity)
    arr.append(5)
    arr.append(8)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(8)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(8)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    arr.append(3)
    arr.append(9)
    arr.append(5)
    print(arr.n)
    # print(sys.getsizeof(arr))
    for num, k in enumerate(range(len(arr))):
        print(num + 1,arr[k])
    
    
