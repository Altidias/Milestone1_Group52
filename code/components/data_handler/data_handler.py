import pandas as pd
import sqlite3
import sys
from datetime import datetime
import itertools


class DataHandler:
    def __init__(self, db_path='../data/Food_Nutrition_Dataset.csv', user_data_path='../data/user_data.db'):
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

    def update_daily_intake(self, nutrients, quantity=1):
        today = datetime.now().strftime('%Y-%m-%d')
        try:
            for nutrient, value in nutrients.items():
                self.cursor.execute('''
                    INSERT OR REPLACE INTO daily_intake (date, nutrient, value)
                    VALUES (?, ?, COALESCE((SELECT value FROM daily_intake WHERE date = ? AND nutrient = ?), 0) + ?)
                ''', (today, nutrient, today, nutrient, value * quantity))
            self.conn.commit()
            print("Daily intake updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating daily intake: {e}")
            self.conn.rollback()

    def set_daily_goal(self, nutrients):
        today = datetime.now().strftime('%Y-%m-%d')
        try:
            for nutrient, value in nutrients.items():
                # Update current goals
                self.cursor.execute('''
                    INSERT OR REPLACE INTO current_goals (nutrient, value)
                    VALUES (?, ?)
                ''', (nutrient, value))
                
                # Add to historical goals
                self.cursor.execute('''
                    INSERT OR REPLACE INTO historical_goals (date, nutrient, value)
                    VALUES (?, ?, ?)
                ''', (today, nutrient, value))
            
            self.conn.commit()
            print("Daily goals set and historical record updated successfully.")
        except Exception as e:
            print(f"An error occurred while setting daily goals: {e}")
            self.conn.rollback()

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
                WHERE date <= ?
                GROUP BY nutrient
                HAVING date = MAX(date)
            ''', (date,))
            goals = self.cursor.fetchall()
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

    def __del__(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()


# example:
if __name__ == "__main__":
    handler = DataHandler()
    print("Database Head:")
    print(handler.get_database().head())
    print("\nLoaded user data:")
    print(handler.get_user_data())

    intake = {'Caloric Value': 500, 'Protein': 25, 'Carbohydrates': 60, 'Fat': 15}
    goals = {
        'Caloric Value': 2000,
        'Protein': 75,
        'Carbohydrates': 250,
        'Fat': 65,
    }
    handler.set_daily_goal(goals)
    handler.update_daily_intake(intake)
    print("\nUser data after updating data.")
    print(handler.get_user_data())

    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\nGoals for {today}:")
    print(handler.get_goals_for_date(today))

    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\nIntake for {today}:")
    print(handler.get_intake_for_date(today))
