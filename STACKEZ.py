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



def main():
    stack = Stack()

    t = int(input())

    for i in range (t):
        query = input().split()
        
        if query[0] == '1':
            stack.push(int(query[1]))

        elif query[0] == '2':
            stack.pop()

        elif query[0] == '3':
            top = stack.peek()

            if top is not None:
                print(top)
            else:
                print("Empty!")


if __name__ == "__main__":
    main()