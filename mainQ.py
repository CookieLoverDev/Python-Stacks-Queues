#As with the Stack, here I have version implemented with node and tuples

class Queue:
    def __init__(self):
        self.queue = []

class Node:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

def enqueue(self, item):
    if item not in self.queue:
        self.queue.append(item)
        return ("Element added")
    else:
        return ("Element already in the stack")

def dequeue(self):
    if len(self.queue) == 0:
        return ("Stack is currently empty")
    else:
        self.queue.pop(0)
        return ("Element removed")
    
def size(self):
    return len(self.queue)

def isEmpty(self):
    answer = True if (self.queue == 0) else False
    return answer

def top(self):
    if isEmpty(self):
        return ("Stack is empty")
    else:
        return self.queue[-1]
    
def viewStack(self):
    return self.queue

Qn = Queue()
p1 = Node("Umidjon", "Khodjamov")
p2 = Node("Alisher", "Khodjamov")
p3 = Node("Nikita", "Proskuryakov")

tmpL = [p1, p2, p3]
for i in tmpL:
    print(enqueue(Qn, i))

print(size(Qn))
print(top(Qn))
print(viewStack(Qn))

print(dequeue(Qn))

print(size(Qn))
print(top(Qn))
print(viewStack(Qn))
print(isEmpty(Qn))

Qt = Queue()
tmpL = [("Umidjon", "Khodjamov"), ("Alisher", "Khodjamov"), ("Nikita", "Proskuryakov")]
for i in tmpL:
    print(enqueue(Qt, i))

print(size(Qt))
print(top(Qt))
print(viewStack(Qt))

print(dequeue(Qt))

print(size(Qt))
print(top(Qt))
print(viewStack(Qt))
print(isEmpty(Qt))