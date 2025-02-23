food_items = {
    "Apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fats": 0.3, "micronutrients": {"vitamin_c": 14, "potassium": 195}},
    "Banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fats": 0.4, "micronutrients": {"vitamin_c": 10, "potassium": 422}},
    "Orange": {"calories": 62, "protein": 1.2, "carbs": 15, "fats": 0.2, "micronutrients": {"vitamin_c": 70, "potassium": 237}},
    "Strawberries": {"calories": 49, "protein": 1, "carbs": 12, "fats": 0.5, "micronutrients": {"vitamin_c": 89, "manganese": 0.6}},
    "Blueberries": {"calories": 84, "protein": 1.1, "carbs": 21, "fats": 0.5, "micronutrients": {"vitamin_c": 14, "vitamin_k": 29}},
    "Grapes": {"calories": 69, "protein": 0.7, "carbs": 18, "fats": 0.2, "micronutrients": {"vitamin_c": 4, "vitamin_k": 14}},
    "Watermelon": {"calories": 30, "protein": 0.6, "carbs": 8, "fats": 0.2, "micronutrients": {"vitamin_c": 12, "vitamin_a": 569}},
    "Avocado": {"calories": 234, "protein": 2.9, "carbs": 12, "fats": 21, "micronutrients": {"vitamin_k": 26, "folate": 20}},
    "Broccoli": {"calories": 55, "protein": 4.3, "carbs": 11, "fats": 0.6, "micronutrients": {"vitamin_c": 135, "vitamin_k": 116}},
    "Spinach": {"calories": 23, "protein": 2.9, "carbs": 3.6, "fats": 0.4, "micronutrients": {"vitamin_a": 188, "vitamin_k": 145}},
    "Carrot": {"calories": 41, "protein": 0.9, "carbs": 10, "fats": 0.2, "micronutrients": {"vitamin_a": 334, "vitamin_k": 13}},
    "Sweet Potato": {"calories": 90, "protein": 2, "carbs": 21, "fats": 0.2, "micronutrients": {"vitamin_a": 384, "vitamin_c": 22}},
    "Potato": {"calories": 130, "protein": 2.5, "carbs": 30, "fats": 0.1, "micronutrients": {"vitamin_c": 27, "potassium": 620}},
    "Tomato": {"calories": 18, "protein": 0.9, "carbs": 3.9, "fats": 0.2, "micronutrients": {"vitamin_c": 17, "vitamin_a": 25}},
    "Cucumber": {"calories": 16, "protein": 0.7, "carbs": 3.6, "fats": 0.1, "micronutrients": {"vitamin_k": 16, "potassium": 152}},
    "Bell Pepper": {"calories": 20, "protein": 0.9, "carbs": 4.6, "fats": 0.2, "micronutrients": {"vitamin_c": 127, "vitamin_a": 313}},
    "Lettuce": {"calories": 5, "protein": 0.5, "carbs": 1, "fats": 0.1, "micronutrients": {"vitamin_a": 148, "vitamin_k": 102}},
    "Onion": {"calories": 40, "protein": 1.1, "carbs": 9, "fats": 0.1, "micronutrients": {"vitamin_c": 8, "folate": 19}},
    "Garlic": {"calories": 4, "protein": 0.2, "carbs": 1, "fats": 0, "micronutrients": {"vitamin_c": 1, "manganese": 0.1}},
    "Egg": {"calories": 70, "protein": 6, "carbs": 0.6, "fats": 5, "micronutrients": {"vitamin_d": 44, "selenium": 15}},
    "Chicken Breast": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6, "micronutrients": {"niacin": 14, "selenium": 26}},
    "Salmon": {"calories": 206, "protein": 22, "carbs": 0, "fats": 13, "micronutrients": {"vitamin_d": 570, "omega_3": 2.3}},
    "Tuna": {"calories": 132, "protein": 29, "carbs": 0, "fats": 1, "micronutrients": {"vitamin_d": 2, "selenium": 108}},
    "Shrimp": {"calories": 99, "protein": 24, "carbs": 0.2, "fats": 0.3, "micronutrients": {"vitamin_b12": 24, "selenium": 48}},
    "Beef Steak": {"calories": 250, "protein": 26, "carbs": 0, "fats": 15, "micronutrients": {"iron": 2.6, "zinc": 6.3}},
    "Pork Chop": {"calories": 242, "protein": 27, "carbs": 0, "fats": 14, "micronutrients": {"thiamine": 0.6, "selenium": 38}},
    "Turkey Breast": {"calories": 135, "protein": 29, "carbs": 0, "fats": 1, "micronutrients": {"niacin": 10, "selenium": 27}},
    "Lamb Chop": {"calories": 250, "protein": 25, "carbs": 0, "fats": 16, "micronutrients": {"vitamin_b12": 2.6, "zinc": 4.2}},
    "Tofu": {"calories": 76, "protein": 8, "carbs": 2, "fats": 4, "micronutrients": {"calcium": 350, "iron": 1.6}},
    "Tempeh": {"calories": 193, "protein": 19, "carbs": 9, "fats": 11, "micronutrients": {"calcium": 111, "iron": 2.7}},
    "Lentils": {"calories": 230, "protein": 18, "carbs": 40, "fats": 0.8, "micronutrients": {"folate": 90, "iron": 6.6}},
    "Chickpeas": {"calories": 269, "protein": 14, "carbs": 45, "fats": 4, "micronutrients": {"folate": 282, "manganese": 1.7}},
    "Black Beans": {"calories": 227, "protein": 15, "carbs": 41, "fats": 0.9, "micronutrients": {"folate": 256, "iron": 3.6}},
    "Quinoa": {"calories": 222, "protein": 8, "carbs": 39, "fats": 3.6, "micronutrients": {"magnesium": 118, "manganese": 1.2}},
    "Brown Rice": {"calories": 216, "protein": 5, "carbs": 45, "fats": 1.8, "micronutrients": {"magnesium": 84, "selenium": 19}},
    "Oats": {"calories": 389, "protein": 17, "carbs": 66, "fats": 7, "micronutrients": {"manganese": 4.9, "phosphorus": 523}},
    "Whole Wheat Bread": {"calories": 247, "protein": 13, "carbs": 41, "fats": 3.4, "micronutrients": {"fiber": 7, "iron": 2.5}},
    "Almonds": {"calories": 579, "protein": 21, "carbs": 22, "fats": 50, "micronutrients": {"vitamin_e": 26, "magnesium": 270}},
    "Walnuts": {"calories": 654, "protein": 15, "carbs": 14, "fats": 65, "micronutrients": {"omega_3": 9, "manganese": 3.4}},
    "Peanuts": {"calories": 567, "protein": 26, "carbs": 16, "fats": 49, "micronutrients": {"niacin": 12, "folate": 240}},
    "Cashews": {"calories": 553, "protein": 18, "carbs": 30, "fats": 44, "micronutrients": {"magnesium": 292, "iron": 6.7}},
    "Pistachios": {"calories": 562, "protein": 20, "carbs": 28, "fats": 45, "micronutrients": {"vitamin_b6": 1.7, "potassium": 1025}},
    "Chia Seeds": {"calories": 486, "protein": 17, "carbs": 42, "fats": 31, "micronutrients": {"omega_3": 17.8, "calcium": 631}},
    "Flaxseeds": {"calories": 534, "protein": 18, "carbs": 29, "fats": 42, "micronutrients": {"omega_3": 22.8, "fiber": 27}},
    "Sunflower Seeds": {"calories": 584, "protein": 21, "carbs": 20, "fats": 51, "micronutrients": {"vitamin_e": 35, "selenium": 53}},
    "Pumpkin Seeds": {"calories": 559, "protein": 30, "carbs": 10, "fats": 49, "micronutrients": {"magnesium": 592, "zinc": 7.8}},
    "Milk": {"calories": 103, "protein": 8, "carbs": 12, "fats": 2.4, "micronutrients": {"calcium": 300, "vitamin_d": 2.7}},
    "Yogurt": {"calories": 59, "protein": 10, "carbs": 3.6, "fats": 0.4, "micronutrients": {"calcium": 110, "vitamin_b12": 0.6}},
    "Cheese (Cheddar)": {"calories": 402, "protein": 25, "carbs": 1.3, "fats": 33, "micronutrients": {"calcium": 721, "vitamin_a": 265}},
    "Cottage Cheese": {"calories": 98, "protein": 11, "carbs": 3.4, "fats": 4.3, "micronutrients": {"calcium": 83, "selenium": 20}},
    "Butter": {"calories": 717, "protein": 0.9, "carbs": 0.1, "fats": 81, "micronutrients": {"vitamin_a": 684, "vitamin_e": 2.3}},
    "Olive Oil": {"calories": 884, "protein": 0, "carbs": 0, "fats": 100, "micronutrients": {"vitamin_e": 14, "vitamin_k": 60}},
    "Coconut Oil": {"calories": 862, "protein": 0, "carbs": 0, "fats": 100, "micronutrients": {"vitamin_e": 0.1, "vitamin_k": 0.6}},
    "Almond Milk": {"calories": 39, "protein": 1, "carbs": 3.4, "fats": 2.5, "micronutrients": {"calcium": 516, "vitamin_e": 49}},
    "Soy Milk": {"calories": 54, "protein": 3.3, "carbs": 6, "fats": 1.8, "micronutrients": {"calcium": 300, "vitamin_d": 2.7}},
    "Dark Chocolate": {"calories": 546, "protein": 4.9, "carbs": 61, "fats": 31, "micronutrients": {"iron": 11, "magnesium": 228}},
    "Milk Chocolate": {"calories": 535, "protein": 7.7, "carbs": 59, "fats": 30, "micronutrients": {"calcium": 189, "iron": 2.4}},
    "Honey": {"calories": 304, "protein": 0.3, "carbs": 82, "fats": 0, "micronutrients": {"vitamin_c": 0.5, "calcium": 6}},
    "Maple Syrup": {"calories": 260, "protein": 0, "carbs": 67, "fats": 0.1, "micronutrients": {"manganese": 2.6, "zinc": 0.1}},
    "White Rice": {"calories": 205, "protein": 4.3, "carbs": 45, "fats": 0.4, "micronutrients": {"thiamine": 0.1, "folate": 4}},
    "Pasta": {"calories": 131, "protein": 5, "carbs": 25, "fats": 1.1, "micronutrients": {"iron": 1.3, "folate": 18}},
    "Whole Wheat Pasta": {"calories": 174, "protein": 7.5, "carbs": 37, "fats": 0.8, "micronutrients": {"fiber": 6, "iron": 2.1}},
    "Bread (White)": {"calories": 265, "protein": 9, "carbs": 49, "fats": 3.2, "micronutrients": {"calcium": 151, "iron": 3.6}},
    "Bagel": {"calories": 245, "protein": 9, "carbs": 48, "fats": 1.5, "micronutrients": {"calcium": 19, "iron": 2.6}},
    "Croissant": {"calories": 231, "protein": 5, "carbs": 26, "fats": 12, "micronutrients": {"calcium": 37, "vitamin_a": 82}},
    "Pancakes": {"calories": 227, "protein": 6, "carbs": 38, "fats": 5, "micronutrients": {"calcium": 180, "iron": 1.8}},
    "Waffles": {"calories": 218, "protein": 6, "carbs": 29, "fats": 9, "micronutrients": {"calcium": 255, "iron": 1.9}},
    "Granola": {"calories": 471, "protein": 10, "carbs": 64, "fats": 20, "micronutrients": {"fiber": 5, "iron": 3.6}},
    "Popcorn": {"calories": 31, "protein": 1, "carbs": 6, "fats": 0.4, "micronutrients": {"fiber": 1, "magnesium": 11}},
    "Potato Chips": {"calories": 536, "protein": 7, "carbs": 53, "fats": 34, "micronutrients": {"vitamin_c": 12, "potassium": 1275}},
    "French Fries": {"calories": 365, "protein": 4, "carbs": 63, "fats": 14, "micronutrients": {"vitamin_c": 9, "potassium": 573}},
    "Pizza (Cheese)": {"calories": 285, "protein": 12, "carbs": 36, "fats": 10, "micronutrients": {"calcium": 220, "iron": 2.5}},
    "Burger (Beef)": {"calories": 354, "protein": 20, "carbs": 29, "fats": 16, "micronutrients": {"iron": 3.6, "zinc": 4.3}},
    "Hot Dog": {"calories": 290, "protein": 10, "carbs": 18, "fats": 18, "micronutrients": {"vitamin_b12": 0.6, "zinc": 1.5}},
}

