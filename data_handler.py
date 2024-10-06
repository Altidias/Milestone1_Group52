import pandas as pd
import sqlite3
import sys
from datetime import datetime
import itertools


class DataHandler:
    NUTRIENT_UNITS = {
        'Food': 'name',
        'Caloric Value': 'kcal/100g',
        'Fat': 'g/100g',
        'Saturated Fats': 'g/100g',
        'Monounsaturated Fats': 'g/100g',
        'Polyunsaturated Fats': 'g/100g',
        'Carbohydrates': 'g/100g',
        'Sugars': 'g/100g',
        'Protein': 'g/100g',
        'Dietary Fiber': 'g/100g',
        'Cholesterol': 'mg/100g',
        'Sodium': 'mg/100g',
        'Water': 'g/100g',
        'Vitamin A': 'mg/100g',
        'Vitamin B1': 'mg/100g',
        'Vitamin B11': 'mg/100g',
        'Vitamin B12': 'mg/100g',
        'Vitamin B2': 'mg/100g',
        'Vitamin B3': 'mg/100g',
        'Vitamin B5': 'mg/100g',
        'Vitamin B6': 'mg/100g',
        'Vitamin C': 'mg/100g',
        'Vitamin D': 'mg/100g',
        'Vitamin E': 'mg/100g',
        'Vitamin K': 'mg/100g',
        'Calcium': 'mg/100g',
        'Copper': 'mg/100g',
        'Iron': 'mg/100g',
        'Magnesium': 'mg/100g',
        'Manganese': 'mg/100g',
        'Phosphorus': 'mg/100g',
        'Potassium': 'mg/100g',
        'Selenium': 'mg/100g',
        'Zinc': 'mg/100g',
        'Nutrition Density': 'score'
    }

    MACRONUTRIENTS = ['Caloric Value', 'Protein', 'Carbohydrates', 'Fat', 'Saturated Fats',
                      'Monounsaturated Fats', 'Polyunsaturated Fats', 'Sugars', 'Dietary Fiber',
                      'Cholesterol', 'Water']

    MICRONUTRIENTS = ['Vitamin A', 'Vitamin B1', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5',
                      'Vitamin B6', 'Vitamin B11', 'Vitamin B12', 'Vitamin C', 'Vitamin D',
                      'Vitamin E', 'Vitamin K', 'Calcium', 'Copper', 'Iron', 'Magnesium',
                      'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc']

    def __init__(self, db_path='data/Food_Nutrition_Dataset.csv', user_data_path='data/user_data.db'):
        self.db_path = db_path
        self.user_data_path = user_data_path
        self.database_df = None
        self.conn = None
        self.cursor = None
        self.load_database()
        self.init_user_data()

    def load_database(self):
        try:
            self.database_df = pd.read_csv(self.db_path)
            print("Database loaded successfully.")
        except Exception as e:
            print(f"An error occurred while loading the database: {e}")
            sys.exit(1)

    def init_user_data(self):
        try:
            self.conn = sqlite3.connect(self.user_data_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS daily_intake (
                    date TEXT,
                    nutrient TEXT,
                    value REAL,
                    PRIMARY KEY (date, nutrient)
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS current_goals (
                    nutrient TEXT PRIMARY KEY,
                    value REAL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS historical_goals (
                    date TEXT,
                    nutrient TEXT,
                    value REAL,
                    PRIMARY KEY (date, nutrient)
                )
            ''')
            self.conn.commit()
            print("User data initialized successfully.")
        except Exception as e:
            print(f"An error occurred while initializing user data: {e}")
            sys.exit(1)

    def update_daily_intake(self, nutrients, quantity=1, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        try:
            for nutrient, value in nutrients.items():
                if nutrient == 'food' or nutrient == 'Nutrition Density':
                    continue 
                self.cursor.execute('''
                    INSERT OR REPLACE INTO daily_intake (date, nutrient, value)
                    VALUES (?, ?, COALESCE((SELECT value FROM daily_intake WHERE date = ? AND nutrient = ?), 0) + ?)
                ''', (date, nutrient, date, nutrient, value * quantity))
            self.conn.commit() 
        except Exception as e:
            print(f"An error occurred while updating daily intake: {e}")
            self.conn.rollback()
            raise e  

    def set_daily_goal(self, nutrients, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        try:
            for nutrient, value in nutrients.items():
                if nutrient == 'food' or nutrient == 'Nutrition Density':
                    continue

                self.cursor.execute('''
                    INSERT OR REPLACE INTO current_goals (nutrient, value)
                    VALUES (?, ?)
                ''', (nutrient, value))
                

                self.cursor.execute('''
                    INSERT OR REPLACE INTO historical_goals (date, nutrient, value)
                    VALUES (?, ?, ?)
                ''', (date, nutrient, value))
            
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred while setting daily goals: {e}")
            self.conn.rollback()
            raise e 

    def get_database(self):
        return self.database_df

    def get_user_data(self):
        try:
            self.cursor.execute("SELECT date, nutrient, value FROM daily_intake")
            daily_intake = self.cursor.fetchall()
            self.cursor.execute("SELECT nutrient, value FROM current_goals")
            current_goals = self.cursor.fetchall()
            self.cursor.execute("SELECT date, nutrient, value FROM historical_goals")
            historical_goals = self.cursor.fetchall()
            
            return {
                'daily_intake': {date: {nutrient: value for _, nutrient, value in group}
                                 for date, group in itertools.groupby(daily_intake, key=lambda x: x[0])},
                'current_goals': dict(current_goals),
                'historical_goals': {date: {nutrient: value for _, nutrient, value in group}
                                     for date, group in itertools.groupby(historical_goals, key=lambda x: x[0])}
            }
        except Exception as e:
            print(f"An error occurred while fetching user data: {e}")
            return {'daily_intake': {}, 'current_goals': {}, 'historical_goals': {}}

    def get_goals_for_date(self, date):
        try:
            self.cursor.execute('''
                SELECT nutrient, value FROM historical_goals
                WHERE date = ?
            ''', (date,))
            goals = self.cursor.fetchall()
            goals = [goal for goal in goals if goal[1] != 0]
            return dict(goals)
        except Exception as e:
            print(f"An error occurred while fetching goals for date {date}: {e}")
            return {}

    def get_intake_for_date(self, date):
        try:
            self.cursor.execute('''
                SELECT nutrient, value FROM daily_intake
                WHERE date = ?
            ''', (date,))
            intake = self.cursor.fetchall()
            return dict(intake)
        except Exception as e:
            print(f"An error occurred while fetching intake for date {date}: {e}")
            return {}
        
    def reset_user_data(self):
        self.cursor.execute("DELETE FROM daily_intake")
        self.cursor.execute("DELETE FROM current_goals")
        self.cursor.execute("DELETE FROM historical_goals")
        self.conn.commit()
        print("User data reset successfully.")

    def get_nutrient_unit(self, nutrient):
        return self.NUTRIENT_UNITS.get(nutrient)

    def __del__(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()



