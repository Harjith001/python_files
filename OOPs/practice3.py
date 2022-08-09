class Person:

    def __init__(self, first_name, last_name,login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'First Name : {self.first_name}')
        print(f'Last Name : {self.last_name}')

    def greetings(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Person('Harjith','LRS')
user2 = Person('Gokul','Sangeeth')
user3 = Person('Harishaker','Menon')

user1.describe_user()
user1.greetings()
user2.describe_user()
user2.greetings()
user3.describe_user()
user3.greetings()

for i in range(5):
    user1.increment_login_attempts()
print(f'{user1.first_name} login attempts = {user1.login_attempts}')
user1.reset_login_attempts()
print(f'{user1.first_name} login attempts = {user1.login_attempts}')