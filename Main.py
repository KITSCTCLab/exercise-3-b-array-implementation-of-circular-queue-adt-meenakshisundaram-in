class MyCircularQueue:
    def __init__(self, size: int):
        self.size=size
        self.queue = []
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        self.queue.append(value)
        self.rear+=1

    def dequeue(self) -> bool:
        if not self.is_empty():
           self.queue.pop(0)
           self.front+=1

    def get_front(self) -> int:
        return self.front

    def get_rear(self):
        return self.rear

    def is_empty(self):
        if len(self.queue)==0:
            return True

    def is_full(self):
        if len(self.queue)==self.size:
            return True


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
