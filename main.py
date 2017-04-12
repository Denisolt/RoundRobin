from Simulate import Simulator
import csv

Simulation = Simulator()
number = 0
with open('process.csv') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            number = number + 1
            pid=int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            Simulation.ProcessAdd(pid,arrival,burst,number)

print('---------------------------------------------\nAdding the process to the process List\n---------------------------------------------')
for process in Simulation.list:
        print(process)
print('---------------------------------------------\n Simulation \n---------------------------------------------')
Simulation.Scheduling()
print('---------------------------------------------')