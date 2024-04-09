from queue import PriorityQueue


#----------- pake priority queue --------------
def time (n, m, lst):
    q = PriorityQueue()
    time = 0
    
    for i in range (len(lst)):
        q.put((i, lst[i]))


    while not q.empty():

        job = q.queue.pop(0)
       
        for i in range (q.qsize()):
            next_job = q.queue[i]

            if next_job[1] > job[1]:
                q.queue.append(job)
                break
            
        else:
            time += 1
            if job[0] == m:
                return time 

                
#------------ pake list ---------------
# # def time(n, m, lst):

# #     queue = list(enumerate(lst)) #[(0, 1), (1, 1), (2, 9), ...
# #     time = 0

#     while True:

#         job = queue.pop(0)

#         for i in range (len(queue)):
#             if queue[i][1] > job[1]:
#                 queue.append(job)
#                 break

#         else: #kalo g counter break
#             time += 1
#             if job[0] == m:
#                 return time
        

def main():
    tc = int(input())

    for _ in range (tc):
        n , m = map(int, input().split()) #n = number of job in queue , m = position of your job

        level = list(map(int, input().split())) #priority level
        # print(n , m , level)

        result = time(n, m, level)

        print(result)

main()