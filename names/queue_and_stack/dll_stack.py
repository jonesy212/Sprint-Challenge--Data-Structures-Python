import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        #set storage DLL
        self.storage = DoublyLinkedList()
        #add - where do we need to check the stack size
        self.size = 0
    def push(self, value):
        #add- where do we need to add item to the stack
        self.storage.add_to_head(value)
        #increase stack length
        self.size += 1
    #define a way to remove items from the stack
    def pop(self):
        #take into account if there is nothing to remove
        if self.storage.length > 0:
            #set a variable 
            remove_stack = self.storage.remove_from_head()
            #remove from stack length
            self.size -= 1
            #return current length after removing an item
            self.storage.length
            #return removed stack
            return remove_stack
    #def length
    def len(self):
        #return size of length
        return self.size