from linked_list import SinglyLinkedList

class Queue:
    def __init__(self):
        self.s = SinglyLinkedList()

    def enqueue(self, value):
        self.s.insert_last(value)

    def dequeue(self):
        return self.s.delete_start()

    def print_queue(self):
        self.s.print_linklist()

    def is_empty(self):
        if self.s.size == 0:
            return True
        return False

    def __len__(self):
        return self.s.size

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.s.head.data

def main()
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    print(queue.peek())

if __name__ == "__main__":
    main()