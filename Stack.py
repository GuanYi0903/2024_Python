class Stack():
    def __init__(self, *args):
        self.stack_items = [arg for arg in args]

    def peek(self):
        if len(self.stack_items) > 0:
            return self.stack_items[-1]
        else:
            return None

    def pop(self):
        if len(self.stack_items) > 0:
            return self.stack_items.pop()
        else:
            return None

    def push(self, item):
        self.stack_items.append(item)

    def size(self):
        return len(self.stack_items)

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(self.stack_items)


class LinkedStack():
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        current = StackNode(data, next=self.top)
        self.top = current

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def pop(self):
        if self.top is None:
            return None
        else:
            pop_item = self.top
            self.top = pop_item.next
            return pop_item.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ""
        current = self.top
        while current:
            s = s + " " + str(current.data)
            current = current.next
        return s


class StackNode():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":

    # x = Stack(1, 2, 3, 4, 5, 6, 7)
    # x = Stack(*range(10))
    # print(x.peek(),    ", After peek: ", x)
    # print(x.pop(),     ", After pop:  ", x)
    # print(x.push(11),  ", After push:  ", x)
    # print(x.size())
    # print(len(x))

    y = LinkedStack()
    y.push(1)
    print('After push: ', y)
    y.push(2)
    print('After push: ', y)
    y.push(3)
    print('After push: ', y)

    print('After peek: ', y.peek())
    print('After pop: ', y.pop(), y)
    print('After pop: ', y.pop(), y)
    print("size = ", y.size())
