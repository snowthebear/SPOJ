class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def reorder(order:list):
    stack = Stack()
    arr = []

    for i in range (len(order)):
        current = order[i]

        if stack.is_empty():
            stack.push(current)

        elif current < stack.peek():
            stack.push(current)

        elif current > stack.peek():
            while not stack.is_empty() and current > stack.peek():
                item = stack.pop()
                arr.append(item)
            stack.push(current)
        

    while not stack.is_empty():
        item = stack.pop()
        arr.append(item)

        
    return arr


def main():
    stack = Stack()

    while True:
        n = int(input())

        if (n == 0):
            break
        
        order = list(map(int, input().split()))
        result = reorder(order)

        if result == sorted(result):
            print ("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()
       