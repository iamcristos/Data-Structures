import sys
sys.path.append('../queue_and_stack')
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
        elif (current_value > target):
            # check if left is empty
            if (self.left == None):
                return False
            else:
                return self.left.contains(target)
        else:
            if (self.right == None):
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_value = self.value
        # check if the right is empty
        if (self.right == None):
            return current_value
        # then recursively check the right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value != None:
            cb(self.value)
            #  check if the left has value
            if self.left != None:
                self.left.for_each(cb)
            # check if the right is not None
            if self.right != None:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
