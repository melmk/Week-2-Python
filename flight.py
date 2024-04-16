class Flight():
    # Creating object
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] # Starts with an empty list of passengers

    # Method that adds passengers to flight so long as there is room on the plane
    def addPassenger(self, name):
        if not self.openSeats():       # pythonic way of doing if self.openSeats == 0
            return False
        else:
            self.passengers.append(name)
            return True

    # Returns number of open seats remaining
    def openSeats(self):
        return self.capacity - len(self.passengers)

# Create the flight
flight = Flight(3)

# Create list of people
people = ["Harry", "Ron", "Hermione", "Draco"]

# Try to add each person to the flight
for person in people:
    success = flight.addPassenger(person)

    # Print messages depending on success of adding to flight
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No seats left for {person}")