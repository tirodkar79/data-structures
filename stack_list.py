from linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self.s = SinglyLinkedList()

    def push(self, value):
        self.s.insert_start(value)

    def pop(self):
        return self.s.delete_start()

    def print_stack(self):
        self.s.print_linklist()

    def is_empty(self):
        if self.s.size == 0:
            return True
        return False

    def __len__(self):
        return self.s.size

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.s.head.data

def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.pop()
    stack.pop()
    stack.print_stack()
    print(stack.peek())

if __name__ == "__main__":
    main()
    