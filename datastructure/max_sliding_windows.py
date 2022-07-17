# from stack_with_max import MaxStack
from collections import namedtuple


Cache = namedtuple('Cache',"ind value")

class MaxStack(list):
    def __init__(self,*args):
        super().__init__(self, *args)
        self.max_cache = []
    def push(self, val):
        self.append(val)
        cache = Cache(len(self)-1, val)
        if len(self) > 1:
            cur = self.max_cache[-1]
            value = max([cur.value, val])
            if not (value == val):
                cache = cur
        self.max_cache.append(cache)

    def pop(self):
        x = super().pop()
        self.max_cache.pop()
        return x
    def get_max(self):
        try:
            return self.max_cache[-1].value
        except:
            return -1 * float('inf')

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
