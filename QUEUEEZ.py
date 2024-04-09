class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)

    def serve(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def __len__(self):
        return self.items


def main():
    tc = int(input())
    q = Queue()

    for i in range (tc):
        query = input().split()

        if query[0] == '1':
            q.append(int(query[1]))
        
        elif query[0] == '2':
            q.serve()

        elif query[0] == '3':
            top = q.peek()

            if top == None:
                print("Empty!")
            else:
                print(top)

if __name__ == "__main__":
    main()