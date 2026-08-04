from db_connection import connection, cursor
muscle_name = muscle_name = [
    "Chest",
    "Back",
    "Legs",
    "Shoulders",
    "Biceps",
    "Triceps",
    "Core"
]

exercise_name = [
    ("Bench press", "Barbell", "Intermediate"),
    ("Incline Dumbbell Press ", "Dumbbell", "Intermediate"),
    ("Chest Fly ", "Machine", "Beginner"),
]


muscleQuery = "INSERT INTO musclegroups (muscle_group_name) VALUES (%s)"

for muscle in muscle_name:
    cursor.execute(muscleQuery, (muscle,))  
connection.commit()

exerciseQuery = "INSERT INTO exercises (exercise_name, equipment, difficulty) VALUES (%s, %s, %s)"

for exercise in exercise_name:
    cursor.execute(exerciseQuery, exercise)

connection.commit()

cursor.close()
connection.close()
print("Seed data inserted successfully")