class Queue:
    def __init__ (self):
        self.__items = []

    def is_empty(self):
        size = len(self.__items)
        return size == 0

    def enqueue(self, item):
        self.__items.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndentationError("La cola esta vacia.")

        return self.__items.pop()
    
    def size(self):
        return len(self.__items)
    
cola = Queue()
cola.enqueue("Juan")
cola.enqueue("Maria")
cola.enqueue("Pedro")
next_client = cola.dequeue()
print(f"Next client: {next_client}")
next_client = cola.dequeue()
print(f"Next client: {next_client}")
print(cola.size())
next_client = cola.dequeue()
print(f"Next client: {next_client}")
print(cola.size())