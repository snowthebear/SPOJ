from queue import Queue

def bfs(table, visited):
    starts = []
    
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j] == 'A':
                starts.append((i, j))
    
    
    total = 0
    for start in starts:
        q = Queue()
        q.put((start, 1)) #start step 1
        visited[start[0]][start[1]] = True

        current_total = 1

        while not q.empty():
            (x, y), steps = q.get()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

            for xpoint, ypoint in directions:
                nx, ny = xpoint + x, ypoint + y

                if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and table[nx][ny] == chr(ord(table[x][y]) + 1):
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.put(((nx, ny), steps+1))
                        
                        current_total = max(current_total, steps+1)

        total = max(total, current_total)
        
    return total

def main():
    case_number = 1
    while True:
        height, width = map(int, input().split())

        if height == 0 and width == 0:
            break

        table = []

        for _ in range (height):
            letters = input().strip() 
            table.append(letters.upper())

        visited = [[False] * width for _ in range (height)] #memo
        result = bfs(table, visited)

        print(f"Case {case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()