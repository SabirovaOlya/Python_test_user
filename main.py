from functions import registration, login
from user import get_data

while True:
    print('1.Registration')
    if len(get_data()) != 0:
        print('2.Login')

    ans = int(input('Enter: '))
    user_id = 0

    if ans == 1:
        status = registration()
        if status:
            print("You have to login to enter to the system")
            user_id = login()
    if ans == 2:
        user_id = login()

    if user_id == 0:
        print('Try again')
    else:
        print(f'You entered to the system. {user_id}')
        break
