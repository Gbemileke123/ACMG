class Aircraft:
    def __init__(self, capacity, aircraftNo, types, name):
        self.capacity=capacity
        self.aircraftNo = aircraftNo
        self.types=types
        self.name=name

    def __str__(self):
        return f"{self.capacity}\t{self.aircraftNo}\t{self.types}\t{self.name}"

    def parse(line: str):
        capacity,aircraftNo,types,name = line.split("\t")
        capacity = int(capacity)
        return Aircraft(capacity,aircraftNo,types,name)
