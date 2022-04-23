
import requests
from pprint import pprint

URL = 'http://127.0.0.1:5000/vehicles/'

def get_vehicle(vehicle_id):
    response = requests.get(URL + str(vehicle_id))
    if response.status_code == 200:
        print('vehicle: ')
        pprint(response.json().get('vehicle'))
        return response.json().get('vehicle')[0]
    else: 
        print('something went wrong')


def update_vehicle(vehicle_data, vehicle_id):
    response = requests.put(URL + vehicle_id,json=vehicle_data)
    if response.status_code == 204:
        print('success')
    else:
        print('something went wrong')



if __name__ == '__main__':
    vehicle_id = input('type in the vehicle id: ')
    target_vehicle = get_vehicle(vehicle_id)
    color = input('enter a color:')
    license_plate = input('enter a license plate:')
    v_type = input('enter vehicle type (1 - 4):')
    owner_id = input('enter a owner id:')
    active = input('enter active (0 or 1):')
    
    if color:
        target_vehicle['color'] = color
    if license_plate:
        target_vehicle['license_plate'] = license_plate
    if v_type:
        target_vehicle['v_type'] = v_type
    if owner_id:
        target_vehicle['owner_id'] = owner_id
    if active:
        target_vehicle['active'] = active
    update_vehicle(target_vehicle, vehicle_id)
    option = input('would you like to see the updated vehicle? [y/N]: ')
    if option == 'y' or 'Y':
        get_vehicle(int(vehicle_id))
    