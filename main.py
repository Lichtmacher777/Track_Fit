import auth
import calories
import log
import progress
import workout

def main():
    if auth.authenticate_user():
        n = int(input("Enter the number of workouts: "))
        workout_plan = workout.generate_workout_plan(n)

        for activity in workout_plan:
            start_time = input(f"Enter the start time for {activity} (HH:MM): ")
            end_time = input(f"Enter the end time for {activity} (HH:MM): ")
            calories_burned = calories.calculate_calories_burned(activity, start_time, end_time)
            if calories_burned is not None:
                log.log_activity(f"{activity} - {start_time} to {end_time} - Calories Burned: {calories_burned}")
                progress.update_progress(progress.progress, activity)
                progress.burned_calories[activity] += calories_burned

        print("Workout plan and progress logged successfully.")
        progress.display_progress(progress.progress, progress.burned_calories)  # Display progress
    else:
        print("User is invalid, please try again.")

if __name__ == "__main__":
    main()
