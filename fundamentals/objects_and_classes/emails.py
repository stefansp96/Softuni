class Email:
    def __init__(self, sender, receiver, content,):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        result = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        return result


emails = []


while True:
    some_data = input().split()
    if some_data[0] == 'Stop':
        break

    sender, receiver, content = some_data
    some_email = Email(sender, receiver, content)
    emails.append(some_email)

indices = [int(num) for num in input().split(', ')]

for index in indices:
    if 0 <= index <= len(emails):
        emails[index].send()

for current_email in emails:
    print(current_email.get_info())
