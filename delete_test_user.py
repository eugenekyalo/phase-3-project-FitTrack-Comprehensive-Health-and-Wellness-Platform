from fittrack.models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def delete_existing_users():
    session = Session()
    try:
        # Delete existing users with the username 'test_user'
        session.query(User).filter_by(username='test_user').delete()
        session.commit()
        print("Existing test users removed.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting users: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    delete_existing_users()
