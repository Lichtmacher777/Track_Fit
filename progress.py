def update_progress(progress, workout):
    progress[workout] += 1
progress = {
    "Running": 0,
    "Cycling": 0,
    "Swimming": 0,
    "Yoga": 0,
    "Push-ups": 0,
    "Sit-ups": 0,
    "Squats": 0,
    "Jumping Jacks": 0,
}

burned_calories = {
    "Running": 0,
    "Cycling": 0,
    "Swimming": 0,
    "Yoga": 0,
    "Push-ups": 0,
    "Sit-ups": 0,
    "Squats": 0,
    "Jumping Jacks": 0,
}
def display_progress(progress, burned_calories):
    print("\nProgress:")
    for activity, count in progress.items():
        print(f"{activity}: {count} times")
    print("\nCalories Burned:")
    for activity, calories in burned_calories.items():
        print(f"{activity}: {calories} calories")
