import sys
from fittrack.views import (
    display_menu,
    create_user_view,
    set_physical_goal_view,
    set_mental_goal_view,
    log_workout_view,
    log_nutrition_view,
    log_mental_health_view,
    view_progress_view,
    get_recommendations_view
)

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            create_user_view()
        elif choice == '2':
            set_physical_goal_view()
        elif choice == '3':
            set_mental_goal_view()
        elif choice == '4':
            log_workout_view()
        elif choice == '5':
            log_nutrition_view()
        elif choice == '6':
            log_mental_health_view()
        elif choice == '7':
            view_progress_view()
        elif choice == '8':
            get_recommendations_view()
        elif choice == '9':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
