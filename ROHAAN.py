def shortest_path(total_stations, distances):
    # Floyd-Warshall algorithm
    for transit in range(total_stations):
        for depart in range(total_stations):
            for destination in range(total_stations):
                distances[depart][destination] = min(distances[depart][destination], distances[depart][transit] + distances[transit][destination])

def main():
    t = int(input().strip())
    
    for case_num in range(t):
        total_stations = int(input().strip())
        distance = [list(map(int, input().strip().split())) for _ in range(total_stations)]
        num_order = int(input().strip())

        shortest_path(total_stations, distance)

        total = 0
        for i in range(num_order):
            s, d = map(int, input().strip().split())
            total += distance[s - 1][d - 1]

        print(f"Case #{case_num + 1}: {total}")


if __name__ == "__main__":
    main()