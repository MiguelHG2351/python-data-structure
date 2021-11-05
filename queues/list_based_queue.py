# Queue first in first out
class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self, item):
        self.items.insert(0, item)
        self.size += 1
    
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1

        return data
    
    def traverse(self):
        for item in self.items:
            print(item)

food = ListQueue()

food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

print(food.dequeue())
print("------------------")
print(food.traverse())
