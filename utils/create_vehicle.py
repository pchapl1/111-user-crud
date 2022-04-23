from venv import create
import requests

URL = 'http://127.0.0.1:5000/vehicles/'


def create_vehicle(color, license_plate, v_type, owner_id, active):
    vehicle_data = {}
    vehicle_data['color'] = color
    vehicle_data['license_plate'] = license_plate
    vehicle_data['v_type'] = v_type
    vehicle_data['owner_id'] = owner_id
    vehicle_data['active'] = active
    response = requests.post(URL, json=vehicle_data)
    if response.status_code == 204:
        print('success')
    else:
        print('something went wrong')


if __name__ == '__main__':
    color = input('enter a color:')
    license_plate = input('enter a license plate:')
    v_type = input('enter vehicle type (1 - 4):')
    owner_id = input('enter a owner id :')
    active = input('enter active (0 or 1):')
    create_vehicle(color, license_plate, v_type, owner_id, active)
