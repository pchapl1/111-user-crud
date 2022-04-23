from venv import create
import requests

URL = 'http://127.0.0.1:5000/users/'
# SAMPLE_USER = {
#     'first_name' : 'bill',
#     'last_name' : 'hader',
#     'hobbies' : 'comedy'
# }

def create_user(first_name, last_name, hobbies):
    user_data = {}
    user_data['first_name'] = first_name
    user_data['last_name'] = last_name
    user_data['hobbies'] = hobbies
    response = requests.post(URL, json=user_data)
    if response.status_code == 204:
        print('success')
    else:
        print('something went wrong')


if __name__ == '__main__':
    first_name = input('enter a first name:')
    last_name = input('enter a last name:')
    hobbies = input('enter hobbies:')
    create_user(first_name, last_name, hobbies)