import json

def get_data():
    try:
        with open('users.json') as file:
            users: list = json.load(file)
            return users
    except(FileNotFoundError, json.JSONDecodeError):
        with open('users.json', 'w') as file:
            json.dump([], file, indent=4)
            return []

class User:
    def __init__(self, first_name, last_name, email, username, birth_date, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.birth_date = birth_date
        self.__password = password

    def append_to_json(self):
        if not self.user_exists():
            user = {
                'id': 1 if len(get_data()) == 0 else get_data()[-1]['id'] + 1,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'username': self.username,
                'birth_date': self.birth_date,
                'password': self.__password
            }
            users: list = get_data()
            users.append(user)
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)
                print("Successfully registered")
                return True
        else:
            print("User already exists")
            return False

    def user_exists(self):
        users: list = get_data()
        for user in users:
            if user['username'] == self.username or user['email'] == self.email:
                return True
        return False

