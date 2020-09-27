class Node:
    """
    Node is an element consisting of key, value and references to its previous and
    next nodes.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRUCache is a data structure of Least Recently Used(LRU) pages/memory/etc.
    """
    def __init__(self, capacity):
        self.head = None    # head of a doubly linked list
        self.tail = None    # tail of a doubly linked list
        # hashmap = {key: Node}
        self.hashmap = {}
        self.maxlen = capacity
        self.currlen = 0

    """Prepend the newly accessed value"""
    def prepend(self, key, val):
        new_node = Node(key, val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    """Remove the least recently used value from the end"""
    def remove_tail_node(self):
        if self.tail != None:
            if self.tail.prev is None:
                self.tail = None
                self.head = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev

    """Move the most recently used value to the front of the dll"""
    def move_to_front(self, node):
        if node.prev != None:
            if node.next == None:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    """Print the LRUCache"""
    def print_list(self):
        i = self.head
        print("** Printing LRU cache **")
        while i != None:
            print(i.val)
            i = i.next

    """Get the value of the key"""
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_to_front(node)
            return node.val
        else:
            return -1
        
    """Insert/ Put the key value pair"""
    def put(self, key, val):
        if self.maxlen == 0:
            return
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_to_front(node)
        else:
            if self.currlen < self.maxlen:
                self.currlen += 1
            else:
                del self.hashmap[self.tail.key]
                self.remove_tail_node()
            self.prepend(key, val)
            self.hashmap[key] = self.head

"""Instantiate the LRUCache object and use it accordingly"""
obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
obj.put(4, 4)
obj.print_list()
print("Getting the value to key 2: %d" % (obj.get(2)))
print("Getting the value to key 3: %d" % (obj.get(3)))
print("Getting the value to key 1: %d" % (obj.get(1)))
obj.print_list()