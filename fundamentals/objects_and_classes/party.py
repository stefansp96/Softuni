class Party:
    def __init__(self):
        self.party_people = []

    def add_person(self, name):
        self.party_people.append(name)

    def party_info(self):
        going = ', '.join(self.party_people)
        total = len(self.party_people)
        result = f'Going: {going}\nTotal: {total}'
        return result


party = Party()

while True:
    person = input()

    if person == 'End':
        break
    party.add_person(person)

print(party.party_info())
