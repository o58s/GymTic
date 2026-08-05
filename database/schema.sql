use gymtic;
CREATE TABLE Users(
user_id INT AUTO_INCREMENT,
name VARCHAR(100),
age INT,
height DECIMAL(5,2),
weight DECIMAL(5,2),
goal VARCHAR(50),
PRIMARY KEY (user_id)
);

CREATE TABLE Exercises(
exercise_id INT AUTO_INCREMENT,
exercise_name VARCHAR(100),
equipment VARCHAR(50),
difficulty VARCHAR(50),
PRIMARY KEY (exercise_id)
);

CREATE TABLE MuscleGroups(
muscle_group_id INT AUTO_INCREMENT,
muscle_group_name VARCHAR(100),
PRIMARY KEY (muscle_group_id)
);

CREATE TABLE ExerciseMuscles(
exercise_id INT,
muscle_group_id INT,
PRIMARY KEY (exercise_id, muscle_group_id),
FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
FOREIGN KEY (muscle_group_id) REFERENCES MuscleGroups(muscle_group_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE Workouts (
workout_id INT AUTO_INCREMENT,
user_id INT,
date DATE,
workout_type VARCHAR(50),
duration INT,
notes TEXT,
PRIMARY KEY (workout_id),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE WorkoutSets (
set_id INT AUTO_INCREMENT,
workout_id INT,
exercise_id INT,
weight DECIMAL(6,2),
reps INT,
sets INT,
rest_time INT,
PRIMARY KEY (set_id),
FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE Measurements (
measurement_id INT AUTO_INCREMENT,
user_id INT,
date DATE,
body_weight DECIMAL(5,2),
BMI DECIMAL(5,2),
PRIMARY KEY (measurement_id),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE Goals (
goal_id INT AUTO_INCREMENT,
user_id INT,
target_weight DECIMAL(5,2),
weekly_workout_goal INT,
monthly_training_goal INT,
PRIMARY KEY (goal_id),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE PersonalRecords (
record_id INT AUTO_INCREMENT,
user_id INT,
exercise_id INT,
weight DECIMAL(6,2),
date DATE,
PRIMARY KEY (record_id),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE,
FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE WorkoutSets (
    set_id INT AUTO_INCREMENT,
    workout_id INT,
    exercise_id INT,
    set_number INT,
    weight DECIMAL(6,2),
    reps INT,
    rest_time INT,
    PRIMARY KEY (set_id),
    FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);