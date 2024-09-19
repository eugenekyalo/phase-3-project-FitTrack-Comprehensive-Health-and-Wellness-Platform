from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fittrack.models import User, PhysicalGoal, MentalGoal, Workout, NutritionLog, MentalHealthLog, Base

# Setup database connection and session
DATABASE_URL = 'sqlite:///fittrack.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class UserController:
    @staticmethod
    def create_user(username, age, height, weight, fitness_level):
        session = Session()
        try:
            new_user = User(username=username, age=age, height=height, weight=weight, fitness_level=fitness_level)
            session.add(new_user)
            session.commit()
            return new_user
        except Exception as e:
            session.rollback()
            print(f"Error creating user: {e}")
        finally:
            session.close()

    @staticmethod
    def get_user(username):
        session = Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            return user
        except Exception as e:
            print(f"Error retrieving user: {e}")
        finally:
            session.close()

    @staticmethod
    def view_journal():
        session = Session()
        try:
            # Example query to get all logs; adjust as needed
            logs = {
                'workouts': session.query(Workout).all(),
                'nutrition_logs': session.query(NutritionLog).all(),
                'mental_health_logs': session.query(MentalHealthLog).all()
            }
            return logs
        except Exception as e:
            print(f"Error viewing journal: {e}")
        finally:
            session.close()

class GoalController:
    @staticmethod
    def set_goal(user_id, goal_type, target_value, current_value, is_mental=False):
        session = Session()
        try:
            if is_mental:
                new_goal = MentalGoal(user_id=user_id, goal_type=goal_type, target_value=target_value, current_value=current_value)
            else:
                new_goal = PhysicalGoal(user_id=user_id, goal_type=goal_type, target_value=target_value, current_value=current_value)
            session.add(new_goal)
            session.commit()
            return new_goal
        except Exception as e:
            session.rollback()
            print(f"Error setting goal: {e}")
        finally:
            session.close()


    @staticmethod
    def create_mental_goal(user_id, goal_type, target_value, current_value):
        session = Session()
        try:
            new_goal = MentalGoal(user_id=user_id, goal_type=goal_type, target_value=target_value, current_value=current_value)
            session.add(new_goal)
            session.commit()
            return new_goal
        except Exception as e:
            session.rollback()
            print(f"Error creating mental goal: {e}")
        finally:
            session.close()

class WorkoutController:
    @staticmethod
    def log_workout(user_id, exercise_type, duration, intensity, calories_burned, heart_rate):
        session = Session()
        try:
            new_workout = Workout(user_id=user_id, exercise_type=exercise_type, duration=duration, intensity=intensity, calories_burned=calories_burned, heart_rate=heart_rate)
            session.add(new_workout)
            session.commit()
            return new_workout
        except Exception as e:
            session.rollback()
            print(f"Error logging workout: {e}")
        finally:
            session.close()

    @staticmethod
    def track_metrics(user_id, weight, height):
        session = Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                user.weight = weight
                user.height = height
                session.commit()
                return user
            else:
                print("User not found.")
        except Exception as e:
            session.rollback()
            print(f"Error tracking metrics: {e}")
        finally:
            session.close()

    @staticmethod
    def set_goal(user_id, goal_type, target_value, current_value, is_mental=False):
        session = Session()
        try:
            if is_mental:
                new_goal = MentalGoal(user_id=user_id, goal_type=goal_type, target_value=target_value, current_value=current_value)
            else:
                new_goal = PhysicalGoal(user_id=user_id, goal_type=goal_type, target_value=target_value, current_value=current_value)
            session.add(new_goal)
            session.commit()
            return new_goal
        except Exception as e:
            session.rollback()
            print(f"Error setting goal: {e}")
        finally:
            session.close()
