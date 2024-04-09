from queue import Queue

def bfs(lst, start, end, map1):
    visited = set()

    queue = Queue()
    queue.put((start, [start]))

    shortest_paths = []

    while not queue.empty():
        current, path = queue.get()

        if current == end:
            shortest_paths.append(path)
        
        if current not in visited:
            visited.add(current)

            neighbors = sorted(lst[current - 1])

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.put((neighbor, path + [neighbor]))
   
    new_shortest = []
    c = 0

    for i in range (len(shortest_paths)):
        new_shortest.append([])
        for j in range (len(shortest_paths[i])):
            new_shortest[c].append(map1[shortest_paths[i][j]])
        c += 1

    if len(new_shortest) == 0:
        return shortest_paths
    
    sorted_paths = sorted(new_shortest)
    
    #cari paling pendek, urut terkecil
    x = len(sorted_paths[0])

    if len(sorted_paths) > 1:
        for i in range (len(sorted_paths)):
            if (len(sorted_paths[i])) < x:
                x = i
                break
    else:
        x = 0
            
    return shortest_paths[x]



def main():
    tc = int(input())

    for a in range (tc):
        relation = int(input())

        map1 = {}
        map2 = {}
        lst = []
        c = 1

        #langkah 1 & 2 (buat adjacency list nya)
        for i in range (relation): #from a planet i you can go to planet j, this relation is symmetric,
            p, q = input().split()
            if p not in map1.values():
                map1[c] = p
                map2[p] = c
                c += 1
                lst.append([])

                if q not in map1.values():
                    map1[c] = q
                    map2[q] = c
                    c += 1
                    lst.append([])
                

            elif q not in map1.values():
                map1[c] = q
                map2[q] = c
                c += 1
                lst.append([])

    
            lst[map2[p]-1].append(map2[q])
            lst[map2[q]-1].append(map2[p])

        
        #langkah 3: using bfs
        s, d = input().split()
        start = map2[s]
        end = map2[d] 

        shortest_paths = bfs(lst, start, end, map1)


        if not shortest_paths:
            print(f"Scenario #{a + 1}: -1")
        else:
            print(f"Scenario #{a + 1}: {len(shortest_paths)}")
            print(" ".join(map1[adj_index] for adj_index in shortest_paths))


main()