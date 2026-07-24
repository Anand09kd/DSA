class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if (self.isEmpty()):
            raise Exception("Empty Queue")
        else:
            return self.items.pop(0)

# Runner Code
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
# q.delete()