from app.database import get_db


def get_all_user_vehicles():
    statement = """
        SELECT  user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.color,
            vehicle.license_plate,
            vehicle_type.description
        FROM user 
        INNER JOIN vehicle ON user.id = vehicle.owner_id
        INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;
    """

    cursor = get_db()
    results = cursor.execute(statement, ()).fetchall()
    cursor.close()
    out = []
    for result in results:
        temp_dict = {

            "last_name" : result[0],
            "first_name" : result[1],
            "hobbies" : result[2],
            "user_active" : result[3],
            "vehicle_color" : result[4],
            "vehicle_license_plate" : result[5],
            "vehicle_description" : result[6]
        }
        out.append(temp_dict)
    return out

# def get_vehicles_for_user_by_user_id(user_id):
#     statement = """
#         SELECT  user.last_name,
#             user.first_name,
#             user.hobbies,
#             user.active,
#             vehicle.color,
#             vehicle.license_plate,
#             vehicle_type.description
#         FROM user 
#         INNER JOIN vehicle ON user.id = vehicle.owner_id
#         INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;
#     """

#     cursor = get_db()
#     cursor.execute(statement, )


if "__name__" == "__main__":
    get_all_user_vehicles()