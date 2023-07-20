# calculate_calories_burned("Running")
#calories_burned = calculate_calories_burned("Running")
#print("Total calories burned:", calories_burned)
from datetime import datetime

def get_duration_in_minutes(start_time, end_time):
    fmt = "%H:%M"
    try:    #try/except for correct time format
        start = datetime.strptime(start_time, fmt)
        end = datetime.strptime(end_time, fmt)
        duration = end - start
        duration_minutes = duration.total_seconds() // 60
        return int(duration_minutes)
    except ValueError:
        print("Invalid time format. Please use the format HH:MM.")
        return None

def calculate_calories_burned(activity, start_time, end_time):
    calorie_chart = {
        "Running": 600,
        "Cycling": 500,
        "Swimming": 700,
        "Yoga": 300,
        "Push-ups": 300,
        "Sit-ups": 500,
        "Squats": 300,
        "Jumping Jacks": 700,
    }

    duration = get_duration_in_minutes(start_time, end_time)
    if duration is not None:
        return calorie_chart[activity] * duration // 60  # Divide by 60 for minutes
    else:
        return None
