# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""

# class ListNode():
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""
#     def insert_after(self, value):
#         #set the current next node 
#         current_next = self.next
#         #set this current value to as the next current node
#         self.next = ListNode(self, value, current_next)
#         #if it is the current next node, assign to be next
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(self, value, current_prev)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""
#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev
  


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""
# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0
#     def __len__(self):
#         return self.length

#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""
#     def add_to_head(self, value):
#         #pass value through ListNode instance 
#         new_node = ListNode(value)
#         #increment list
#         self.length += 1
#         #if empty 
#         if self.head and self.tail == None:
#             # create a new node with a tail and a head
#             self.head = new_node
#             self.tail = new_node
#         #if there is one node
#         elif self.head == self.tail:
#             #pointer will now point to the new node created
#             self.head.prev = new_node
#             #point new node to the head
#             new_node.next = self.head
#             #make the new node the head
#             self.head = new_node
    
#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""
#     def remove_from_head(self):
#         #if theri s at least one node
#         if self.length > 0:
#             #set return value of head
#             ret_val = self.head.value
#             #point head to new node
#             new_node = self.head.next
#             #delete old head pointer
#             self.delete(self.head)
#             #update new head pointer
#             self.head = new_head
#             #decreae length after removing head
#             self.length -= 1
#             #return value 
#             return ret_val

#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""
#     def add_to_tail(self, value):
#         #if length is greater than 0
#         if self.length > 0:
#             #inser value after 
#             self.tail.insert_after(value)
#             #update tail
#             self.tail = self.tail.next
#             #increment
#             self.length += 1
#         #if length is 0
#         elif self.length == 0:
#             #assign tail to a node value
#             self.tail = ListNode(value)
#             #to have one node head and tails needs to be the same
#             self.head == self.tail
#             #increment length of tail
#             self.length += 1

#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""
#     #define remove from tail
#     def remove_from_tail(self):
#         #if length is greater than 0
#         if self.length > 0:
#             #set a return value
#             ret_value = self.tail.value
#             #create a new tail
#             new_tail = self.tail.next
#             #subtract from tail
#             self.length -= 1
#             #delete from tail
#             self.delete(self.tail)
#         #else if there is no tail
#         elif self.tail == 0:
#             #set tail to none
#             self.tail = None
#             #set head to none
#             self.head = None
#             #subtract from tail if 
#             self.length -= 1
#             #return
#             return ret_val

#     def remove_from_tail(self):
#         #if length is great than 0
#         if self.length > 0:
#             #set return value
#             ret_value = self.tail.value
#             #create a new tail
#             new_tail = self.tail.next
#             #subtract from tail
#             self.length -= 1
#             #delete from tail
#             self.delet(self.tail)
#         #if there is no tail
#         elif self.length == 0:
#             #set tail to none
#             self.tail = None
#             #set head to none
#             self.head = None
#             #decrease length
#             self.length -= 1
#             #return value
#             return ret_val


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None: 
            return "empty"
        curr_node = self.head
        output = ''
        output += f'( {curr_node.value} ) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next 
            output += f'( {curr_node.value} ) <-> '
        return output
        
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
       # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value
    
    # """Removes the input node from its current spot in the 
    # List and inserts it as the new head node of the List."""
    # def move_to_front(self, node):
    #     if node is not self.head:
    #         #1. remove
    #         self.delete(node)
    #         #2. insert
    #         self.add_to_head(node.value) #only need the node value


    # """Removes the input node from its current spot in the 
    # List and inserts it as the new tail node of the List."""
    # def move_to_end(self, node):
    #     if node is not self.tail:
    #     #1. remove
    #         self.delete(node)
    #         #2. insert @ tail
    #         self.add_to_tail(node.value)

    # """Removes a node from the list and handles cases where
    # the node was the head or the tail"""
    # def delete(self, node):
    #     if self.length == 0:
    #         #or
    #     #if not self.head and not self.tail: # deleting from empty list
    #         return 
    #     elif self.head == self.tail:  # deleting list of 1
    #         self.head = None
    #         self.tail = None
    #     elif node.prev is None:  #node is head  #self.head == node
    #         self.head = node.next 
    #     elif self.node == self.tail: # node is the tail
    #         self.tail = node.prev
    #     node.delete()
       

    # """Returns the highest value currently in the list"""
    def get_max(self):

        for i in range(0, self.length - 1):
            if(self.length > self.length):
                return self.length




















# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""
# ​
# ​
# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
# ​
# ​
# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""
# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0
# ​
#     def __len__(self):
#         return self.length
# ​
#     def __str__(self):
#         if self.head is None and self.tail is None: 
#             return "empty"
#         curr_node = self.head
#         output = ''
#         output += f'( {curr_node.value} ) <-> '
#         while curr_node.next is not None:
#             curr_node = curr_node.next 
#             output += f'( {curr_node.value} ) <-> '
#         return output
# ​
#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""
#     def add_to_head(self, value):
#         # adding to an empty list
#         new_node = ListNode(value)   
#         self.length += 1
#         if self.head is None and self.tail is None:
#             # create a new node
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # adding a new value, to existing list
#             # link new_node with current head
#             new_node.next = self.head
#             self.head.prev = new_node
#             # update head
#             self.head = new_node
        
# ​
#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""
#     def remove_from_head(self):
#         # if list is empty
#         if self.head is None and self.tail is None:
#             return  
#         # if list has only one element
#         elif self.head == self.tail:
#             # unlink the node
#             value = self.head.value
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return value
#         else:
#             # we have more than one element
#             value = self.head.value
#             next_head = self.head.next
#             next_head.prev = None
#             self.head.next = None
#             self.head = next_head
#             self.length -= 1
#             return value
# ​
#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""
#     def add_to_tail(self, value):
#         # adding to an empty list
#         new_node = ListNode(value)   
#         self.length += 1
#         if self.head is None and self.tail is None:
#             # create a new node
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
# ​
# ​
#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""
#     def remove_from_tail(self):
#        # if list is empty
#         if self.head is None and self.tail is None:
#             return  
#         # if list has only one element
#         elif self.head == self.tail:
#             # unlink the node
#             value = self.tail.value
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return value
#         else:
#             # we have more than one element
#             value = self.tail.value
#             prev_tail = self.tail.prev
#             prev_tail.next = None
#             self.tail.prev = None
#             self.tail = prev_tail
#             self.length -= 1
#             return value
# ​
#     """Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List."""
#     def move_to_front(self, node):
#         pass
# ​
#     """Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List."""
#     def move_to_end(self, node):
#         pass
# ​
# ​
#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""
#     def delete(self, node):
#         pass
        
#     """Returns the highest value currently in the list"""
#     def get_max(self):
#         pass


