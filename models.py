from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime, timezone
from base64 import b64encode
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm import backref

db = SQLAlchemy()


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    size = db.Column(db.Float, nullable=False)
    featured = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)
    short_description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100),  nullable=False)
    #minimun_stay = db.Column(db.Integer, nullable=False)
    #facilities
    balcony_terrace = db.Column(db.Boolean, nullable=False)
    garden = db.Column(db.Boolean, nullable=False)
    kitchen = db.Column(db.Boolean, nullable=False)
    pets = db.Column(db.Boolean, nullable=False)
    parking = db.Column(db.Boolean, nullable=False)
    wheelchair = db.Column(db.Boolean, nullable=False)
    basement = db.Column(db.Boolean, nullable=False)
    #amenities
    dishwasher = db.Column(db.Boolean, nullable=False)
    washing_machine = db.Column(db.Boolean, nullable=False)
    dryer = db.Column(db.Boolean, nullable=False)
    ac = db.Column(db.Boolean, nullable=False)
    heating = db.Column(db.Boolean, nullable=False)
    wifi = db.Column(db.Boolean, nullable=False)
    #suitable for 
    students = db.Column(db.Boolean, nullable=False)
    working_proffesionals = db.Column(db.Boolean, nullable=False)
    couples = db.Column(db.Boolean, nullable=False)
    male = db.Column(db.Boolean, nullable=False)
    female = db.Column(db.Boolean, nullable=False)
    #house rules
    smoking = db.Column(db.String(50), nullable=False)
    instruments = db.Column(db.String(50), nullable=False)
    rooms = db.relationship("Room", backref="House", foreign_keys="Room.house_id")
    images = db.relationship("houseImage", backref="House", foreign_keys="houseImage.house_id")

    def __init__(self, name, slug, size, featured, description, short_description, location, balcony_terrace, garden, kitchen, pets, parking, wheelchair, basement, dishwasher, washing_machine, dryer, ac, heating, wifi, students, working_proffesionals, couples, male, female, smoking, instruments):
        self.name = name
        self.slug = slug
        self.size = size
        self.featured = featured
        self.description = description
        self.short_description = short_description
        self.location = location
        #self.minimun_stay = minimum_stay
        self.balcony_terrace = balcony_terrace
        self.garden = garden
        self.kitchen = kitchen
        self.pets = pets
        self.parking = parking
        self.wheelchair = wheelchair
        self.basement = basement
        self.dishwasher = dishwasher
        self.washing_machine = washing_machine
        self.dryer = dryer
        self.ac = ac
        self.heating = heating
        self.wifi = wifi
        self.students = students
        self.working_proffesionals = working_proffesionals
        self.couples = couples
        self.male = male
        self.female = female
        self.smoking = smoking
        self.instruments = instruments

    @classmethod
    def add_house(cls, name, slug, size, featured, description, short_description, location, balcony_terrace, garden, kitchen, pets, parking, wheelchair, basement, dishwasher, washing_machine, dryer, ac, heating, wifi, students, working_proffesionals, couples, male, female, smoking, instruments):
        new_house = cls(
            name,
            slug,
            size,
            featured,
            description,
            short_description,
            location,
            #minimum_stay,
            balcony_terrace,
            garden,
            kitchen,
            pets,
            parking,
            wheelchair,
            basement,
            dishwasher,
            washing_machine,
            dryer,
            ac,
            heating,
            wifi,
            students, 
            working_proffesionals, 
            couples, 
            male, 
            female, 
            smoking, 
            instruments
        )

        return new_house


    def update(self, dictionary):
        for (key, value) in dictionary.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return True

    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'slug':self.slug,
            'size': self.size,
            'featured': self.featured,
            'description': self.description,
            'shortDescription': self.short_description,
            'location': self.location,
            #'minimum_stay': self.minimun_stay
            'balconyTerrace': self.balcony_terrace,
            'garden': self.garden,
            'kitchen': self.kitchen,
            'pets': self.pets,
            'parking': self.parking,
            'wheelchair': self.wheelchair,
            'basement': self.basement,
            'dishwasher': self.dishwasher,
            'washing_machine': self.washing_machine,
            'dryer': self.dryer,
            'ac': self.ac,
            'heating': self.heating,
            'wifi': self.wifi,
            'students': self.students, 
            'workingProffesionals': self.working_proffesionals,
            'couples' :self.couples,
            'male' : self.male,
            'female' : self.female,
            'smoking' : self.smoking,
            'instruments': self.instruments
        }




