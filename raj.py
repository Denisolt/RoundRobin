import queue,csv

MAX_CLOCK = 100


class Process:

    # name, arrival time, burst time
    def __init__(self, n, at, bt):
        self.name = n
        self.arrive = at
        self.burst = bt

    def __str__(self):
        return '[name: {:3s}] [arrival time: {:3d}] [burst time: {:3d}]'.format(self.name, self.arrive, self.burst)


class Event:

    def __init__(self, n, s, e):
        self.name = n
        self.start = s
        self.end = e

    def __str__(self):
        return '[process: {:3s}] [start: {:3d}] [end: {:3d}]'.format(self.name, self.start, self.end)


class Simulator:

    # time quantum, processes
    def __init__(self, tq=2):
        self.quantum = tq
        self.procs = []
        self.clock = 0
        self.queue = queue()
        self.events = []
        self.timer = 0

    # time quantum
    def quantize(self, tq=2):
        self.quantum = tq

    # create procces and add to list
    def process(self, pname, pat, pbt):
        self.procs.append(Process(pname, pat, pbt))

    # create process from csv ';' file and add to list
    def load(self, path):
        with open(path) as file:
            content = file.read()
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                data = line.strip().split(';')
                n = data[0].strip()
                at = int(data[1].strip())
                bt = int(data[2].strip())
                self.process(n, at, bt)

    # listen for arriving
    def catch(self):
        temp = []   # to store enqueued processed to be removed from list
        for proc in self.procs:
            if proc.arrive == self.clock:
                self.queue.put(proc)
                temp.append(proc)
        for proc in temp:
            self.procs.remove(proc)

    def run(self):
        proc = self.queue.get()
        complete = False
        if proc.burst > self.quantum:
            time = self.quantum
        else:
            time = proc.burst
            complete = True
        event = Event(proc.name, self.timer, self.timer + time)
        self.events.append(event)
        self.timer += time
        if not complete:
            proc.burst -= time
            self.queue.put(proc)

    def schedule(self):
        while self.clock < MAX_CLOCK:
            self.catch()
            if not self.queue.empty():
                self.run()
            self.clock += 1