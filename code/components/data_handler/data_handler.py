import pandas as pd
import os
import xml.etree.ElementTree as ET
import sys


class DataHandler:
    def __init__(self, db_path='../data/Food_Nutrition_Dataset.csv', user_data_path='../data/user.xml'):
        self.db_path = db_path
        self.user_data_path = user_data_path
        self.database_df = None
        self.user_data_df = None
        self.load_database()
        self.load_user_data()

    def load_database(self):
        try:
            self.database_df = pd.read_csv(self.db_path)
            print(f"Database loaded.")
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(0)

    def load_user_data(self):
        if os.path.exists(self.user_data_path):
            try:
                self.user_data_df = pd.read_xml(self.user_data_path)
                print(f"User data loaded.")
            except Exception as e:
                print(f"An error occurred: {e}")
                sys.exit(0)
        else:
            print(f"User data not found, creating it.")
            self.user_data_df = pd.DataFrame()
            self.save_user_data()

    def save_user_data(self):
        try:
            if self.user_data_df.empty:
                # Example below, final implementation will need to have dated entries for the tracker and the goal
                # set on that day, as well as the currently set goal.
                initial_data = {
                    'Calories': [2000],
                }
                self.user_data_df = pd.DataFrame(initial_data)

            self.user_data_df.to_xml(self.user_data_path, index=False, root_name='Users', row_name='User')
            print(f"User data saved.")
        except Exception as e:
            print(f"An error occurred: {e}")

