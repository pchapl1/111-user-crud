CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

INSERT INTO user (
    first_name, 
    last_name, 
    hobbies 
) VALUES (
    "Phil", 
    "Chaplin",
    "Scuba Diving"
);

INSERT INTO user (
    first_name, 
    last_name, 
    hobbies
) VALUES (
    "Michael", 
    "Scott",
    "Making Friends"
);

INSERT INTO user (
    first_name, 
    last_name, 
    hobbies 
) VALUES (
    "Bruce", 
    "Wayne",
    "Being a bat"
);


CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45),
    license_plate VARCHAR(45),
    v_type INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);


INSERT INTO vehicle_type (
    description VARCHAR(45)
) VALUES (
    "Car"
);
INSERT INTO vehicle_type (
    description
) VALUES (
    "Truck"
);
INSERT INTO vehicle_type (
    description
) VALUES (
    "SUV"
);
INSERT INTO vehicle_type (
    description
) VALUES (
    "Hatchback"
);

INSERT INTO vehicle_type (
    description
) VALUES (
    "Unicycle"
);



INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "red", 
    "78V89E", 
    "1", 
    "1"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "black", 
    "H53897", 
    "2", 
    "2"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "green", 
    "MKL852", 
    "3", 
    "3"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "red", 
    "64LL34", 
    "4", 
    "4"
);



SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.color,
        vehicle.license_plate,
        vehicle.v_type as vehicle_type
FROM user INNER JOIN vehicle
ON user.id = vehicle.owner_id;


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

