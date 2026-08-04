from db_connection import connection, cursor

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
