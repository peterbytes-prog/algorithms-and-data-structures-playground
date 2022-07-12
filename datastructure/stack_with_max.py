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
        return self.max_cache[-1]
def main():
    max_stack = MaxStack()
    num_queries = int((input()))
    for _ in range(num_queries):
        query = input().split()
        if query[0] == 'push':
            max_stack.push(int(query[1]))
        elif query[0] == 'pop':
            max_stack.pop()
        elif query[0] == 'max':
            print(max_stack.get_max().value)
        else:
            assert(0)

if __name__ == '__main__':
    main()
