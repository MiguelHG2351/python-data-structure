class Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        while self.inbound_stack:
            self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop(0) if self.outbound_stack else None


numbers = Queue()
numbers.enqueue(5)
numbers.enqueue(6)
numbers.enqueue(7)

print(numbers.inbound_stack)

print('------------')
print(numbers.dequeue())

print('------------')
print(numbers.inbound_stack)

print('------------')
print(numbers.outbound_stack)

print('------------')
print(numbers.dequeue())

print('------------')
print(numbers.outbound_stack)

print('------------')
print(numbers.dequeue())

print('------------')
print(numbers.outbound_stack)
