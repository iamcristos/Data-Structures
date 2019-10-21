import sys
sys.path.insert(1, '../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size = self.size + 1
        return self.storage.add_to_head(value)
        pass

    def pop(self):
        if (self.size) :
            self.size -= 1
            return self.storage.remove_from_tail()
        pass

    def len(self):
        return self.size
        pass
