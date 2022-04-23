from time import strftime
from flask import (
    Flask,
    request
)
from datetime import datetime
from app.database import user, vehicle

VERSION = '1.0.0'
app = Flask(__name__)

@app.get("/version")
def get_version():
    out = {
        "server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out

@app.get("/users")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok", 
        "message": "success",
        "users": user_list
    }
    return resp

@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status":"ok",
        "message":"success",
        "user": target_user
    }
    if target_user:
        resp['user'] = target_user
        return resp
    else:
        resp['status'] = 'error'
        resp['message'] = 'User not found'
        return resp, 404


@app.post("/users/")
def create_user():
    user_data = request.json
    user.insert(user_data)
    return "", 204

@app.put("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204


@app.delete("/users/del/<int:pk>")
def delete_user(pk):
    user.deactivate(pk)
    return "", 204


# ===================================Vehicles===================================

@app.get("/vehicles")
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    resp = {
        "status": "ok", 
        "message": "success",
        "vehicles": vehicle_list
    }
    return resp

@app.get("/vehicles/<int:pk>")
def get_vehicle_by_id(pk):
    target_vehicle = vehicle.select_by_id(pk)
    resp = {
        "status":"ok",
        "message":"success",
        "vehicle": target_vehicle
    }
    if target_vehicle:
        resp['user'] = target_vehicle
        return resp
    else:
        resp['status'] = 'error'
        resp['message'] = 'vehicle not found'
        return resp, 404


@app.post("/vehicles/")
def create_vehicle():
    vehicle_data = request.json
    vehicle.insert(vehicle_data)
    return "", 204

@app.put("/vehicles/<int:pk>")
def update_vehicle(pk):
    vehicle_data = request.json
    vehicle.update(pk, vehicle_data)
    return "", 204


@app.delete("/vehicles/del/<int:pk>")
def delete_vehicles(pk):
    vehicle.deactivate(pk)
    return "", 204




