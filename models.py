from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):  # Add UserMixin
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    alcohol = db.Column(db.String(10), nullable=False)
    smoking = db.Column(db.String(10), nullable=False)
    id_card = db.Column(db.String(50), unique=True, nullable=False)
    vaibhav_code = db.Column(db.String(64), unique=True, nullable=False)

class AccessRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    identifier_type = db.Column(db.String(20), nullable=False)  # Email, PAN, Aadhaar, Phone
    identifier_value = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Pending')  # Pending, Accepted, Rejected
    
    requester = db.relationship('User', foreign_keys=[requester_id])
    recipient = db.relationship('User', foreign_keys=[recipient_id])

class FoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # In grams
    calories = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
        return {
            "food_item": self.food_item,
            "calories": self.calories,
            "date_logged": self.date_logged.strftime("%Y-%m-%d")
        }

class GymLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_type = db.Column(db.String(50), nullable=False)  # 'Gym' or 'Sport'
    name = db.Column(db.String(100), nullable=False)  # Exercise or Sport name
    reps = db.Column(db.Integer, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    hours = db.Column(db.Float, nullable=True)  # For sports
    calories_burned = db.Column(db.Float, nullable=False)
    date_logged = db.Column(db.DateTime, nullable=False)



    def to_dict(self):
        return {
            "exercise_type": self.exercise_type,
            "calories_burned": self.calories_burned,
            "date_logged": self.date_logged.strftime("%Y-%m-%d")
        }

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique Report ID
    user_id = db.Column(db.Integer, nullable=False)  # ID of the user whose report this is
    uploader_id = db.Column(db.Integer, nullable=False)  # ID of the user who uploaded the report
    filename = db.Column(db.String(255), nullable=False)  # Stored file name
    original_filename = db.Column(db.String(255), nullable=False)  # Original file name
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the report was uploaded
