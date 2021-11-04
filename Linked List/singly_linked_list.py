from node import Node

class Singly_linked_list:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = node
        else:
            # node.next = self.tail
            # self.tail = node
            current = self.tail

            while current.next:
                current = current.next
            
            current.next = node
        self.size += 1
    
    def size(self):
        return self.size

    def iter(self):
        # current = self.tail
        # while current:
        #     yield current.data
        #     current = current.next
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self, data):
        current = self.tail
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.tail = current.next
                self.size -= 1
                return "Deleted"
            previous = current
            current = current.next
    
    def search(self, data):
        for node in self.iter():
            if node == data:
                print(f"Found {data}!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


words = Singly_linked_list()
words.append("eggs")
words.append("ham")
words.append("spam")
current = words.tail

while current:
    print(current.data)
    current = current.next

for word in words.iter():
    print(word)

words.clear()

for word in words.iter():
    print(word)
