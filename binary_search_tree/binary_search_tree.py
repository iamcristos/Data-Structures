# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_value = self.value
        if(current_value > value):
            if(self.left == None):
                return BinarySearchTree(value)
            else:
                return self.left.insert(value)
        else:
            if(self.right == None):
                return BinarySearchTree(value)
            else:
                return self.right.insert(value)   
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is the current value
        current_value = self.value
        if (current_value == target):
            return True
        # check if target is greater than value
        if (current_value > target):
            # check if left is empty
            if (self.left == None):
                return False
            else:
                return self.left.contains(target)
        if (current_value < target):
            if (self.right == None):
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_value = self.value
        if current_value is None:
            return None
        # check if the right is empty
        if (self.right is None):
            return current_value
        # then recursively check the right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
            #  check if the left has value
            if self.left is not None:
                self.left.for_each(cb)
            # check if the right is not None
            if self.right is not None:
                self.right.for_each(cb)
                
    def itter_df_for_each(self,cb):
        # create a stack
        stack = []
        # let's push the node in the stack
        stack.append(self)
        # let loop through the stack
        while len(stack):
            current_node = stack.pop()
            # check if the right has item
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # check if there is a value
        if self.value:
            # check if the node has a left
            if node.left:
                # recursively call the left item
                self.in_order_print(node.left)
            # print the item
            print (self.value)
            # check if the node has a right item
            if node.right:
                # recursively call the right
                self.in_order_print(node.right)
            # print the right
            print(self.value)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue data structure
        queue = Queue()
        
        # enque the starting node on the queue
        queue.enqueue(node)
        # loop while the queue has data
        while queue.len():
            
            # deque the current node off the stack
            current_node = queue.dequeue()
            # print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.right:
                
                # enque the left child
                queue.enqueue(self.left)
            # if the current node has a right child
            if current_node.left:
                queue.enqueue(self.right)
                # enque right child on to the stack
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack data structure
        stack = Stack()
        # push the starting node on the stack
        stack.push(node)
        # loop while the stack has data
        while stack.len():
            # pop the current node off the stack
            current_node = stack.pop()
            # print the current value
            print(current_node.value)
            # if the current node has a right child
            if current_node.right:
                # push the right child
                stack.push(current_node.right)
            # if the current node has a left child
            if current_node.left:
                # push left child on to the stack
                stack.push(current_node.left)
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
