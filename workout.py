import random


def generate_workout_plan(n): #added argument 'n'
    workouts = [
        "Push-ups",
        "Sit-ups",
        "Squats",
        "Jumping Jacks",
        "Running",
        "Cycling",
        "Swimming",
        "Yoga",

    ]
    workout_plan = []

    for i in range(n): #added argument 'n'
        workout_plan.append(random.choice(workouts))

    return workout_plan
# n=int(input('number of workout:')) #input number of workout
# workout_plan=generate_workout_plan(n) #generate workout plan
# print(workout_plan) #print workout plan
