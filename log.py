def log_activity(activity):
    with open("activity_log.txt", "a") as file:  # Use 'a' for append mode
        file.write(activity + "\n")