# Python Implementation of Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def deleteNodeAtPosition(self, position):
        if self.head == None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    def getCount(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False

    def getNth(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        assert False, "Error: Index out of range"

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Driver Code
if __name__ == "__main__":
    llist = LinkedList()

    llist.append(6)

    llist.push(7)

    llist.push(1)

    llist.append(4)

    llist.insertAfter(llist.head.next, 8)
