class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def palindromo(self):
        n = self.peek()
        _n = n
        rev = 0
        while n>0:
            remainder = n % 10
            rev = rev * 10 + remainder
            n = n // 10
        if _n == rev:
            print(_n, 'is a palindrome number')
        else:
            print(_n, 'is not a palindrome number')

    def __str__(self):
        return str(self.stack)
my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(18)
my_stack.push(5560655)
print(my_stack)
print(my_stack.palindromo())
print(my_stack.peek())
print(my_stack)
