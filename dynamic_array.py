# Name: Katie Schuamleffle
# OSU Email: schaumlk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 Part 1
# Due Date: 10/18/2021
# Description: Assignment number 2 gets us familiar with using dynamic arrays by
#               implementing a Dynamic Array class. This class uses a static array
#               object as its underlying data storage container and provides several
#               methods, including resize(), append(), insert_at_index(), remove_at_index(),
#               slice(), merge(), map(), filter(), and reduce()

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying storage for the array. Only
        accepts positive integers for new_capacity.
        """
        #check if capacity is less than current size
        if new_capacity < self.size or new_capacity <= 0:
            return
        #create a new, larger array
        temp_array = StaticArray(new_capacity)
        #copy elements into new static array
        for i in range(self.size):
            temp_array.set(i, self.get_at_index(i))
        #update new array
        self.capacity = new_capacity
        self.data = temp_array 

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array.
        """
        #if size == capacity, resize to twice the capacity
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.size += 1
        self.set_at_index(self.size - 1, value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index in the dynamic array.
        """
        #make sure index is valid
        if index < 0 or index > self.size:
            raise DynamicArrayException

        #Check if array is filled
        elif self.size == self.capacity:
            self.resize(self.capacity * 2)

        #insert value at specified index
        for i in range(self.size-1, index -1, -1):
            self.data[i+1] = self.data[i]
        self.data[index] = value
        self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at a specified index from the dynamic array.
        """
        #Check if index is valid
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        elif self.size == 0:
            pass

        #resize if elements stored in array is strictly less than 1/4 of capacity
        if self.size < (self.capacity / 4):
            #Don't reduce if capacity is less than or equal to 10
            if self.capacity <= 10:
                for i in range(index, self.size -1):
                    self.data[i] = self.data[i+1]
                self.data[self.size-1] = None
                self.size -= 1

            #If current capacity before reduction is greater than 10, set size to 10
            elif self.capacity // 2 <= 10:
                self.resize(10)
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i+1]
                self.data[self.size-1] = None
                self.size -= 1
            
            #capacity is reduced to twice the size of current size
            else:
                new_capacity = self.size * 2
                self.resize(new_capacity)
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i+1]
                self.data[self.size-1] = None
                self.size -= 1

        #check if index is at end of list
        elif index == self.size - 1:
            self.data[index] = None
            self.size -= 1
        else:
            #iterate through array, moving elements over to the right by 1
            for i in range(index, self.size-1):
                self.data[i] = self.data[i+1]
            #delete at index, and move back to the right
            self.data[self.size -1] = None 
            self.size -= 1 



    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new dynamic array that contains the requested number of elements
        from the original array starting with the element located at the requested
        start index
        """
        if start_index < 0 or start_index >= self.size or size < 0 or size > self.size-start_index:
            raise DynamicArrayException

        #create new array starting with element at requested start index
        new_arr = DynamicArray()
        for i in range(start_index, size+start_index):
            new_arr.append(self.data[i])
        return new_arr

    def merge(self, second_da: object) -> None:
        """
        Takes another dynamic array as a parameter and appends all elements 
        from this second dynamic array onto the current one.
        """
        for i in range(second_da.size):
            self.append(second_da[i])

    def map(self, map_func) -> object:
        """
        Creates a new dynamic array where the value of each element is derived 
        by applying a map_func to the corresponding value from original array.
        Works similarly to the built-in map() function in Python.
        """
        new_arr = DynamicArray()
        #scan old array, adding to new array
        for i in range(self.length()):
            new_arr.append(map_func(self.data[i]))
        
        return new_arr

    def filter(self, filter_func) -> object:
        """
        This method creates a new dynamic array created only with those elements from
        original array for which filter_func returns true. Similar to built in Python
        function filter()
        """
        new_arr = DynamicArray()

        #scan old array, if True, add elements to new array
        for i in range(self.length()):
            if filter_func(self.data[i]) == True:
                new_arr.append(self.data[i])

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements in the Dynamic
        array and returns the resulting value. The method takes an optional initializer 
        parameter. If this is not provided, the first value is used as the initializer.
        If the array is empty, the method returns the value of the initiailer (None if not
        provided)
        """
        reduced = 0
        #array is empty, but initializer is given
        if self.size == 0 and initializer != None:
            return initializer

        #if array is empty, return none
        elif self.size == 0:
            return None

        #if array has one element
        elif initializer == None and self.size == 1:
            return self.data[0]

        #if initializer is given
        elif initializer != None:
            reduced = initializer 
            for i in range(self.size):
                reduced = reduce_func(reduced, self.data[i])

        #if initializer is not given
        else:
            reduced = self.data[0]
            for i in range(1, self.size):
                reduced = reduce_func(reduced, self.data[i])

        return reduced




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))