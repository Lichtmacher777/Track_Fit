import random


def generate_workout_plan():
    workouts = [
        "Push-ups",
        "Sit-ups",
        "Squats",
        "Jumping Jacks",
        "Push-ups",
        "Sit-ups",
        "Squats",
        "Jumping Jacks",
    ]
    workout_plan = []

    for i in range(5):
        workout_plan.append(random.choice(workouts))

    return workout_plan
