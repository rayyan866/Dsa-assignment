class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Index out of range")

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete(self, index):
        if index < 0:
            raise IndexError("Index out of range")

        if self.head is None:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def rotate(self, k):
        if not self.head or k <= 0:
            return

        length = self.size()
        k = k % length
        if k == 0:
            return

        fast = slow = self.head
        for _ in range(k):
            if fast is None:
                return
            fast = fast.next

        if fast is None:
            return

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

    def interleave(self, other_list):
        dummy = Node()
        tail = dummy
        l1, l2 = self.head, other_list.head

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            tail.next = l2
            l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        self.head = dummy.next

    def middle_element(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def split(self, index):
        if index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            self.head = None
            return new_list

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        new_list = SinglyLinkedList()
        new_list.head = current.next
        current.next = None
        return new_list

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example :
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original list:")
ll.print_list()

ll.insert(2, 6)
print("\nAfter inserting 6 at index 2:")
ll.print_list()

ll.delete(3)
print("\nAfter deleting element at index 3:")
ll.print_list()

print("\nSize of the list:", ll.size())
print("Is the list empty?", ll.is_empty())

ll.rotate(2)
print("\nAfter rotating the list by 2 positions to the right:")
ll.print_list()

ll.reverse()
print("\nAfter reversing the list:")
ll.print_list()

ll.prepend(0)
print("\nAfter prepending 0 to the list:")
ll.print_list()

ll2 = SinglyLinkedList()
ll2.append(7)
ll2.append(8)
ll2.append(9)
ll.merge(ll2)
print("\nAfter merging with another list [7, 8, 9]:")
ll.print_list()

ll3 = SinglyLinkedList()
ll3.append(10)
ll3.append(11)
ll3.append(12)
ll.interleave(ll3)
print("\nAfter interleaving with another list [10, 11, 12]:")
ll.print_list()

print("\nMiddle element of the list:", ll.middle_element())
print("Index of element 8:", ll.index_of(8))

ll4 = ll.split(5)
print("\nAfter splitting the list at index 5:")
print("First part:")
ll.print_list()
print("Second part:")
ll4.print_list()


