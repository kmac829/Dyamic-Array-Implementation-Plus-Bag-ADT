 # Name: Katie Schaumleffle
# OSU Email: schaumlk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 Part 2
# Due Date: 10/18/2021
# Description: This code is part 2 of assignment 2. Here we implement a 
#               Bag ADT class by using the Dynamic Array data structure implemented 
#               in part 1 of this assignment, as the underlying data storage for the 
#               Bag ADT.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag using O(1) amortized time complexity
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the given value
        object. Returns True if an object was removed, otherwise returns false.
        Implemented using O(N) runtime complexity.
        """
        for i in range(self.size()):
            if self.da.data.get(i) == value:
                self.da.remove_at_index(i)
                return True  
        return False

    def count(self, value: object) -> int:
        """
        Returns the number of elements in the bag that matches the given
        value object. Implemented using O(n) runtime complexity.
        """
        num = 0
        for i in range(self.size()):
            if self.da.data.get(i) == value:
                num += 1
        return num


    def clear(self) -> None:
        """
        Clears the contents of the bag using O(1) runtime complexity.
        """
        #if size is 0, then bag is already empty
        if self.size == 0:
            pass
        #set array as an empty array to clear it
        else:
            empty_arr = DynamicArray()
            self.da = empty_arr

    def equal(self, second_bag: object) -> bool:
        """
        Compares the contents of the bag with contents of a second bag.
        Returns True if the bags are equal, meaning they have the same 
        number of elements and contain the same elements, regardless of order.
        Returns False otherwise. 
        """
        first_size = self.da.length()
        second_size = second_bag.da.length()

        #if sizes don't match, automatically return False
        if (first_size != second_size):
            return False
        
        #If an element doesn't match, return false. Otherwise return True
        for i in range(first_size):
            element = self.da.get_at_index(i)
            if (self.count(element) != second_bag.count(element)):
                return False
        return True


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