class Room(db.Model): 
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), unique=True, nullable=False)
   slug = db.Column(db.String(50), unique=True, nullable=False)
   size = db.Column(db.Integer, nullable=False)
   beds = db.Column(db.Integer, nullable=False)
   private_bathroom = db.Column(db.Boolean, nullable=False)
   price = db.Column(db.Float, nullable=False)
   house_id = db.Column(db.Integer, db.ForeignKey("house.id"))

   booking_orders = db.relationship("Booking_order", backref="Room", foreign_keys="Booking_order.room_id")

   def __init__(self, name, slug, size, beds, private_bathroom, price, house_id):
       self.name = name
       self.slug = slug
       self.size = size
       self.beds = beds
       self.private_bathroom = private_bathroom
       self.price = price
       self.house_id = house_id


   @classmethod
   def add_room(cls, name, slug, size, beds, private_bathroom, price, house_id):
        new_room = cls(
           name, 
           slug,  
           size, 
           beds, 
           private_bathroom, 
           price, 
           house_id
        )

        return new_room


   def update(self, dictionary):
        for (key, value) in dictionary.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return True 

   def serialize(self):
        return{
            'id': self.id,
            'name': self.name, 
            'slug' : self.slug,
            'size' : self.size,
            'beds' : self.beds,
            'privateBathroom' : self.private_bathroom,
            'price' : self.price,
            'houseId': self.house_id
        }





class houseImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey("house.id"))

    def __init__(self, url, house_id):
        self.url = url
        self.house_id = house_id

    @classmethod
    def add_house_image(cls, url, house_id):
        new_house_image = cls(
            url,
            house_id
        )

        return new_house_image

    def serialize(self):
        return{
            'id': self.id,
            'url': self.url,
            'houseId': self.house_id
        }
        



class roomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))

    def __init__(self, url, room_id):
        self.url = url
        self.house_id = room_id

    @classmethod
    def add_room_image(cls, url, room_id):
        new_room_image = cls(
            url,
            room_id
        )

        return new_room_image


    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'roomId': self.room_id
        }




class Booking_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.DateTime(timezone=True), nullable=False)
    check_out_date = db.Column(db.DateTime(timezone=True), nullable=False)
    tennant_email = db.Column(db.String(50), nullable=False)
    tennant_name = db.Column(db.String(50), nullable=False)
    tennant_number = db.Column(db.String(50), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))


    def __init__(self, check_in_date, check_out_date, tennant_email, tennant_name, tennant_number, room_id): 
       self.check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
       self.check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
       self.tennant_email = tennant_email
       self.tennant_name = tennant_name
       self.tennant_number = tennant_number
       self.room_id = room_id

    @classmethod
    def add_order(cls, check_in_date, check_out_date, tennant_email, tennant_name, tennant_number, room_id):
        new_order = cls(
        check_in_date, 
        check_out_date, 
        tennant_email, 
        tennant_name, 
        tennant_number, 
        room_id)

        return new_order

    def serialize(self):
        return{
            'id': self.id,
            'checkInDate': self.check_in_date, 
            'checkOutDate': self.check_out_date, 
            'tennantEmail': self.tennant_email, 
            'tennantName': self.tennant_name, 
            'tennantNumber': self.tennant_number, 
            'roomId': self.room_id

        }
    
    



class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)
    salt = db.Column(db.String(16), nullable=False)
    status = db.Column(db.Boolean(), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.salt = b64encode(os.urandom(4)).decode("utf-8")
        self.set_password(password)
        self.status = True



    def set_password(self, password):
        self.password_hash = generate_password_hash(f"{password}{self.salt}")


    def check_password(self, password):
        return check_password_hash(self.password_hash, f"{password}{self.salt}")
    
    @classmethod
    def register(cls, name, password):
        new_admin = cls(
            name,
            password
        )

        return new_admin


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


        