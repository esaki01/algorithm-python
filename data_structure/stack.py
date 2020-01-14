class Stack:
    def __init__(self, stack=None):
        if isinstance(stack, list):
            self.stack = stack
        elif stack is None:
            self.stack = []
        else:
            print(f'The stack is invalid type: {stack}')

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print('The stack has no element')
