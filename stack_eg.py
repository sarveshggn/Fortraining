class Stack:
    def __init__(self):
        self.stack = list()

    def push(self , value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) < 1:
            print("Stack is already empty")

        else:
            self.stack.pop()

    def print_stack(self):
        print(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.print_stack()
