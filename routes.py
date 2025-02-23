from flask import Blueprint, render_template, session, redirect, url_for, flash, request,send_from_directory,jsonify
from flask_login import login_required, current_user
from data import gym_exercises, sports, food_items as food_data
from models import db, User, AccessRequest, FoodLog, GymLog, Report
from datetime import datetime
import hashlib
import time
from sqlalchemy.sql import func
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename

routes_bp = Blueprint('routes', __name__)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def create_genesis_block(self, user_email):
        genesis_block = Block(0, "0", time.time(), user_email)
        self.chain.append(genesis_block)
        return genesis_block.hash  # This hash is the user's "Vaibhav code"

@routes_bp.route('/dashboard')
@login_required
def dashboard():
    # Ensure user is authenticated
    if not current_user.is_authenticated:
        flash('Please log in first.', 'warning')
        return redirect(url_for('auth.login'))

    # Fetch pending received requests
    received_requests = db.session.query(AccessRequest).filter_by(
        recipient_id=current_user.id, status="Pending"
    ).all()

    # Fetch accepted access requests (granted access)
    granted_access = db.session.query(AccessRequest).filter_by(
        requester_id=current_user.id, status="Accepted"
    ).all()

    return render_template('dashboard.html', user=current_user, received_requests=received_requests, granted_access=granted_access)

# Request Access to Medical Data
@routes_bp.route('/request_access', methods=['POST'])
@login_required
def request_access():
    full_name = request.form['full_name']
    identifier_type = request.form['identifier_type']
    identifier_value = request.form['identifier_value']

    print(f"Received request: Full Name={full_name}, Type={identifier_type}, Value={identifier_value}")

    # Find recipient based on selected identifier type
    recipient_query = None
    if identifier_type == "email":
        recipient_query = db.session.query(User).filter_by(email=identifier_value).first()
    elif identifier_type in ["PAN", "aadhaar"]:
        recipient_query = db.session.query(User).filter_by(id_card=identifier_value).first()
    elif identifier_type == "phone":
        recipient_query = db.session.query(User).filter_by(phone=identifier_value).first()

    recipient = recipient_query if recipient_query else None

    if not recipient:
        flash('User not found. Please check the details and try again.', 'error')
        print("User not found")
        return redirect(url_for('routes.dashboard'))

    # Check if request already exists
    existing_request = db.session.query(AccessRequest).filter_by(
        requester_id=current_user.id,
        recipient_id=recipient.id,
        status="Pending"
    ).first()

    if existing_request:
        flash('You have already sent a request to this user.', 'warning')
        print("Duplicate request detected")
        return redirect(url_for('routes.dashboard'))

    # Create a new access request
    new_request = AccessRequest(
        requester_id=current_user.id,
        recipient_id=recipient.id,
        full_name=full_name,
        identifier_type=identifier_type,
        identifier_value=identifier_value,
        status="Pending"
    )

    db.session.add(new_request)
    db.session.commit()

    flash('Access request sent successfully!', 'success')
    print("Access request successfully added to database")

    return redirect(url_for('routes.dashboard'))
# Accept Access Request
@routes_bp.route('/accept_request/<int:request_id>', methods=['POST'])
@login_required
def accept_request(request_id):
    access_request = AccessRequest.query.get(request_id)

    if not access_request or access_request.recipient_id != current_user.id:
        flash("Invalid request!", "error")
        return redirect(url_for('routes.dashboard'))

    access_request.status = "Accepted"
    db.session.commit()

    flash("Access granted successfully!", "success")
    return redirect(url_for('routes.dashboard'))


# Reject Access Request
@routes_bp.route('/reject_request/<int:request_id>', methods=['POST'])
@login_required
def reject_request(request_id):
    access_request = AccessRequest.query.get(request_id)

    if not access_request or access_request.recipient_id != current_user.id:
        flash("Invalid request!", "error")
        return redirect(url_for('routes.dashboard'))

    access_request.status = "Rejected"
    db.session.commit()

    flash("Access request declined.", "info")
    return redirect(url_for('routes.dashboard'))

@routes_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    return render_template('index.html')

@routes_bp.route("/calories", methods=["GET", "POST"])
def calorie_tracker():
    if request.method == "POST":
        food_item = request.form.get("food_item")
        quantity = float(request.form.get("quantity", 0))

        if food_item in food_data:
            data = food_data[food_item]
            calories = (data["calories"] * quantity) / 100
            protein = (data["protein"] * quantity) / 100
            carbs = (data["carbs"] * quantity) / 100
            fat = (data["fats"] * quantity) / 100

            new_entry = FoodLog(
                user_id=current_user.id,
                food_item=food_item,
                quantity=quantity,
                calories=calories,
                protein=protein,
                carbs=carbs,
                fat=fat,
                date_logged=datetime.utcnow()
            )
            db.session.add(new_entry)
            db.session.commit()

        return redirect(url_for("routes.calorie_tracker"))

    # Fetch today's total intake
    today = datetime.utcnow().date()
    today_entries = FoodLog.query.filter_by(user_id=current_user.id).filter(func.date(FoodLog.date_logged) == today).all()

    total_calories = sum(entry.calories for entry in today_entries)
    total_protein = sum(entry.protein for entry in today_entries)
    total_carbs = sum(entry.carbs for entry in today_entries)
    total_fat = sum(entry.fat for entry in today_entries)

    return render_template(
        "calories.html",
        food_data=food_data,
        entries=FoodLog.query.filter_by(user_id=current_user.id).all(),
        total_calories=total_calories,
        total_protein=total_protein,
        total_carbs=total_carbs,
        total_fat=total_fat
    )

