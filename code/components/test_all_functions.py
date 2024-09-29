import unittest
import pandas as pd
from searching.search import SearchHandler
from data_handler.data_handler import DataHandler
import os
import tempfile
from datetime import datetime
from difflib import SequenceMatcher


class TestSearchHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_db_path = os.path.join(cls.temp_dir.name, 'test_food_db.csv')
        cls.temp_user_db_path = os.path.join(cls.temp_dir.name, 'test_user_db.db')

        pd.DataFrame({
            'food': ['apple', 'banana', 'orange', 'chicken breast', 'salmon', 'broccoli', 'brown rice', 'egg', 'avocado', 'greek yogurt'],
            'Caloric Value': [52, 89, 47, 165, 208, 55, 216, 155, 160, 59],
            'Protein': [0.3, 1.1, 0.9, 31, 20, 3.7, 5, 13, 2, 10],
            'Carbohydrates': [14, 23, 12, 0, 0, 11, 45, 1.1, 9, 3.6],
            'Fat': [0.2, 0.3, 0.1, 3.6, 13, 0.6, 1.6, 11, 15, 0.4],
            'Fiber': [2.4, 2.6, 2.4, 0, 0, 2.6, 3.5, 0, 7, 0],
            'Vitamin C': [4.6, 8.7, 53.2, 0, 3.9, 89.2, 0, 0, 10, 0]
        }).to_csv(cls.temp_db_path, index=False)

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def setUp(self):
        self.search_handler = SearchHandler(db_path=self.temp_db_path, user_data_path=self.temp_user_db_path)

    def tearDown(self):
        del self.search_handler

    def test_search_food(self):
        results = self.search_handler.search_food("app")
        self.assertFalse(results.empty)
        self.assertTrue('apple' in results.iloc[0]['food'].lower())

    def test_filter_by_range(self):
        results = self.search_handler.filter_by_range("Caloric Value", 50, 100)
        self.assertFalse(results.empty)
        self.assertTrue(all((results['Caloric Value'] >= 50) & (results['Caloric Value'] <= 100)))

    def test_filter_by_level(self):
        results = self.search_handler.filter_by_level("Protein", "high")
        self.assertFalse(results.empty)
        max_protein = self.search_handler.database_df['Protein'].max()
        self.assertTrue(all(results['Protein'] >= max_protein * 0.66))

    def test_get_food_item(self):
        item = self.search_handler.get_food_item("apple")
        self.assertIsNotNone(item)
        self.assertEqual(item['food'], "apple")

    def test_search_food_order(self):
        results = self.search_handler.search_food("app")
        self.assertFalse(results.empty)
        query = "app"
        similarities = [SequenceMatcher(None, query, name.lower()).ratio() for name in results['food']]
        self.assertEqual(similarities, sorted(similarities, reverse=True))


class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_db_path = os.path.join(self.temp_dir.name, 'test_food_db.csv')
        self.temp_user_db_path = os.path.join(self.temp_dir.name, 'test_user_db.db')

        pd.DataFrame({
            'food': ['apple', 'banana', 'orange', 'chicken breast', 'salmon', 'broccoli', 'brown rice', 'egg', 'avocado', 'greek yogurt'],
            'Caloric Value': [52, 89, 47, 165, 208, 55, 216, 155, 160, 59],
            'Protein': [0.3, 1.1, 0.9, 31, 20, 3.7, 5, 13, 2, 10],
            'Carbohydrates': [14, 23, 12, 0, 0, 11, 45, 1.1, 9, 3.6],
            'Fat': [0.2, 0.3, 0.1, 3.6, 13, 0.6, 1.6, 11, 15, 0.4],
            'Fiber': [2.4, 2.6, 2.4, 0, 0, 2.6, 3.5, 0, 7, 0],
            'Vitamin C': [4.6, 8.7, 53.2, 0, 3.9, 89.2, 0, 0, 10, 0]
        }).to_csv(self.temp_db_path, index=False)

        self.data_handler = DataHandler(db_path=self.temp_db_path, user_data_path=self.temp_user_db_path)

    def tearDown(self):
        self.data_handler.database_df = None 
        if self.data_handler.conn:
            self.data_handler.conn.close() 
        del self.data_handler 
        self.temp_dir.cleanup() 

    def test_load_database(self):
        self.assertIsNotNone(self.data_handler.database_df)
        self.assertEqual(len(self.data_handler.database_df), 10) 

    def test_update_daily_intake(self):
        nutrients = {'Caloric Value': 52, 'Protein': 0.3}
        self.data_handler.update_daily_intake(nutrients, 2)
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_intake = self.data_handler.get_intake_for_date(today)
        self.assertAlmostEqual(retrieved_intake['Caloric Value'], 104)
        self.assertAlmostEqual(retrieved_intake['Protein'], 0.6)

    def test_set_daily_goal(self):
        goals = {'Caloric Value': 2000, 'Protein': 50}
        self.data_handler.set_daily_goal(goals)
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_goals = self.data_handler.get_goals_for_date(today)
        self.assertEqual(retrieved_goals, goals)

    def test_get_database(self):
        db = self.data_handler.get_database()
        self.assertIsInstance(db, pd.DataFrame)
        self.assertEqual(len(db), 10)  

    def test_get_user_data(self):
        user_data = self.data_handler.get_user_data()
        self.assertIsInstance(user_data, dict)
        self.assertIn('daily_intake', user_data)
        self.assertIn('current_goals', user_data)
        self.assertIn('historical_goals', user_data)

    def test_get_goals_for_date(self):
        goals = {'Caloric Value': 2000, 'Protein': 50}
        self.data_handler.set_daily_goal(goals)
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_goals = self.data_handler.get_goals_for_date(today)
        self.assertEqual(retrieved_goals, goals)

    def test_get_intake_for_date(self):
        nutrients = {'Caloric Value': 500, 'Protein': 25}
        self.data_handler.update_daily_intake(nutrients)
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_intake = self.data_handler.get_intake_for_date(today)
        self.assertEqual(retrieved_intake, nutrients)
