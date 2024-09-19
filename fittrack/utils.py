def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    - weight: Weight in kilograms
    - height: Height in centimeters

    Returns:
    - BMI value
    """
    return weight / ((height / 100) ** 2)

def calculate_daily_calorie_needs(weight, height, age, gender, activity_level):
    """
    Calculate daily calorie needs based on weight, height, age, gender, and activity level.

    Parameters:
    - weight: Weight in kilograms
    - height: Height in centimeters
    - age: Age in years
    - gender: Gender ('male' or 'female')
    - activity_level: Activity level ('sedentary', 'lightly active', 'moderately active', 'very active', 'extra active')

    Returns:
    - Daily calorie needs
    """
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }

    return bmr * activity_factors.get(activity_level.lower(), 1.2)

def calculate_macronutrient_ratio(goal):
    """
    Calculate macronutrient ratios based on fitness goals.

    Parameters:
    - goal: Fitness goal ('weight_loss', 'muscle_gain', 'endurance', or other)

    Returns:
    - Dictionary with macronutrient ratios
    """
    if goal == 'weight_loss':
        return {'protein': 0.4, 'carbs': 0.3, 'fats': 0.3}
    elif goal == 'muscle_gain':
        return {'protein': 0.5, 'carbs': 0.3, 'fats': 0.2}
    elif goal == 'endurance':
        return {'protein': 0.3, 'carbs': 0.5, 'fats': 0.2}
    else:
        return {'protein': 0.3, 'carbs': 0.4, 'fats': 0.3}
