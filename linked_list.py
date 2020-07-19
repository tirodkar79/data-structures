class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size += 1
            return None

        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size += 1
            return None

        temp = Node(value)
        current = self.head
        while current.next:
            current = current.next

        current.next = temp

    def insert_pos(self, position, value):
        if self.head is None:
            if position != 1:
                return None 
            self.head = Node(value)
            self.size += 1
            return None
        current = self.head
        pos = 1
        if position == pos:
            return self.insert_start(value)

        while pos + 1 != position:
            current = current.next
            pos += 1

        temp = Node(value)
        temp.next = current.next
        current.next = temp
        return None

    def delete_pos(self, position):
        if self.head is None:
            print("Empty")
            return None
        pos = 1
        if position == pos:
            return self.delete_start()

        current = self.head
        while pos + 1 != position:
            current = current.next
            pos += 1

        temp = current.next
        current.next = current.next.next
        temp.next = None
        return temp.data

    def delete_start(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        return temp.data

    def delete_last(self):
        if self.head is None:
            return None
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        return temp.data

    def __len__(self):
        return self.size

    def print_linklist(self):
        if self.head is None:
            print("Empty")
            return
        current = self.head
        result = ""
        while current.next:
            result += str(current.data) + " -> "
            current = current.next
        result += str(current.data) + " -> " + "None"
        print(result)

def main():
    a1 = SinglyLinkedList()
    a1.insert_start(10)
    a1.insert_start(20)
    a1.insert_start(30)
    a1.insert_start(40)
    a1.insert_last(50)
    a1.insert_last(60)
    a1.insert_last(70)
    a1.insert_last(80)
    a1.insert_pos(3,100)
    a1.print_linklist()
    a1.delete_pos(3)
    a1.print_linklist()

if __name__ == "__main__":
    main()


         