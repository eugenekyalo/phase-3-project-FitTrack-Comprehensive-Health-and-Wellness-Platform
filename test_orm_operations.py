from fittrack.models import User, Goal, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def test_operations():
    session = Session()
    try:
        # Check if the user already exists
        existing_user = session.query(User).filter_by(username='test_user').first()
        if existing_user:
            print(f"User already exists: {existing_user}")
        else:
            # Create a new user
            user = User(username='test_user', age=30, height=180, weight=75, fitness_level='beginner')
            session.add(user)
            session.commit()
            print(f"Created User: {user}")

        # Add a goal for the user
        if existing_user:
            user = existing_user

        goal = Goal(user_id=user.id, goal_type='weight_loss', target_value=10, current_value=5)
        session.add(goal)
        session.commit()
        print(f"Created Goal: {goal}")

    except Exception as e:
        print(f"Error during ORM operations: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_operations()


