class Double_Ended_Queue:
    def __init__(self):
        self.items = []

    def first_enqueue(self, item):
        self.items.insert(0, item)

    def first_dequeue(self):
        return self.items.pop(0)

    def last_enqueue(self, item):
        self.items.append(item)

    def last_dequeue(self):
        return self.items.pop()

    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return

    def last(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return

    def __len__(self):
        return len(self.items)

    def display(self):
        print(*self.items)

    def is_empty(self):
        return [True if len(self.items) == 0 else False]