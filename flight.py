class Flight():
    def __init__(self, capacity):
        self.model = 'BOEING350'
        self.capacity= capacity
        self.people= []
    def seatLeft(self):
        return self.capacity - len(self.people)
    def addToFlight(self, name):
        if not self.seatLeft():
            return False
        else:
            self.people.append(name)
            return True
    def closingMesage(self):
        return f'Thank you for choosing {self.model} today. We appreciate your trust. Safe travels! If you need assistance, contact our team. Have a great day! #FlyWithUs 🎌✈✈'

flight = Flight(8)

passengers = ['Mary', 'Joan', 'Kingsley', 'Martha','Mary', 'Joan', 'Kingsley', 'Martha','Mary']

for passenger in passengers:
    if flight.addToFlight(passenger):
        print(f'Congratulations {passenger} you have successfully been onboarded on {flight.model} ✅')
        print()
    else:
        print(f'Oh sorry {passenger}, our {flight.model} is fully booked at the moment kindly wait for the next available flight. Thank you 😔')
        print()

print(flight.closingMesage())
      
    