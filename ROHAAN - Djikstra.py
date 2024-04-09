import heapq

def dijkstra(total_stations, distances, start):
    # Dijkstra's algorithm
    min_distances = [float('inf')] * total_stations
    min_distances[start] = 0

    heap = [(0, start)]

    print("heap = ", heap)
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        print ("min_distances[curr_node]:", min_distances[curr_node])
        if curr_dist > min_distances[curr_node]:
            continue

        for neighbor, weight in enumerate(distances[curr_node]):
            new_dist = curr_dist + weight

            if new_dist < min_distances[neighbor]:
                min_distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return min_distances

def main():
    t = int(input().strip())
    
    for case_num in range(t):
        total_stations = int(input().strip()) #n
        distances = [list(map(int, input().strip().split())) for _ in range(total_stations)]
        num_order = int(input().strip()) #r
        print ("distance = ", distances)

        total = 0
        for i in range(num_order):
            s, d = map(int, input().strip().split())
            print("s = ", s)
            min_distances = dijkstra(total_stations, distances, s - 1)
            total += min_distances[d - 1]
            

        print(f"Case #{case_num + 1}: {total}")

if __name__ == "__main__":
    main()
