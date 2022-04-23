
import requests
from pprint import pprint

URL = 'http://127.0.0.1:5000/users/'

def get_user(user_id):
    response = requests.get(URL + str(user_id))
    if response.status_code == 200:
        print('User: ')
        print(user_id)
        pprint(response.json().get('user'))
        return response.json().get('user')[0]
    else: 
        print('something went wrong')


def update_user(user_data, user_id):
    response = requests.put(URL + str(user_id),json=user_data)
    if response.status_code == 204:
        print('success')
    else:
        print('something went wrong')



if __name__ == '__main__':
    user_id = input('type in the user id: ')
    target_user = get_user(user_id)
    # print(target_user)
    first_name = input('enter a first name:')
    last_name = input('enter a last name:')
    hobbies = input('enter hobbies:')
    if first_name:
        target_user['first_name'] = first_name
    if last_name:
        target_user['last_name'] = last_name
    if hobbies:
        target_user['hobbies'] = hobbies
    update_user(target_user, user_id)
    option = input('would you like to see the updated user? [y/N]: ')
    if option == 'y' or 'Y':
        get_user(int(user_id))
    