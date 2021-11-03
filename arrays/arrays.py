# reduce
import random
import functools

class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self._items = list()
        for count in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)
    
    def __iter__(self):
      return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value

    def __fillrandom__(self, a, b):
        for i in range(len(self._items)):
            self._items[i] = random.randint(a, b)
            
    def __sum__(self):
        return functools.reduce(lambda x, y: x + y, self._items)
