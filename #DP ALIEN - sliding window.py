t = int(input("Enter a number: "))
at, bt = input("Enter At % Bt separate by space: ").split()
array = input("Enter numbers: ").split()

at = int(at)
bt = int(bt)

for i in range (len(array)):
    array[i] = (int)(array[i])

total_station = 0
total_human = 0
answer_station = 0
answer_human = 0
counter =0

for a in range (at):
    total_station +=1
    total_human += array[a]

    
        # print ("final answer: ", answer_station, answer_human)

    while (total_human > bt):
        total_human -= array[counter]
        total_station -=1
        counter += 1

    if total_station > answer_station: #update
        answer_human = total_human
        answer_station = total_station
        
    elif total_human == answer_human:
        answer_human = min(total_human, answer_human)

    

print (answer_station)
print (answer_human)

    