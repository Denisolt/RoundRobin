Simulation = Simulator()

with open('process.csv') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            pid=int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            sim.addProcess(pid,arrival,burst)

