class Stack:
    def __init__(self):
        self.items = []
    def __repr__(self):
        return "%s" %(self.items)
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    stk = Stack()
    e = stk.is_empty()
    print(stk)
    print(e)
    stk.push(1)
    print(stk)
    print(stk.pop())
    print(stk)


    a = [1,2,3]
    print(a)
    d = {
        0: '0',
        1: '1',
        2: '2'
    }
    print(d.items())
    print(d)