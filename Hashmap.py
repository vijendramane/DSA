class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value   
        self.prev = None  
        self.next = None
   

class DoublyLinkedList: 
    def __init__(self): 
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_front(self, node):
        self.remove_node(node)
        self.add_to_front(node)

    def remove_last(self):
        if self.tail.prev == self.head:
            return None

        last_node = self.tail.prev
        self.remove_node(last_node)

        return last_node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.dll = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.dll.move_to_front(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.dll.move_to_front(node)

        else:
            if len(self.cache) >= self.capacity:
                removed = self.dll.remove_last()

                if removed:
                    del self.cache[removed.key]

            new_node = Node(key, value)

            self.dll.add_to_front(new_node)

            self.cache[key] = new_node

    def display(self):
        current = self.dll.head.next

        result = []

        while current != self.dll.tail:
            result.append((current.key, current.value))
            current = current.next

        print(result)


cache = LRUCache(3)

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)

cache.display()

cache.get(1)

cache.put(4, 40)

cache.display()
