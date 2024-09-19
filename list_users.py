from fittrack.models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def list_users():
    session = Session()
    try:
        users = session.query(User).all()
        for user in users:
            print(user.id, user.username, user.age)
    except Exception as e:
        print(f"Error listing users: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    list_users()
