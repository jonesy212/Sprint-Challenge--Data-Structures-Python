from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if ring is empty or has an open space
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            return
        #if at capacity
        if self.storage.length == self.capacity:
            #if the oldest is the head 
            if self.current == self.storage.head:
                #remove current item
                self.storage.remove_from_head()
                #add new item 
                self.storage.add_to_head(item)
                #update the current item
                self.current = self.storage.head.next
            #if the oldest is the tail
            elif self.current == self.storage.tail:

                self.storage.remove_from_tail()
                #add new item
                self.storage.add_to_tail(item)
                #current should still be the head 
                self.current = self.storage.head
            else:
                #set current value in the node to item
                self.current.value = item
                #current item now is set to the next node in the list
                self.current = self.current.next

                print(self.current.value)

        # # if ring is not a capacity(not full)
        # if self.current == None:
        #     self.item = self.current
        #     # self.current.next = self.current + 1
        #     print("current: ",self.current)
        #     print("item: ",self.item)         
        #     print("length: ",self.storage.length)
        # #if almost full
        # if self.storage.lengh == self.capacity -1:
        #     #update current to head
        #     self.current = self.storage.head
        #     self.storage.add_to_tail(item)
        #     return
          
        # elif self.capacity:
        #     self.storage.add_to_head(item)
        #     print("capacity", self.storage.add_to_head(item))

        # if self.current == self.storage.head:
        #     self.current == self.storage.head.next
        #     self.storage.add_to_head(item)
        #     print(self.storage.current)
        #     return
        # elif self.storage.length == self.capacity:
        #     self.storage.remove_to_head()
        #     self.sotarge.add_to_head(item)
        #     print("capacity", self.storage.length)
        #     print('self.current.next',self.current.next)
        #     self.current.next = self.current
        #     self.current = self.storage.remove_to_head.item
        #     self.current.next(item)
        # # print(self.append)

            #the next new index
            #replace the oldest
            # self.current is 
            # self.storage.append(item) = self.current

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        currentNode = self.storage.head
        while currentNode:
            if currentNode != None:
                list_buffer_contents.append(currentNode.value)
            currentNode = currentNode.next
        return list_buffer_contents
    
# RingBuffer( )
# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
