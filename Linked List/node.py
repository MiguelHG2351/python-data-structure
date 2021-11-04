# El primero en entrar es el último en salir
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
