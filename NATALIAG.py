from queue import Queue


def bfs(maze, row, col):

    visited = [[False] * col for _ in range (row)]

    for i in range (len(maze)):
        for j in range (len(maze[i])):
            if maze[i][j] == '$':
                start = (i, j)
                break
    
    q = Queue()
    q.put((start, 0)) #start step 0

    while not q.empty():

        point, steps = q.get()
        x, y = point[0], point[1]

        directions = [(0,1), (0,-1), (1,0), (-1,0)] #atas kanan kiri bawah

        for xpoint, ypoint in directions:
            nx, ny = x + xpoint, y + ypoint

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '*':
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    if maze[nx][ny] == '#':
                        return steps + 1  # destination reached
                    
                    q.put(((nx,ny), steps + 1))

    return -1


def main():
    t = int(input())

    for _ in range (t):
        row, col = input().split()
        row, col = map(int, (row, col))

        maze = []

        for i in range (row):
            line = input().strip()
            maze.append(line)

        result = bfs(maze, row, col)

        print(result)
        
        


if __name__ == "__main__":
    main()