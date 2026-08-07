import pandas as pd

def workout_frequency(workouts):
    if not workouts:
        return None

    df = pd.DataFrame(workouts)
    df["date"] = pd.to_datetime(df["date"])
    df["week"] = df["date"].dt.strftime("%Y-%U")

    weekly = (
        df.groupby("week")
        .size()
        .reset_index(name = "workouts")
    )
    return weekly

def weight_progress(measurements):
    if not measurements:
        return None
    df = pd.DataFrame(measurements)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    return df[["date","body_weight"]]


def muscle_distribution(data):
    if not data:
        return None
    df = pd.DataFrame(data)

    result =(
        df.groupby("muscle_group_name")
        .size()
        .reset_index(name= "count")
    )
    return result

def training_volume(sets):
    if not set:
        return None

    df = pd.DataFrame(sets)

    df["volume"]= (
        df["weights"]
        * 
        df["reps"]
    )

    result = (
        df.groupby("workout_id")
        ["volume"]
        .sum()
        .reset_index
    )
    return result
    