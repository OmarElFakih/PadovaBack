"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
#from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, House, Room, roomImage, houseImage, Booking_order, Admin
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:omar@localhost/example"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def hello():
    return "hello"

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200


@app.route('/addBooking', methods=['POST'])
def add_booking():
    body = request.json


    newBooking = Booking_order.add_order(
        body["checkIn"],
        body["checkOut"],
        body["email"],
        body["name"],
        body["number"],
        body["roomId"]
    )

    db.session.add(newBooking)
    try:
        db.session.commit()
        return jsonify(newBooking.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500

@app.route('/addHouse', methods=['POST'])
def add_house():
    body = request.json


    newHouse = House.add_house(
        body["name"],
        body["slug"],
        body["size"],
        body["featured"],
        body["description"],
        body["shortDescription"],
        body["location"],
        body["balconyTerrace"],
        body["garden"],
        body["kitchen"],
        body["pets"],
        body["parking"],
        body["wheelChair"],
        body["basement"],
        body["dishwasher"],
        body["washingMachine"],
        body["dryer"],
        body["ac"],
        body["heating"],
        body["wifi"],
        body["students"],
        body["workingProffessionals"],
        body["couples"],
        body["male"],
        body["female"],
        body["smoking"],
        body["instruments"]
    )

    db.session.add(newHouse)
    try:
        db.session.commit()
        return jsonify(newHouse.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500




@app.route('/addRoom', methods=['POST'])
def add_room():
    body = request.json


    newRoom = Room.add_room(
        body["name"],
        body["slug"],
        body["size"],
        body["beds"],
        body["privateBathroom"],
        body["price"],
        body["houseId"]
    )

    db.session.add(newRoom)
    try:
        db.session.commit()
        return jsonify(newRoom.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500


@app.route('/addHouseImg', methods=['POST'])
def add_himg():
    body = request.json
    new_himage = houseImage.add_house_image(
        body["url"],
        body["houseId"]
    )
    db.session.add(new_himage)
    
    try:
        db.session.commit()
        return jsonify(new_himage.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500


@app.route('/addRoomImg', methods=['POST'])
def add_rimg():
    body = request.json
    new_rimage = roomImage.add_room_image(
        body["url"],
        body["roomId"]
    )

    db.session.add(new_rimage)
    try:
        db.session.commit()
        return jsonify(new_rimage.serialize()), 201
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
            "response": f"{error.args}"
        }), 500


@app.route('/getBookings', methods=['GET'])
def get_bookings():
    bookings = Booking_order.query.all()
    bookings_serialize = list(map(lambda booking: booking.serialize(), bookings))
    return jsonify(bookings_serialize), 200

@app.route('/getHouses', methods=['GET'])
def get_houses():
    houses = House.query.all()
    houses_serialize = list(map(lambda house: house.serialize(), houses))
    return jsonify(houses_serialize), 200

@app.route('/getRooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    rooms_serialize = list(map(lambda room: room.serialize(), rooms))
    return jsonify(rooms_serialize), 200

@app.route('/getHouseImg', methods=['GET'])
def get_house_img():
    imgs = houseImage.query.all()
    img_serialize = list(map(lambda img: img.serialize(), imgs))
    return jsonify(img_serialize), 200

@app.route('/getRoomImg', methods=['GET'])
def get_room_img():
    imgs = roomImage.query.all()
    img_serialize = list(map(lambda img: img.serialize(), imgs))
    return jsonify(img_serialize), 200


@app.route('/updateHouse/<house_id>', methods=['PATCH'])
def update_house(house_id):
    body = request.json
    house = House.query.get(house_id)
    house.update(body)
    try:
        db.session.commit()
        return "house Updated" , 200
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
        "result": f"{error.args}"
        }), 500


@app.route('/updateRoom/<room_id>', methods=['PATCH'])
def update_room(room_id):
    body = request.json
    room = Room.query.get(room_id)
    room.update(body)
    try:
        db.session.commit()
        return "room updated" , 200
    except Exception as error:
        db.session.rollback()
        print(f"{error.args} {type(error)}")
        return jsonify({
        "result": f"{error.args}"
        }), 500



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run()
    #app.run(host='0.0.0.0', port=PORT, debug=False)
