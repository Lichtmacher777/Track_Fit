import datetime


def get_duration_in_minutes(start_time, end_time):
    fmt = "%H: %M"  # Define the time format
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    duration = end - start
    duration_minutes = duration // 60
    return int(duration_minutes)


def calculate_calories_burned(activity):
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
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")

    duration = get_duration_in_minutes(start_time, end_time) // 30

    return calorie_chart[activity] * duration
