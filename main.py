import auth, calories, log, progress, workout

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


def main():
    if auth.authenticate_user():
        pass
    else:
        print("User is invalid please try again")


if __name__ == "__main__":
    main()
