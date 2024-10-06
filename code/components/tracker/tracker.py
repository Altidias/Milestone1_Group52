from data_handler.data_handler import DataHandler
from searching.search import SearchHandler
import datetime


class TrackerHandler:
    def __init__(self, data_handler=None, search_handler=None):
        if search_handler is None:
            self.search_handler = SearchHandler(data_handler=self.data_handler)
        else:
            self.search_handler = search_handler
        if data_handler is None:
            self.data_handler = DataHandler()
        else:
            self.data_handler = data_handler

    def validate_date(self, date):
        if date is None:
            return datetime.date.today().strftime('%Y-%m-%d')
        elif isinstance(date, datetime.date):
            return date.strftime('%Y-%m-%d')
        elif isinstance(date, str):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
                return date
            except ValueError:
                raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        else:
            raise ValueError("Invalid date type. Use datetime.date, string 'YYYY-MM-DD', or None.")

    def log_food_intake(self, food_name, quantity, date=None):
        if not food_name or not isinstance(food_name, str):
            raise ValueError("Invalid food name provided.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        
        date = self.validate_date(date)
    
        food_item = self.search_handler.get_food_item(food_name)
        if food_item is None:
            raise ValueError(f"Food item '{food_name}' not found in database.")
    
        nutrients = food_item.to_dict()
    
        self.data_handler.update_daily_intake(nutrients, quantity, date)


    def set_daily_goal(self, nutrients, date=None):
        if not isinstance(nutrients, dict):
            raise TypeError("Nutrients must be provided as a dictionary.")
        date = self.validate_date(date)
        self.data_handler.set_daily_goal(nutrients, date)

    def get_daily_intake(self, date=None):
        date = self.validate_date(date)
        return self.data_handler.get_intake_for_date(date)
    
    def get_goal(self, date=None):
        date = self.validate_date(date)
        return self.data_handler.get_goals_for_date(date)

    def check_goal_progress(self, date=None):
        date = self.validate_date(date)
        intake = self.get_daily_intake(date)
        goal = self.data_handler.get_goals_for_date(date)
        progress = {}
        for nutrient in goal:
            if nutrient not in intake:
                progress[nutrient] = 0
            else:
                if goal[nutrient] == 0:
                    continue
                else:
                    progress[nutrient] = (intake[nutrient] / goal[nutrient])
        return progress
    
    def overall_progress(self, date=None):
        date = self.validate_date(date)
        intake = self.get_daily_intake(date)
        goal = self.data_handler.get_goals_for_date(date)
        progress = 0
        for nutrient in goal:
            if nutrient in intake:
                if goal[nutrient] == 0:
                    continue
                else:
                    progress += (intake[nutrient] / goal[nutrient])
        return progress / len(goal) if goal else 0


