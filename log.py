def log_activity(activity):
    with open("activity_log.txt", "w") as file:
        file.write(activity + "\n")
