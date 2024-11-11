class User:
    def __init__(self, name):
        self.name = name
        self.workouts = []
        self.goals = {}

    def add_workout(self, workout):
        self.workouts.append(workout)

    def set_goal(self, goal_type, target_value):
        self.goals[goal_type] = target_value

    def get_progress(self):
        progress = {}
        for goal_type, target_value in self.goals.items():
            total = sum(workout[goal_type] for workout in self.workouts if goal_type in workout)
            progress[goal_type] = total
        return progress

    def __str__(self):
        return f"User: {self.name}, Goals: {self.goals}, Workouts: {self.workouts}"


class Workout:
    def __init__(self, type, duration, calories_burned):
        self.type = type
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned

    def to_dict(self):
        return {
            'type': self.type,
            'duration': self.duration,
            'calories_burned': self.calories_burned
        }

    def __str__(self):
        return f"Workout(type={self.type}, duration={self.duration}min, calories_burned={self.calories_burned})"


def main():
    # Create a new user
    user_name = input("Enter your name: ")
    user = User(user_name)

    # Set fitness goals
    calories_goal = int(input("Set your calorie burn goal: "))
    user.set_goal('calories_burned', calories_goal)

    while True:
        # Add workouts
        workout_type = input("Enter workout type (or 'done' to finish): ")
        if workout_type.lower() == 'done':
            break
        duration = int(input("Enter workout duration in minutes: "))
        calories_burned = int(input("Enter calories burned: "))

        workout = Workout(workout_type, duration, calories_burned)
        user.add_workout(workout.to_dict())

    # Display user information and progress
    print(user)
    progress = user.get_progress()
    print("Progress towards goals:")
    for goal_type, total in progress.items():
        print(f"{goal_type}: {total} / {user.goals.get(goal_type, 'Not Set')}")

if __name__ == "__main__":
    main()