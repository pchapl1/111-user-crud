from webbrowser import get
from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id" : result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4],
        }
        out.append(result_dict)
    return out


def insert(user_dict):
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )

    statement = """
        INSERT INTO user (
            first_name,
            last_name,
            hobbies
        ) VALUES (?, ?, ?)
    """

    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db()
    results = cursor.execute("SELECT * FROM user WHERE active=1", ()).fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db()
    results = cursor.execute("SELECT * FROM user WHERE id=?", (pk, )).fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """
        UPDATE user 
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """
    cursor=get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db()
    statement = """
        UPDATE user 
        SET active=0 
        WHERE id=?
    """
    cursor.execute(statement, (pk, ))
    cursor.commit()
    cursor.close()


def get_users_and_vehicles():
    cursor = get_db()
    output = []

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

    results = cursor.execute(statement).fetchall()
    cursor.close()
    for result in results:
        temp_dict = {
            'last_name': result[0],
            'first_name': result[1],
            'hobbies': result[2],
            'active': result[3],
            'v_color': result[4],
            'v_license_plate': result[5],
            'v_description': result[6],
        }
        output.append(temp_dict)
    # print(results)
    return output