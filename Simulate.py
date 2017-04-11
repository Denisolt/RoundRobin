import queue,csv

MaxTime = 300
class Process: # Definining Process
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
    def __str__(self):
        return '|ID:{:3d}| Arrival Time:{:3d}| Burst Time:{:3d}|'.format(self.pid,self.arrival,self.burst)


class Simulator:
    def __init__(self, tq=2):
        self.quantum = tq
        self.clock = 0
        self.list = []
        self.ProcessQueue = queue.Queue()
        self.RunQueue = queue.Queue()

    def ProcessAdd(self, pid, arrival, burst, number):
        process = Process(pid, arrival, burst)
        self.list.append(process)

    def Check(self, clock):
        for process in self.list:
                if process.arrival == self.clock and number <= 3:
                    self.ProcessQueue.put(process)
                    break

    def Scheduling(self):
        self.timer = 0
        for process in self.list:
                if process.arrival == self.clock and number <= 3:
                    self.ProcessQueue.put(process)
                    break
        while self.clock < MaxTime:
            #self.Check(self.clock)
            self.clock = self.clock + 1
            self.Check(self.clock)
            
            if not self.ProcessQueue.empty():
                process = self.ProcessQueue.get()
                if(process.burst < self.quantum):
                    self.timer = self.timer + process.burst
                    bur = process.burst
                    process.burst = 0
                    print '|ID:{:3d}| Start:{:3d}| End:{:3d}| Time Left:{:3d}'.format(process.pid, self.timer - bur, self.timer, process.burst)
                else:
                    process.burst = process.burst - self.quantum
                    print '|ID:{:3d}| Start:{:3d}| End:{:3d}| Time Left:{:3d}'.format(process.pid, self.timer, self.timer + self.quantum, process.burst)
                    self.timer = self.timer + self.quantum
            self.clock = self.clock + 1
            self.Check(self.clock)

            if not process.burst <= 0:
                self.ProcessQueue.put(process)

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