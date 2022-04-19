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
    return results


def select_by_id(pk):
    cursor = get_db()
    results = cursor.execute("SELECT * FROM user WHERE id=?", (pk, )).fetchall()
    cursor.close()
    return results


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
    cursor.execute("DELETE from user WHERE id=?", (pk, ))
    cursor.commit()
    cursor.close()
