from queue import PriorityQueue

def play(hero, tower, damage, health):
    q = PriorityQueue()
    
    for h in health:
        q.put(-h)


    # for i in range (tower): 
    #     current_hero = -q.get()
    #     print("current herro = ", current_hero)
        
    #     current_hero -= damage
        
    #     q.put(-current_hero)

    count = 0
    for i in range (hero):
        current_hero = -q.get()
         
        while current_hero > damage:
             current_hero -= damage
             count += 1
        q.put(-current_hero)

    print (q.queue)

    if count < tower:
        return "NO"

    # while not q.empty():
    #     remaining_health = -q.get()
    #     if remaining_health <= 0:
    #         return "NO"

    return "YES"


def main():
    t = int(input())

    for i in range (t):
        hero, tower, damage = map(int, input().split())
        health = []

        for j in range (hero):
            health.append(int(input()))

        result = play(hero, tower, damage, health)
        print(result)
        

if __name__ == "__main__":
    main()