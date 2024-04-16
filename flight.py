class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] # Starts with an empty list of passengers

    def addPassenger(self, name):
        if not self.openSeats():       # pythonic way of doing if self.openSeats == 0
            return False
        else:
            self.passengers.append(name)
            return True

    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Draco"]

for person in people:
    success = flight.addPassenger(person)

    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No seats left for {person}")