from stack_with_max import MaxStack

class Queue:
    def __init__(self):
        self.tail = MaxStack()#as tail
        self.head = MaxStack()#as head
    def enQueue(self, val):
        self.tail.push(val)
    def get_max(self):
        return max(self.tail.get_max(),self.head.get_max())
    def deQueue(self):
        if len(self.head) == 0:
            while len(self.tail):
                self.head.push(self.tail.pop())
        return self.head.pop()

def main(lst, k):
    queue = Queue()
    maxes = []
    for i in range(k):
        queue.enQueue(lst[i])
    maxes.append(queue.get_max())
    for i in range(k, len(lst)):
        queue.deQueue()
        queue.enQueue(lst[i])
        maxes.append(queue.get_max())
    return maxes
if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    k = int(input())
    print(main(lst, k))
