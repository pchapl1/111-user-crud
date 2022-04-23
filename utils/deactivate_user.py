
import requests

URL = 'http://127.0.0.1:5000/users/del/'

def delete_user(pk):

    response = requests.delete(URL+str(pk))

    if response.status_code == 204:
        print('success')
    else: 
        print('something went wrong')


if __name__ == '__main__':
    pk = input('enter user id:')

    delete_user(pk)