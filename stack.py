class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def multiple_push(self, item_list):
        self.items.extend(item_list)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return

    def is_empty(self):
        return [True if len(self.items) == 0 else False]

    def __len__(self):
        return len(self.items)

    def display(self):
        print(*self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()