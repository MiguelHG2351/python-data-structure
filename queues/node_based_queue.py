
class TwoWayNode(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1
    
    def dequeue(self):
        current = self.head
        if self.head is None:
            return None
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
        
        return current.data

food = Queue()

food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

print('------------')
print(food.head)

print('------------')
print(food.head.data)

print('------------')
print(food.head.next.data)

print('------------')
print(food.tail.data)

print('------------')
print(food.tail.prev.data)

print('------------')
print(food.count)

print('------------')
print(food.dequeue())
print(food.head.data)


