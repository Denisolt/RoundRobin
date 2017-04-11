import queue,csv

MaxTime = 100
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

    def ProcessAdd(self, pid, arrival, burst):
        process = Process(pid, arrival, burst)
        self.list.append(process)

    def Check(self, clock):
        for process in self.list:
                if process.arrival == self.clock:
                    self.ProcessQueue.put(process)

    def Scheduling(self):
        self.timer = 0
        while self.clock < MaxTime:
            for process in self.list:
                if process.arrival == self.clock:
                    self.ProcessQueue.put(process)
                    break

            if not self.ProcessQueue.empty():
                process = self.ProcessQueue.get()
                process.burst = process.burst - self.quantum
                if(process.burst < 0):
                    process.burst = 0
                else:
                    print '|ID:{:3d}| Start:{:3d}| End:{:3d}| Time Left:{:3d}'.format(process.pid, self.timer, self.timer + self.quantum, process.burst)
                #print(process)

            self.timer = self.timer + self.quantum
            self.clock = self.clock + 1
            self.Check(self.clock)
            #this should let the process + 1.arrival == self.clock and put it in the queue
            #if process.arrival == self.clock:
            #        self.ProcessQueue.put(process)
            if not process.burst <= 0:
                    self.ProcessQueue.put(process)


Simulation = Simulator()

with open('process.csv') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            pid=int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            Simulation.ProcessAdd(pid,arrival,burst)

print('Adding the process to the process List\n---------------------------------------------')
for process in Simulation.list:
        print(process)
print('---------------------------------------------\n Simulation \n---------------------------------------------')
Simulation.Scheduling()