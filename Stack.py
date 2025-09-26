class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            return None # Or raise an exception

        def peek(self):
            if not self.is_empty():
                return self.items[-1] # Access the last element without removing it
            return None # Or raise an exception

        def is_empty(self):
            return len(self.items) == 0

my_stack = Stack()
for i in [3,5,6,2,1,4,6,9]:
     my_stack.push(i)

# my_stack.push(20)
print(my_stack.peek()) # Output: 20
print(my_stack.pop())  # Output: 20
print(my_stack.peek()) # Output: 10