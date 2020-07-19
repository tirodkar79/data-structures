class Node:
    __slots__ = ['_element', '_next']
    def __init__(self, value):
        self._element = value
        self._next = None

class CircularLinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.head._next = self.head
            self.tail = self.head
            self.size += 1
            return
        current = self.head
        while current._next != self.head:
            current = current._next
        temp = Node(value)
        current._next = temp
        temp._next = self.head
        self.size += 1
        return

    def remove(self):
        if self.head is None:
            print("Linked List is Empty")
            return 
        
        current = self.head
        while current._next._next != self.head:
            current = current._next
        
        temp = current._next
        current._next = self.head
        return temp._element



    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def print_elements(self):
        if self.is_empty():
            print("List is Empty")
            return
        current = self.head
        result = ""
        while current._next != self.head:
            result += str(current._element) + " -> "
            current = current._next
        
        result += str(current._element) + " -> " + str(self.head._element)
        print(result)
        return

dl = CircularLinkedList()
dl.insert(10)
dl.print_elements()
dl.insert(20)
dl.print_elements()
dl.insert(30)
dl.print_elements()
dl.insert(40)
dl.print_elements()
dl.insert(50)
dl.print_elements()
dl.remove()
dl.print_elements()