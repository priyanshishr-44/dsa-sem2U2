class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        print("Resizing from", self.capacity, "to", self.capacity * 2)
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            return "Empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.arr[:self.size])


# ---------------- Singly Linked List ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- Doubly Linked List ----------------
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp
                if temp.next:
                    temp.next.prev = new
                temp.next = new
                return
            temp = temp.next

    def delete_pos(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp:
                temp = temp.next
        if not temp:
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if pos == 0:
            self.head = temp.next


# ---------------- Stack using SLL ----------------
class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, x):
        self.sll.insert_begin(x)

    def pop(self):
        if not self.sll.head:
            return "Empty"
        val = self.sll.head.data
        self.sll.head = self.sll.head.next
        return val

    def peek(self):
        if not self.sll.head:
            return "Empty"
        return self.sll.head.data


# ---------------- Queue using SLL ----------------
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return "Empty"
        return self.head.data


# ---------------- Parentheses Checker ----------------
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() == pairs[ch]:
                stack.pop()
            else:
                return False

    return stack.peek() == "Empty"


# ---------------- MAIN TEST ----------------
if __name__ == "__main__":
    print("Dynamic Array Test:")
    da = DynamicArray()
    for i in range(10):
        da.append(i)
    da.display()
    print("Pop:", da.pop())
    da.display()

    print("\nParentheses Test:")
    print("([]):", is_balanced("([])"))
    print("([)]:", is_balanced("([)]"))
    print("(((:", is_balanced("((("))
    print("Empty:", is_balanced(""))
