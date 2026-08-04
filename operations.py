from db_connection import connection, cursor

def get_exercises():
    query = "SELECT * FROM exercises"
    cursor.execute(query)
    exercises = cursor.fetchall()
    return exercises

def get_muscle_groups():
    query = "SELECT * FROM musclegroups"
    cursor.execute(query)
    muscle_groups = cursor.fetchall()
    return muscle_groups

def add_exercise(exercise_name, equipment, difficulty):
    query = "INSERT INTO exercises (exercise_name, equipment, difficulty) VALUES (%s, %s, %s)"
    cursor.execute(query, (exercise_name, equipment, difficulty))
    connection.commit()
