import Queue
import csv

''''
Theory
Round Robin CPU Scheduling method.
When applying round robin method, we assign a quantum time limit for all processes that arrives to the cpu. each process
can use the cpu resources only during the given quantum time. If it did not finish in the given time the process is moved
in the end of the ready queue.

Step#1 if the process not finished in the time limit, move to end of ready Queue.
step#2 if the process finished in the time limit, terminate process.
'''

q=Queue.Queue()


class Process: #Here we define a process.
    def __init__(self,id,a,b): #for THe process's ID, Arrival Time, and Burst Time.
        self.id = id
        self.a = a
        self.b = b
    def __str__(self):
        return 'ID:{:3d} Arrive:{:3d} Burst:{:3d} '.format(self.id,self.a,self.b)

class Schedule:
    def __init__ (self,tq=2):
        self.tq=tq
        self.timer=100
        self.clock=0
        self.process=[]
        self.runtime=0

    def addP(self,id,a,b):
        p=Process(id,a,b)
        self.process.append(p)
    def schedule(self):
        while self.timer > 0:
            for p in self.process:
                    if p.a == self.clock :
                            q.put(p)
                            print 'Initailizng  Process',p.id,' to Queue at',self.clock,': 00 \n'
            #  run process
            if not q.empty():
                    p = q.get()
                    print(p)
                    p.b=p.b-self.tq
                    if not p.b <= 0 :
                        q.put(p)
            self.clock=self.clock+1
            self.timer=self.timer-1


## main method
s=Schedule()
with open('process.csv') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            pid=int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            s.addP(pid,arrival,burst)
s.schedule()
