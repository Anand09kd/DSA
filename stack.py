class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, value):
        self.s.insert(0, value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]

    def pop(self):
        if len(self.s) == 0:
            raise Exception("stack is Empty")
        else:
            return self.s.pop(0)

# Runner Code
stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.pop())