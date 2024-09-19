FitTrack - Comprehensive Health and Wellness Platform

FitTrack is a comprehensive health and wellness platform designed to help users track their physical and mental health. The application offers tools for tracking body metrics, setting health goals, and calculating important health statistics such as BMI and daily calorie needs.

Features

Track daily physical health metrics such as weight and height.
Calculate BMI (Body Mass Index).
Calculate daily calorie needs based on activity level.
Set and track fitness goals like weight loss, muscle gain, or endurance.
Track mental wellness with a built-in journaling feature.

Table of Contents

Installation
Usage
Contributing
License

Installation

To get started with FitTrack, follow these steps:

1. Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>

2. Set up a virtual environment:

bash
Copy code
pipenv install
pipenv shell

3. Install dependencies:

bash
Copy code
pip install -r requirements.txt

Usage

1. Initialize the database:
To set up the database and tables, run the following command:

bash
Copy code
python -m fittrack.models

2. Run the application:
bash
Copy code
python main.py

3. Available Commands:
FitTrack is a Command Line Interface (CLI) application. After running python main.py, you can interact with the app using the following commands:

track – Log your daily physical health metrics.
bmi – Calculate your Body Mass Index based on weight and height.
calories – Calculate your daily calorie needs based on activity level.
goals – Set fitness goals (e.g., weight loss, muscle gain).
journal – Record your mental health and wellness through journaling.
Contributing
Contributions are welcome! If you’d like to contribute to FitTrack, please follow these steps:

Fork the repository.

Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Create a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