@routes_bp.route('/gym', methods=['GET', 'POST'])
def gym_tracker():
    if request.method == 'POST':
        name = request.form.get('name')
        reps = request.form.get('reps')
        sets = request.form.get('sets')
        hours = request.form.get('hours')
        date_logged = datetime.now()

        # Convert inputs safely
        try:
            reps = int(reps) if reps and reps.strip() else 0
        except ValueError:
            reps = 0
        try:
            sets = int(sets) if sets and sets.strip() else 0
        except ValueError:
            sets = 0
        try:
            hours = float(hours) if hours and hours.strip() else 0.0
        except ValueError:
            hours = 0.0

        # Calculate calories burned
        calories_burned = 0.0
        if hours > 0:
            calories_burned = round(hours * 300, 2)
        elif reps > 0 and sets > 0:
            calories_burned = round(reps * sets * 0.5, 2)

        new_log = GymLog(
                user_id=current_user.id,
            exercise_type=name, 
            name=name, 
            reps=reps if reps > 0 else None, 
            sets=sets if sets > 0 else None, 
            hours=hours if hours > 0 else None, 
            calories_burned=calories_burned, 
            date_logged=date_logged
        )
        db.session.add(new_log)
        db.session.commit()
        return redirect(url_for('routes.gym_tracker'))

    logs = GymLog.query.filter_by(user_id=current_user.id).order_by(GymLog.date_logged.desc()).all()
    return render_template('gym_tracker.html', gym_exercises=gym_exercises, sports=sports, logs=logs)

@routes_bp.route('/user_data/<int:user_id>')
@login_required
def user_data(user_id):
    # Ensure the user exists
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    # Check if an accepted access request exists
    access_request = AccessRequest.query.filter_by(
        recipient_id=user_id,
        requester_id=current_user.id,
        status="Accepted"
    ).first()

    if not access_request:
        flash("You do not have permission to view this data.", "danger")
        return redirect(url_for("dashboard"))  # Redirect to dashboard or home page

    # Fetch logs if access is granted
    gym_logs = GymLog.query.filter_by(user_id=user_id).order_by(GymLog.date_logged.desc()).all()
    calorie_logs = FoodLog.query.filter_by(user_id=user_id).order_by(FoodLog.date_logged.desc()).all()

    reports = Report.query.filter_by(user_id=user_id).all()
    print(reports)

    return render_template("user_data.html", user=user, gym_logs=gym_logs, calorie_logs=calorie_logs, reports=reports, 
        gym_log=[log.to_dict() for log in gym_logs],
        calorie_log=[log.to_dict() for log in calorie_logs])


# Route to upload report
@routes_bp.route("/upload_report/<int:user_id>", methods=["POST"])
def upload_report(user_id):
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.referrer)

    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(request.referrer)

    if file and allowed_file(file.filename):
        original_filename = file.filename
        filename = secure_filename(f"{len(os.listdir("uploads")) + 1}_{original_filename}")
        file_path = os.path.join("uploads", filename)
        file.save(file_path)

        # Get logged-in user (example: fetching from session)
        uploader_id = session.get("user_id")  # ID of the logged-in user

        # Save report info in database
        new_report = Report(user_id=user_id, uploader_id=uploader_id, filename=filename, original_filename=original_filename)
        db.session.add(new_report)
        db.session.commit()

        flash("File uploaded successfully!")
    
    return redirect(request.referrer)

@routes_bp.route("/download/<filename>")
def download_report(filename):
    return send_from_directory("uploads", filename)

genai.configure(api_key="AIzaSyAbqca4OrkQlyFJFoZ5AiNTUf9pbYRzFnM")

@routes_bp.route('/generate_health_report/<int:user_id>', methods=['GET'])
def generate_health_report(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Fetch user health logs
    gym_logs = GymLog.query.filter_by(user_id=user.id).all()
    calorie_logs = FoodLog.query.filter_by(user_id=user.id).all()

    # Format logs
    gym_summary = "\n".join([f"{log.exercise_type}: {log.reps} reps x {log.sets} sets" for log in gym_logs]) if gym_logs else "No gym logs available"
    calorie_summary = "\n".join([f"{log.food_item}: {log.calories} kcal" for log in calorie_logs]) if calorie_logs else "No calorie logs available"

    # AI Prompt
    prompt = f"""
    You are a health expert. Analyze the given user data and generate Medical condition summary, potential risks, and lifestyle suggestions.

    **User Details:**
    - Name: {user.name}
    - Age: {user.age}
    - Height: {user.height} feet
    - Weight: {user.weight} kg
    - Blood Group: {user.blood_group}
    - Alcohol Consumption: {user.alcohol}
    - Smoking Habit: {user.smoking}

    **Health Logs:**
    - Gym Activities: {gym_summary}
    - Calorie Intake: {calorie_summary}

    Provide a structured response in 2-3 lines in **Markdown format**.
    """

    try:
        # Call Gemini AI
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        # Extract AI response
        health_report = response.text if response.text else "No response generated."

        return jsonify({"health_report": health_report})

    except Exception as e:
        return jsonify({"error": str(e)}), 500