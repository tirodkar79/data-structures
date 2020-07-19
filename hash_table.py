class Node(object):
    def __init__(self, data, details):

        self.data = data
        self.next = None
        self.details = details


class LinkedList():
    def __init__(self):

        self.head = None

    def insert_data(self, data, details):

        new_node = Node(data, details)

        if not self.head:

            self.head = new_node
            return

        start = self.head

        while start.next:
            start = start.next

        start.next = new_node

        return

    def search(self, key):

        if not self.head:
            return False

        cur_node = self.head

        while cur_node and cur_node.data != key:
            cur_node = cur_node.next

        if not cur_node:
            return False

        return cur_node.details

    def pop(self, key):

        if not self.head:
            return

        cur_node = self.head

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if not cur_node:
            return

        prev.next = cur_node.next
        cur_node = None

        print("Deleted successfully")
        return


n = int(input("Enter the capactiy you want to store: "))

bucket = [0]*n

for i in range(0, n):

    data = int(input("Enter the Roll No "))
    index = data % n

    Name = input("Enter Name ")
    Std = input("Class ")

    details = [Name, Std]

    if bucket[index] == 0:

        bucket[index] = LinkedList()
        bucket[index].insert_data(data, details)

    else:

        bucket[index].insert_data(data, details)

search_key = int(input("Search key "))

index = search_key % n

print(bucket[index].search(search_key))
