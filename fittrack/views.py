from .controllers import UserController, GoalController, WorkoutController, NutritionController, MentalHealthController
from .recommendations import get_recommendations

def display_menu():
    print("\nFitTrack Menu:")
    print("1. Create User")
    print("2. Set Physical Goal")
    print("3. Set Mental Goal")
    print("4. Log Workout")
    print("5. Log Nutrition")
    print("6. Log Mental Health")
    print("7. View Progress")
    print("8. Get Recommendations")
    print("9. Exit")
    return input("Enter your choice: ")

def create_user_view():
    username = input("Enter username: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height (cm): "))
    weight = float(input("Enter weight (kg): "))
    fitness_level = input("Enter fitness level (beginner/intermediate/advanced): ")
    user = UserController.create_user(username, age, height, weight, fitness_level)
    print(f"User {user.username} created successfully!")

def set_physical_goal_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        goal_type = input("Enter physical goal type (weight_loss/muscle_gain/endurance): ")
        target_value = float(input("Enter target value: "))
        current_value = float(input("Enter current value: "))
        goal = GoalController.create_physical_goal(user.id, goal_type, target_value, current_value)
        print(f"Physical goal set for {user.username}: {goal_type} - Target: {target_value}")
    else:
        print("User not found.")

def set_mental_goal_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        goal_type = input("Enter mental goal type (stress_reduction/sleep_improvement/mindfulness): ")
        target_value = float(input("Enter target value: "))
        current_value = float(input("Enter current value: "))
        goal = GoalController.create_mental_goal(user.id, goal_type, target_value, current_value)
        print(f"Mental goal set for {user.username}: {goal_type} - Target: {target_value}")
    else:
        print("User not found.")

def log_workout_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        exercise_type = input("Enter exercise type: ")
        duration = int(input("Enter duration (minutes): "))
        intensity = input("Enter intensity (low/medium/high): ")
        calories_burned = int(input("Enter estimated calories burned: "))
        heart_rate = int(input("Enter average heart rate: "))
        workout = WorkoutController.log_workout(user.id, exercise_type, duration, intensity, calories_burned, heart_rate)
        print(f"Workout logged for {user.username}: {exercise_type} for {duration} minutes")
    else:
        print("User not found.")

def log_nutrition_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        food_item = input("Enter food item: ")
        calories = int(input("Enter calories: "))
        protein = float(input("Enter protein (g): "))
        carbs = float(input("Enter carbs (g): "))
        fats = float(input("Enter fats (g): "))
        log = NutritionController.log_nutrition(user.id, food_item, calories, protein, carbs, fats)
        print(f"Nutrition logged for {user.username}: {food_item} - {calories} calories")
    else:
        print("User not found.")

def log_mental_health_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        stress_level = int(input("Enter stress level (1-10): "))
        sleep_hours = float(input("Enter hours of sleep: "))
        mindfulness_minutes = int(input("Enter minutes spent on mindfulness: "))
        mood = input("Enter current mood: ")
        log = MentalHealthController.log_mental_health(user.id, stress_level, sleep_hours, mindfulness_minutes, mood)
        print(f"Mental health logged for {user.username}")
    else:
        print("User not found.")

def view_progress_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        print(f"\nProgress for {user.username}:")
        print(f"Current weight: {user.weight} kg")
        print("\nPhysical Goals:")
        for goal in user.physical_goals:
            progress = (goal.current_value / goal.target_value) * 100
            print(f"- {goal.goal_type}: {goal.current_value}/{goal.target_value} ({progress:.2f}% complete)")
        print("\nMental Goals:")
        for goal in user.mental_goals:
            progress = (goal.current_value / goal.target_value) * 100
            print(f"- {goal.goal_type}: {goal.current_value}/{goal.target_value} ({progress:.2f}% complete)")
        print("\nRecent Workouts:")
        for workout in user.workouts[-5:]:
            print(f"- {workout.exercise_type} for {workout.duration} minutes, burned {workout.calories_burned} calories, avg heart rate: {workout.heart_rate}")
        print("\nNutrition Summary (Last 7 days):")
        total_calories = sum(log.calories for log in user.nutrition_logs[-7:])
        avg_calories = total_calories / 7 if user.nutrition_logs else 0
        print(f"Average daily calories: {avg_calories:.2f}")
        print("\nMental Health Summary (Last 7 days):")
        avg_stress = sum(log.stress_level for log in user.mental_logs[-7:]) / 7 if user.mental_logs else 0
        avg_sleep = sum(log.sleep_hours for log in user.mental_logs[-7:]) / 7 if user.mental_logs else 0
        print(f"Average stress level: {avg_stress:.2f}")
        print(f"Average sleep duration: {avg_sleep:.2f} hours")
    else:
        print("User not found.")

def get_recommendations_view():
    username = input("Enter username: ")
    user = UserController.get_user(username)
    if user:
        recommendations = get_recommendations(user)
        print("\nPersonalized Recommendations:")
        for category, rec in recommendations.items():
            print(f"\n{category.capitalize()}:")
            for item in rec:
                print(f"- {item}")
    else:
        print("User not found.")