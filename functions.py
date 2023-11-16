from user import User, get_data
import hashlib

def registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    username = input("Enter your username: ")
    birth_date = input("Enter your birth date(dd-mm-yyyy): ")
    password = sha256_hash(input("Enter your password: "))

    user = User(first_name, last_name, email, username, birth_date, password)
    return user.append_to_json()

def login():
    users: list = get_data()
    email = input("Enter your email: ")
    password = sha256_hash(input("Enter your password: "))

    for user in users:
        if user['email'] == email:
            if user['password'] == password:
                return user['id']
            else:
                print('Incorrect password')
                return 0

    print('There no such user')
    return 0

def sha256_hash(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash_object = hashlib.sha256()
    sha256_hash_object.update(encoded_string)
    hashed_string = sha256_hash_object.hexdigest()

    return hashed_string