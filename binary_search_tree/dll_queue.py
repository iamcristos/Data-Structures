import sys
sys.path.insert(1, '../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)
        # pass

    def dequeue(self):
        
        if self.storage.head is None:
            return
        value = self.storage.remove_from_head()
        return value
        # pass

    def len(self):
        return self.size
        # pass
