import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        #set value
        self.value = value
        #set traverse left
        self.left = None
        #st traverse right
        self.right = None

    def insert(self, value):
        #if there is no value on the left of the tree and the value is current value is less than the tree value, 
        if self.left is None and value <= self.value:
            self.left = BinarySearchTree(value)
            return
        #if the value is larger, make sure it goes to the right
        elif self.right is None and value >= self.value:
            self.right = BinarySearchTree(value)
            return
        #if value is less current value insert to the left
        if value <= self.value:
            self.left.insert(value)
        #if the current value is greater than the visited node value insert to the right of that value
        if value >= self.value:
            self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    #Return max value found in the tree
    def get_max(self):
        #right as fir as you can go
        #and self.right is None
        #return max
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #1. Base case: Left is None or Right is None
        cb(self.value)  
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

        #2. Recursive case:
        # Go Left and Right
    

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

      #go left FIRST
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)

        #go right
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #can't be done with recursion
        #goes wide (left to right on each level)
        #create a queue
        queue = Queue()
        #if there is no node
        queue.enqueue(node)
        #if there is at least one item in the queue
        while (queue.len() > 0):
        #remove from the queue
            temp = queue.dequeue()
            #print value
            print(temp.value)
            #if temp left
            if temp.left:
                queue.enqueue(temp.left)
            #if temp right
            if temp.right:
                queue.enqueue(temp.right)
        
            #dequeue a node
            #print the node
            #add it's children
                #i.e add left (if you can)
                #add right (if you can)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    #using the binary search tree
    def dft_print(self, node):
        stack = Stack()
        #if there is no add a new Node
        stack.push(node)
        #if there is at least one item in the queue
        while stack.len() > 0:
            #remove item from queue
            temp= stack.pop()
            #print value
            print(temp.value)
            #if the temp is to the left
            if temp.left:
                stack.push(temp.left)
            # if the temp is to the right
            if temp.right:
                stack.push(temp.right)
            



    # def dft_print(self, node):
    #     removed_node = node
    #     #create a node stack
    #     if self.head == None:
    #         self.head = dft_print(node)
    #         self.size += 1
    #     #push the current node on to the stack
    #     if self.head >= 0:
    #         self.head = self.head.next
    #         self.size += 1
         
    #     #while we have items on stack
    #     while node >= 0:
    #         #print the current value and pop it off
    #         if self.head:
    #             print(self.head.pop())
    #             self.size -= 1
    #             return removed_node
    #             #push right value of current node if we can
    #             if self.right is True:
    #                 self.node.right.push(value)   
    #             #push the left value of current node if we can
    #             if self.left is True:
    #                 self.node.left.push(value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(12)

# bst.insert(19)
# bst.insert(23)
# bst.insert(34)

# bst.for_each(print)