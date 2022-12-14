class MyCircularQueue:
    def __init__(self, size: int):
        self.size=size
        self.queue = [0]*size
        self.rear = -1
        self.front = -1
    
    def get_front(self) -> int:
        if self.is_empty():
            return -1
        else:
            return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            return -1
        else:
            return self.queue[self.rear]
    
    def enqueue(self, value: int) -> bool:
        if not self.is_full():
            if self.front == self.rear==-1:
               self.front=self.rear=0
            else:
               self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True
        else:
            return False

    def dequeue(self) -> bool:
        if not self.is_empty():
           if self.front == self.rear:
             self.front =-1
             self.rear=-1
           else:
             self.front = (self.front+1)%self.size
           return True
        else:
            return False

    def is_empty(self):
        return (self.front==self.rear==-1)

    def is_full(self):
        return (self.front == 0 and self.rear == (self.size - 1)) or (self.front == (self.rear + 1) % self.size)


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
