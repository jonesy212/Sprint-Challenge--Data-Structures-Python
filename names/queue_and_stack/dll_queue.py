import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        #keep track of size
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #assign storage to the DoublyLinked List
        self.storage = DoublyLinkedList()
    #adding
    def enqueue(self, value):
        # how do you add to the end of the queue
        self.storage.add_to_tail(value)
        # increment to size
        self.size += 1
        #print queue
        # print(self.storage)
    #removing
    def dequeue(self):
        #if queue is not empty
        if self.storage.length > 0:    
        # how do you remove one from the front
            remove_storage = self.storage.remove_from_head()
            self.size -= 1
            return remove_storage
            # print(self.remove_storage)
        #accessing length
            if self.size is None:
                return 0
    def len(self):
        return self.size



#notes
#     #return the middle of a DLL, if there are two noes, return the left one
#     #1 - 2 - 3 : 2
#     #1 - 2 - 3 - 4 : 2

#    def find_middle(dll) :
#        head = dll.head
#        tail = dll.tail
       
#        while head != tail and head.next != tail:
#            head = head.next
#            tail = tail.prev

#         return head.value

# odd_nums = DoublyLinkedList()
# [odd_num.add_tail_(i) for i in [5,3,10,3]
# ]

# even_nums = DoublyLinkedList()
# [even_nums.add_tail_(i) for i in [4,3,'10', 7, 8]]
# print(find_middle(even_nums))


# #first in first out

# plan
#     - floor division
#     - get length by traversing it
#     - which direction
#        - forwards
#        - backwards

# head                            tail
#        5 -> 3 -> 4 -> 10 -> 7
#     hi ->                ti  <- ti

#        if hi == ti
#        return .length

#        hi = head.next
#        ti = head.next +1
#        if ti = none
#        hi = ti/2




# #no recursion
# # we can't stor the DLL and it's data is in other data structures

# def reverse(dll):
#     curr_nex = current.next
    
#     if current.next, current.prev is None:
#         current.next, current.prev = current.prev, curren.next
#     while current.next is not None:
#         prev = 



#         new = current.next
#         whle new is not None:
#             prev = current
#             current = new
#             current.next = prev
#             #moves on
#             new = current.next
        



#     loop 
#     switch pointer change head and tail