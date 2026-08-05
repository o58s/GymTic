from db_connection import connection, cursor


# Exercise CRUD operations
def add_exercise(exercise_name, equipment, difficulty):
    query = "INSERT INTO exercises (exercise_name, equipment, difficulty) VALUES (%s, %s, %s)"
    cursor.execute(query, (exercise_name, equipment, difficulty))
    connection.commit()
    return cursor.lastrowid

def get_exercises():
    query = "SELECT * FROM exercises"
    cursor.execute(query)
    return cursor.fetchall()
     

def get_exercise_by_id(exercise_id):
    query = "SELECT * FROM exercises WHERE exercise_id = %s"
    cursor.execute(query, (exercise_id,))
    return cursor.fetchone()
     

def update_exercise(exercise_id, exercise_name, equipment, difficulty):
    query = "UPDATE exercises SET exercise_name = %s, equipment = %s, difficulty = %s WHERE exercise_id = %s"
    cursor.execute(query, (exercise_name, equipment, difficulty, exercise_id))
    connection.commit()
    return cursor.rowcount

def delete_exercise(exercise_id):
    query = "DELETE FROM exercises WHERE exercise_id = %s"
    cursor.execute(query, (exercise_id,))
    connection.commit()
    return cursor.rowcount


# User CRUD operations
def add_user(age, height, weight, goal):
    query = "INSERT INTO users(age, height, weight, goal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (age, height, weight, goal))
    connection.commit()
    return cursor.lastrowid

def get_users():
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()

def get_user_by_id(user_id):
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

def update_user(user_id, age, height, weight, goal):
    query = "UPDATE users SET age = %s, height = %s, weight = %s, goal = %s WHERE user_id = %s"
    cursor.execute(query, (age, height, weight, goal, user_id))
    connection.commit()
    return cursor.rowcount

def delete_user(user_id):
    query = "DELETE FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    return cursor.rowcount

# Muscle Group operations
def get_muscle_groups():
    query = "SELECT * FROM musclegroups"
    cursor.execute(query)
    return cursor.fetchall()

def get_muscle_group_by_id(muscle_group_id):
    query = "SELECT * FROM musclegroups WHERE muscle_group_id = %s"
    cursor.execute(query, (muscle_group_id,))
    return cursor.fetchone()

#Exercise-Muscle operations
def link_exercise_to_muscle(exercise_id, muscle_group_id):
    query = "INSERT INTO exercisemuscles (exercise_id, muscle_group_id) VALUES (%s, %s)"
    cursor.execute(query, (exercise_id, muscle_group_id))
    connection.commit()
    return cursor.rowcount

def get_muscles_for_exercise(exercise_id):
    query = "SELECT mg.muscle_group_name FROM musclegroups mg JOIN exercisemuscles em ON mg.muscle_group_id = em.muscle_group_id WHERE em.exercise_id = %s"
    cursor.execute(query, (exercise_id,))
    return cursor.fetchall()

def get_exercises_for_muscle(muscle_group_id):
    query = "SELECT e.exercise_name FROM exercises e JOIN exercisemuscles em ON e.exercise_id = em.exercise_id WHERE em.muscle_group_id = %s"
    cursor.execute(query, (muscle_group_id,))
    return cursor.fetchall()

def unlink_exercise_from_muscle(exercise_id, muscle_group_id):
    query = "DELETE FROM exercisemuscles WHERE exercise_id = %s AND muscle_group_id = %s"
    cursor.execute(query, (exercise_id, muscle_group_id))
    connection.commit()
    return cursor.rowcount



# workout set operations
def add_workout_set(workout_id, exercise_id, set_number, weight, reps, rest_time):
    query = "INSERT INTO workoutsets (workout_id, exercise_id, set_number, weight, reps, rest_time) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (workout_id, exercise_id, set_number, weight, reps, rest_time))
    connection.commit()
    return cursor.lastrowid

def get_workout_sets():
    query = "SELECT * FROM workoutsets"
    cursor.execute(query)
    return cursor.fetchall()

def get_workout_set_by_id(set_id):
    query = "SELECT * FROM workoutsets WHERE set_id = %s"
    cursor.execute(query, (set_id,))
    return cursor.fetchone()

def get_workout_sets_by_workout_id(workout_id):
    query = "SELECT * FROM workoutsets WHERE workout_id = %s"
    cursor.execute(query, (workout_id,))
    return cursor.fetchall()

def update_workout_set(set_id, workout_id, exercise_id, set_number, weight, reps, rest_time):
    query = "UPDATE workoutsets SET workout_id = %s, exercise_id = %s, set_number = %s, weight = %s, reps = %s, rest_time = %s WHERE set_id = %s"
    cursor.execute(query, (workout_id, exercise_id, set_number, weight, reps, rest_time, set_id))
    connection.commit()
    return cursor.rowcount

def delete_workout_set(set_id):
    query = "DELETE FROM workoutsets WHERE set_id = %s"
    cursor.execute(query, (set_id,))
    connection.commit()
    return cursor.rowcount


# measurement operations
def add_measurement(user_id, date, body_weight, bmi):
    query = "INSERT INTO measurements(user_id, date, body_weight, bmi) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, date, body_weight, bmi))
    connection.commit()
    return cursor.lastrowid

def get_user_measurements(user_id):
    query = "SELECT * FROM measurements WHERE user_id = %s ORDER BY date DESC"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

def get_latest_measurement(user_id):
    query = "SELECT * FROM measurements WHERE user_id = %s ORDER BY date DESC LIMIT 1"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

def get_measurement_by_id(measurement_id):
    query = "SELECT * FROM measurements WHERE measurement_id = %s"
    cursor.execute(query, (measurement_id,))
    return cursor.fetchone()

def update_measurement(measurement_id, user_id, date, body_weight, bmi):
    query = "UPDATE measurements SET user_id = %s, date = %s, body_weight = %s, bmi = %s WHERE measurement_id = %s"
    cursor.execute(query, (user_id, date, body_weight, bmi, measurement_id))
    connection.commit()
    return cursor.rowcount

def delete_measurement(measurement_id):
    query = "DELETE FROM measurements WHERE measurement_id = %s"
    cursor.execute(query, (measurement_id,))
    connection.commit()
    return cursor.rowcount

# Goal operations
def add_goal(user_id, target_weight, weekly_workout_goal, monthly_workout_goal):
    query = "INSERT INTO goals(user_id, target_weight, weekly_workout_goal, monthly_workout_goal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, target_weight, weekly_workout_goal, monthly_workout_goal))
    connection.commit()
    return cursor.lastrowid

def get_user_goals(user_id):
    query = "SELECT * FROM goals WHERE user_id = %s ORDER BY goal_id DESC"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

def get_goal_by_id(goal_id):
    query = "SELECT * FROM goals WHERE goal_id = %s"
    cursor.execute(query, (goal_id,))
    return cursor.fetchone()

def update_goal(goal_id, user_id, target_weight, weekly_workout_goal, monthly_workout_goal):
    query = "UPDATE goals SET user_id = %s, target_weight = %s, weekly_workout_goal = %s, monthly_workout_goal = %s WHERE goal_id = %s"
    cursor.execute(query, (user_id, target_weight, weekly_workout_goal, monthly_workout_goal, goal_id))
    connection.commit()
    return cursor.rowcount

def delete_goal(goal_id):
    query = "DELETE FROM goals WHERE goal_id = %s"
    cursor.execute(query, (goal_id,))
    connection.commit()
    return cursor.rowcount