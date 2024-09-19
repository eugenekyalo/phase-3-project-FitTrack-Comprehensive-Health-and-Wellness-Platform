from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    goal = Column(String, index=True)

    def __repr__(self):
        return f"<Goal(id={self.id}, goal={self.goal})>"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    fitness_level = Column(String)

    physical_goals = relationship("PhysicalGoal", back_populates="user")
    mental_goals = relationship("MentalGoal", back_populates="user")
    workouts = relationship("Workout", back_populates="user")
    nutrition_logs = relationship("NutritionLog", back_populates="user")
    mental_logs = relationship("MentalHealthLog", back_populates="user")

    def __repr__(self):
        return (f"<User(id={self.id}, username={self.username}, age={self.age}, "
                f"height={self.height}, weight={self.weight}, fitness_level={self.fitness_level})>")

class PhysicalGoal(Base):
    __tablename__ = 'physical_goals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal_type = Column(String)
    target_value = Column(Float)
    current_value = Column(Float)

    user = relationship("User", back_populates="physical_goals")

    def __repr__(self):
        return (f"<PhysicalGoal(id={self.id}, user_id={self.user_id}, goal_type={self.goal_type}, "
                f"target_value={self.target_value}, current_value={self.current_value})>")

class MentalGoal(Base):
    __tablename__ = 'mental_goals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal_type = Column(String)
    target_value = Column(Float)
    current_value = Column(Float)

    user = relationship("User", back_populates="mental_goals")

    def __repr__(self):
        return (f"<MentalGoal(id={self.id}, user_id={self.user_id}, goal_type={self.goal_type}, "
                f"target_value={self.target_value}, current_value={self.current_value})>")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    exercise_type = Column(String)
    duration = Column(Integer)
    intensity = Column(String)
    calories_burned = Column(Integer)
    heart_rate = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="workouts")

    def __repr__(self):
        return (f"<Workout(id={self.id}, user_id={self.user_id}, exercise_type={self.exercise_type}, "
                f"duration={self.duration}, intensity={self.intensity}, calories_burned={self.calories_burned}, "
                f"heart_rate={self.heart_rate}, date={self.date})>")

class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    food_item = Column(String)
    calories = Column(Integer)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="nutrition_logs")

    def __repr__(self):
        return (f"<NutritionLog(id={self.id}, user_id={self.user_id}, food_item={self.food_item}, "
                f"calories={self.calories}, protein={self.protein}, carbs={self.carbs}, fats={self.fats}, "
                f"date={self.date})>")

class MentalHealthLog(Base):
    __tablename__ = 'mental_health_logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stress_level = Column(Integer)
    sleep_hours = Column(Float)
    mindfulness_minutes = Column(Integer)
    mood = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="mental_logs")

    def __repr__(self):
        return (f"<MentalHealthLog(id={self.id}, user_id={self.user_id}, stress_level={self.stress_level}, "
                f"sleep_hours={self.sleep_hours}, mindfulness_minutes={self.mindfulness_minutes}, "
                f"mood={self.mood}, date={self.date})>")

# Create the database
engine = create_engine('sqlite:///fittrack.db')
Base.metadata.create_all(engine)
