class Queue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0

    def __repr__(self):
        return "%s" % (self.items)

    def insert(self, item):
        self.items.append(item)
        self.tail += 1
        return self.items

    def delete(self):
        removal = self.items[0]
        self.items.remove(removal)
        self.head += 1
        return removal

    def reset(self):
        self.items = []
        self.head = 0
        self.tail = 0
        return self.items

    def is_empty(self):
        self.head = 0
        self.tail = 0
        return self.items == []

if __name__ == "__main__":
    qu = Queue()
    print(qu.head)
    print(qu.tail)
    qu.insert(1)
    print(qu.head)
    print(qu.tail)
    qu.insert(2)
    qu.insert(3)
    print(qu)
    print(qu.delete())
    print(qu)
    print(qu.head)
    print(qu.tail)
    qu.delete()
    qu.delete()
    print(qu)
    print(qu.head)
    print(qu.tail)
    qu.is_empty()
    print(qu)
    print(qu.head)
    print(qu.tail)
    '''
    a = [1,2,3]
    print(a)
    print(a.remove(a[0]))
    print(a)
    i = a[0]
    a.remove(i)
    print(a)
    '''