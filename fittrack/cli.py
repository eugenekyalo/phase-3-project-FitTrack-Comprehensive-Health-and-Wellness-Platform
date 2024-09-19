import click
from fittrack.controllers import UserController, GoalController, WorkoutController

@click.group()
def cli():
    """FitTrack CLI."""
    pass

@cli.command()
@click.option('--user_id', type=int, required=True, help='ID of the user')
@click.option('--goal_type', type=str, required=True, help='Type of the goal')
@click.option('--target_value', type=float, required=True, help='Target value for the goal')
@click.option('--current_value', type=float, required=True, help='Current value for the goal')
@click.option('--is_mental', is_flag=True, help='Specify if the goal is mental')
def set_goal(user_id, goal_type, target_value, current_value, is_mental):
    """Set a fitness goal."""
    GoalController.set_goal(user_id, goal_type, target_value, current_value, is_mental)

@cli.command()
@click.option('--user_id', type=int, required=True, help='ID of the user')
@click.option('--weight', type=float, required=True, help='User weight')
@click.option('--height', type=float, required=True, help='User height')
def track(user_id, weight, height):
    """Track health metrics."""
    WorkoutController.track_metrics(user_id, weight, height)

@cli.command()
def view_journal():
    """View journal entries."""
    logs = UserController.view_journal()
    print("workouts:", logs['workouts'])
    print("nutrition_logs:", logs['nutrition_logs'])
    print("mental_health_logs:", logs['mental_health_logs'])

if __name__ == '__main__':
    cli()
