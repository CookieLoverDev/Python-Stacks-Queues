#Stack data structure where the elements of the stack are implemented as Nodes
#Below this code you can find code where the elements are implemented as tuples
class Stack:
    def __init__(self):
        self.stack = []

class Node:
    def __init__(self, valueA, valueB):
        self.x = valueA
        self.y = valueB

def push(self, item):
    if item not in self.stack:
        self.stack.append(item)
        return ("Element added")
    else:
        return ("Element already in the stack")

def pop(self):
    if len(self.stack) == 0:
        return ("Stack is currently empty")
    else:
        self.stack.pop()
        return ("Element removed")
    
def size(self):
    return len(self.stack)

def isEmpty(self):
    answer = True if (self.stack == 0) else False
    return answer

def top(self):
    if isEmpty(self):
        return ("Stack is empty")
    else:
        return self.stack[-1]
    
def viewStack(self):
    return self.stack

L = Stack()
e1 = Node(1, 2)
e2 = Node(3, 4)
e3 = Node(5, 6)
e4 = Node(7, 8)
e5 = Node(9, 10)
e6 = Node(11, 12)

tmpList = [e1, e2, e3, e4, e5, e6]
for i in tmpList:
    print(push(L, i))

print(viewStack(L))
print(top(L))
print(pop(L))
print(viewStack(L))
print(top(L))
print(size(L))
print(isEmpty(L))

#Here is implementation with elements as tuple of two real numbers
S = Stack()
tmpList = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (1, 2), (2, 1)]
for i in tmpList:
    print(push(S, i))

print(viewStack(S))
print(top(S))
print(pop(S))
print(viewStack(S))
print(top(S))
print(size(S))
print(isEmpty(S))