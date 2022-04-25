from time import strftime
from flask import (
    Flask,
    request
)
from datetime import datetime
from app.database import vehicle

VERSION = '1.0.0'
app = Flask(__name__)

# @app.get("/version")
# def get_version():
#     out = {
#         "server_time": datetime.now().strftime("%F %H:%M:%S"),
#         "version": VERSION
#     }
#     return out

from webbrowser import get
from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id" : result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result[3],
            "owner_id": result[4],
            "active": result[5],
        }
        out.append(result_dict)
    return out


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("color"),
        vehicle_dict.get("license_plate"),
        vehicle_dict.get("v_type"),
        vehicle_dict.get("owner_id"),
        vehicle_dict.get("active")
    )

    statement = """
        INSERT INTO vehicle (
            color,
            license_plate,
            v_type,
            owner_id,
            active
        ) VALUES (?, ?, ?, ?, ?)
    """

    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db()
    results = cursor.execute("SELECT * FROM vehicle WHERE active=1", ()).fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db()
    results = cursor.execute("SELECT * FROM vehicle WHERE id=?", (pk, )).fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, user_data):
    value_tuple = (
        user_data.get("color"),
        user_data.get("license_plate"),
        user_data.get("v_type"),
        user_data.get("owner_id"),
        user_data.get("active"),
        pk
    )
    statement = """
        UPDATE vehicle 
        SET color=?,
        license_plate=?,
        v_type=?,
        owner_id=?,
        active=?
        WHERE id=?
    """
    cursor=get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db()
    statement = """
        UPDATE vehicle 
        SET active=0 
        WHERE id=?
    """
    cursor.execute(statement, (pk, ))
    cursor.commit()
    cursor.close()
