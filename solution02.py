class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError()

    def is_empty(self):
        return len(self.items) == 0


def sort_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        current = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > current:
            stack.push(temp_stack.pop())

        temp_stack.push(current)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


def test_sort_stack():
    stack1 = Stack()
    stack1.push(5)
    stack1.push(2)
    stack1.push(8)
    stack1.push(1)
    stack1.push(3)

    sort_stack(stack1)

    assert stack1.items == [8, 5, 3, 2, 1]

    stack2 = Stack()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    stack2.push(4)
    stack2.push(5)

    sort_stack(stack2)
    assert stack2.items == [5, 4, 3, 2, 1]

    stack3 = Stack()
    stack3.push(5)
    stack3.push(4)
    stack3.push(3)
    stack3.push(2)
    stack3.push(1)

    sort_stack(stack3)
    assert stack3.items == [5, 4, 3, 2, 1]

    stack4 = Stack()
    stack4.push(1)

    sort_stack(stack4)
    assert stack4.items == [1]

    stack5 = Stack()

    sort_stack(stack5)
    assert stack5.items == []

    stack6 = Stack()
    stack6.push(3)
    stack6.push(1)
    stack6.push(3)
    stack6.push(2)
    stack6.push(3)

    sort_stack(stack6)
    assert stack6.items == [3, 3, 3, 2, 1]

    stack7 = Stack()
    stack7.push(10)
    stack7.push(-5)
    stack7.push(0)
    stack7.push(-3)
    stack7.push(7)

    sort_stack(stack7)
    assert stack7.items == [10, 7, 0, -3, -5]

    print("Все тесты пройдены")


test_sort_stack()


    
