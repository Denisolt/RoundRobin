class Process:

    # name, arrival time, burst time
    def __init__(self, n, at, bt):
        self.name = n
        self.arrive = at
        self.burst = bt

    def __str__(self):
        return '[name: {:3s}] [arrival time: {:3d}] [burst time: {:3d}]'.format(self.name, self.arrive, self.burst)