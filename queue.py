class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return 
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def display(self):
        print(*self.items)

    def is_empty(self):
        return [True if len(self.items) == 0 else False]


    