gym_exercises = [
    "Bench Press", "Incline Bench Press", "Decline Bench Press", "Overhead Shoulder Press", 
    "Arnold Press", "Lateral Raises", "Front Raises", "Bent-Over Rear Delt Flys", "Push-Ups", 
    "Pull-Ups", "Chin-Ups", "Lat Pulldown", "Bent-Over Rows", "T-Bar Rows", "Seated Cable Rows", 
    "Face Pulls", "Bicep Curls", "Hammer Curls", "Preacher Curls", "Tricep Dips", 
    "Tricep Pushdowns", "Skull Crushers", "Close-Grip Bench Press", "Squats", "Front Squats", 
    "Bulgarian Split Squats", "Leg Press", "Deadlifts", "Hip Thrusts", "Glute Bridges", 
    "Lunges", "Step-Ups", "Calf Raises", "Leg Extensions", "Leg Curls", "Hack Squats", 
    "Plank", "Russian Twists", "Hanging Leg Raises", "Mountain Climbers", "Cable Crunches", 
    "Ab Wheel Rollouts", "Burpees", "Kettlebell Swings", "Box Jumps", "Jump Rope", 
    "Battle Ropes", "Farmer's Walk", "Dumbbell Shrugs", "Barbell Shrugs"
]

sports = [
    "Football", "Basketball", "Tennis", "Cricket", "Volleyball", 
    "Baseball", "Rugby", "Golf", "Hockey", "Badminton", 
    "Table Tennis", "Swimming", "Athletics", "Cycling", "Boxing", 
    "Martial Arts", "Wrestling", "Gymnastics", "Skiing", "Snowboarding", 
    "Surfing", "Skateboarding", "Rowing", "Sailing", "Canoeing", 
    "Kayaking", "Triathlon", "Marathon", "Ultimate Frisbee", "Lacrosse", 
    "Handball", "Squash", "Fencing", "Archery", "Shooting", 
    "Weightlifting", "Powerlifting", "CrossFit", "Darts", "Bowling", 
    "Horse Racing", "Polo", "Ice Hockey", "Figure Skating", "Curling", 
    "Bobsleigh", "Luge", "Skeleton", "Climbing", "Parkour"
]