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
