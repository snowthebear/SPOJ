from collections import deque

def main():
    d = deque()

    t = int(input())
    reverse = False

    for i in range (t):
        query = input().split()

        if query[0].lower() == 'back':
            if len(d) > 0:
                if reverse == False:
                    item = d.pop()
                    
                elif reverse == True:
                    item = d.popleft()

                print(item)
                
            else:
                print("No job for Ada?")


        elif query[0].lower() == 'front':
            if len(d) > 0:
                if reverse == False:
                    item = d.popleft()

                elif reverse == True:
                    item = d.pop()

                print(item)

            else:
                print("No job for Ada?")
        

        elif query[0].lower() == 'reverse':
            # d.reverse()
            reverse = not reverse

        elif query[0].lower() == 'push_back':
            if reverse == False:
                d.append(int(query[1]))
            else:
                d.appendleft(int(query[1]))

        elif query[0].lower() == 'tofront':
            if reverse == False:
                d.appendleft(int(query[1]))
            else:
                d.append(int(query[1]))


if __name__ == "__main__":
    main()