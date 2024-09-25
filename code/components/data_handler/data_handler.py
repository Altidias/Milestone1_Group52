import pandas as pd
import os
import xml.etree.ElementTree as ET
import sys
from datetime import datetime

class DataHandler:
    def __init__(self, db_path='../data/Food_Nutrition_Dataset.csv', user_data_path='../data/user.xml'):
        self.db_path = db_path
        self.user_data_path = user_data_path
        self.database_df = None
        self.user_data = None
        self.load_database()
        self.load_user_data()

    def load_database(self):
        try:
            self.database_df = pd.read_csv(self.db_path)
            print("Database loaded successfully.")
        except Exception as e:
            print(f"An error occurred while loading the database: {e}")
            sys.exit(1)

    def load_user_data(self):
        if os.path.exists(self.user_data_path):
            try:
                tree = ET.parse(self.user_data_path)
                root = tree.getroot()
                self.user_data = self.xml_to_dict(root)
                print("User data loaded successfully.")
            except Exception as e:
                print(f"An error occurred while loading user data: {e}")
                sys.exit(1)
        else:
            print("User data not found.")
            self.user_data = {'daily_intake': {}, 'goals': {}}
            self.save_user_data()

    def xml_to_dict(self, element):
        result = {}
        for child in element:
            if len(child) == 0:
                result[child.tag] = child.text
            else:
                result[child.tag] = self.xml_to_dict(child)
        return result

    def save_user_data(self):
        try:
            root = ET.Element("UserData")
            self.dict_to_xml(self.user_data, root)
            tree = ET.ElementTree(root)
            tree.write(self.user_data_path, encoding="utf-8", xml_declaration=True)
            print("User data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving user data: {e}")

    def dict_to_xml(self, tag, d):
        elem = ET.Element(tag)
        for key, val in d.items():
            child = ET.Element(key)
            if isinstance(val, dict):
                self.dict_to_xml(key, val)
            else:
                child.text = str(val)
            elem.append(child)
        return elem

    def update_daily_intake(self, food_item, quantity):
        today = datetime.now().strftime('%d-%m-%Y')
        if today not in self.user_data['daily_intake']:
            self.user_data['daily_intake'][today] = {}
        
        for nutrient, value in food_item.items():
            if nutrient != 'food':
                if nutrient not in self.user_data['daily_intake'][today]:
                    self.user_data['daily_intake'][today][nutrient] = 0
                self.user_data['daily_intake'][today][nutrient] += value * (quantity / 100)
        
        self.save_user_data()

    def set_daily_goal(self, nutrients):
        self.user_data['goals'] = nutrients
        self.save_user_data()

    def get_database(self):
        return self.database_df

    def get_user_data(self):
        return self.user_data

# example:
if __name__ == "__main__":
    handler = DataHandler()
    print(handler.get_database().head())
    print(handler.get_user_data())

