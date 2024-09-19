import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fittrack.models import Base, User, PhysicalGoal, MentalGoal, Workout, NutritionLog, MentalHealthLog

DATABASE_URL = 'sqlite:///test_fittrack.db'

class TestFitTrackModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    
    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        user = User(username='testuser', age=25, height=175.0, weight=70.0, fitness_level='moderate')
        self.session.add(user)
        self.session.commit()
        queried_user = self.session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.username, 'testuser')

# Add similar tests for other models...

if __name__ == '__main__':
    unittest.main()

