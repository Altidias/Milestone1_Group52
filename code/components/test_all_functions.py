import unittest
import pandas as pd
from searching.search import SearchHandler
from data_handler.data_handler import DataHandler
from tracker.tracker import TrackerHandler
import os
import tempfile
from datetime import datetime, timedelta
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
        if hasattr(self, 'search_handler'):
            del self.search_handler

    def test_search_food(self):
        results = self.search_handler.search_food("app")
        self.assertFalse(results.empty)
        self.assertIn('apple', results['food'].str.lower().tolist())

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
        similarities = []
        for name in results['food']:
            similarity = SequenceMatcher(None, query, name.lower()).ratio()
            similarities.append(similarity)
        self.assertEqual(similarities, sorted(similarities, reverse=True))

        empty_results = self.search_handler.search_food("qwertyuiop")
        self.assertTrue(empty_results.empty)

        all_results = self.search_handler.search_food("")
        self.assertFalse(all_results.empty)
        self.assertEqual(len(all_results), len(self.search_handler.database_df))


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
        if self.data_handler.conn:
            self.data_handler.conn.close()
        self.temp_dir.cleanup()

    def test_load_database(self):
        self.assertIsNotNone(self.data_handler.database_df)
        self.assertEqual(len(self.data_handler.database_df), 10)

    def test_update_daily_intake(self):
        nutrients = {'Caloric Value': 52, 'Protein': 0.3}
        today = datetime.now().strftime('%Y-%m-%d')
        self.data_handler.update_daily_intake(nutrients, 2, today)
        retrieved_intake = self.data_handler.get_intake_for_date(today)
        self.assertAlmostEqual(retrieved_intake['Caloric Value'], 104)
        self.assertAlmostEqual(retrieved_intake['Protein'], 0.6)

    def test_update_daily_intake_skips_non_nutrient(self):
        nutrients = {'food': 'apple', 'Nutrition Density': 10}
        today = datetime.now().strftime('%Y-%m-%d')
        self.data_handler.update_daily_intake(nutrients, 1, today)
        intake = self.data_handler.get_intake_for_date(today)
        self.assertEqual(intake, {}, "Intake should be empty as non-nutrient keys are skipped.")

    def test_update_daily_intake_records_nutrient(self):
        nutrients = {'Caloric Value': 100}
        today = datetime.now().strftime('%Y-%m-%d')
        self.data_handler.update_daily_intake(nutrients, 1, today)
        intake = self.data_handler.get_intake_for_date(today)
        self.assertEqual(intake, {'Caloric Value': 100}, "Valid nutrient should be recorded in intake.")
        
    def test_update_daily_intake_exception_handling(self):
        self.data_handler.conn.close()
        nutrients = {'Caloric Value': 100}
        with self.assertRaises(Exception):
            self.data_handler.update_daily_intake(nutrients)
        self.data_handler.init_user_data()

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

    def test_update_daily_intake_exception(self):
        self.data_handler.conn.close() 
        with self.assertRaises(Exception):
            self.data_handler.update_daily_intake({'Caloric Value': 100})
        self.data_handler.init_user_data()  

    def test_set_daily_goal_exception(self):
        self.data_handler.conn.close()  
        with self.assertRaises(Exception):
            self.data_handler.set_daily_goal({'Caloric Value': 2000})
        self.data_handler.init_user_data()  

    def test_get_user_data_exception(self):
        self.data_handler.conn.close() 
        user_data = self.data_handler.get_user_data()
        self.assertEqual(user_data, {'daily_intake': {}, 'current_goals': {}, 'historical_goals': {}})
        self.data_handler.init_user_data()  

    def test_get_goals_for_date_exception(self):
        self.data_handler.conn.close()
        goals = self.data_handler.get_goals_for_date(datetime.now().strftime('%Y-%m-%d'))
        self.assertEqual(goals, {})
        self.data_handler.init_user_data()  

    def test_get_intake_for_date_exception(self):
        self.data_handler.conn.close() 
        intake = self.data_handler.get_intake_for_date(datetime.now().strftime('%Y-%m-%d'))
        self.assertEqual(intake, {})
        self.data_handler.init_user_data() 

    def test_get_goals_for_date_with_zero_values(self):
        goals = {'Caloric Value': 0.0, 'Protein': 50.0}
        self.data_handler.set_daily_goal(goals)
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_goals = self.data_handler.get_goals_for_date(today)
        expected_goals = {'Protein': 50.0}  
        self.assertEqual(retrieved_goals, expected_goals)

    def test_get_goals_for_date_no_goals(self):
        today = datetime.now().strftime('%Y-%m-%d')
        retrieved_goals = self.data_handler.get_goals_for_date(today)
        self.assertEqual(retrieved_goals, {})


class TestTrackerHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_db_path = os.path.join(self.temp_dir.name, 'test_food_db.csv')
        self.temp_user_db_path = os.path.join(self.temp_dir.name, 'test_user_db.db')

        pd.DataFrame({
            'food': ['apple', 'banana', 'chicken breast'],
            'Caloric Value': [52, 89, 165],
            'Protein': [0.3, 1.1, 31],
            'Carbohydrates': [14, 23, 0],
            'Fat': [0.2, 0.3, 3.6]
        }).to_csv(self.temp_db_path, index=False)

        self.data_handler = DataHandler(db_path=self.temp_db_path, user_data_path=self.temp_user_db_path)
        self.search_handler = SearchHandler(data_handler=self.data_handler)
        self.tracker_handler = TrackerHandler(data_handler=self.data_handler, search_handler=self.search_handler)

    def tearDown(self):
        if self.data_handler.conn:
            self.data_handler.conn.close()
        self.temp_dir.cleanup()

    def test_set_daily_goal(self):
        goals = {'Caloric Value': 2000.0, 'Protein': 50.0, 'Carbohydrates': 300.0, 'Fat': 70.0}
        self.tracker_handler.set_daily_goal(goals)
        retrieved_goals = self.tracker_handler.get_goal()
        self.assertEqual(retrieved_goals, goals)

    def test_log_food_intake(self):
        today = datetime.now().strftime('%Y-%m-%d')
        self.tracker_handler.log_food_intake('apple', 2, today)
        daily_intake = self.tracker_handler.get_daily_intake(today)
        expected_intake = {'Caloric Value': 104, 'Protein': 0.6, 'Carbohydrates': 28, 'Fat': 0.4}
        for nutrient, value in expected_intake.items():
            self.assertAlmostEqual(daily_intake.get(nutrient, 0), value)

    def test_check_goal_progress(self):
        today = datetime.now().strftime('%Y-%m-%d')
        self.tracker_handler.set_daily_goal({'Caloric Value': 2000.0, 'Protein': 50.0})
        self.tracker_handler.log_food_intake('apple', 2, today)
        progress = self.tracker_handler.check_goal_progress(today)
        expected_progress = {
            'Caloric Value': 104 / 2000.0,
            'Protein': 0.6 / 50.0
        }
        for nutrient, value in expected_progress.items():
            self.assertAlmostEqual(progress.get(nutrient, 0), value)

    def test_overall_progress(self):
        today = datetime.now().strftime('%Y-%m-%d')
        self.tracker_handler.set_daily_goal({'Caloric Value': 2000.0, 'Protein': 50.0})
        self.tracker_handler.log_food_intake('apple', 2, today)
        overall_progress = self.tracker_handler.overall_progress(today)
        expected_progress = ((104 / 2000.0) + (0.6 / 50.0)) / 2
        self.assertAlmostEqual(overall_progress, expected_progress)

    def test_get_daily_intake(self):
        self.tracker_handler.log_food_intake('chicken breast', 1)
        daily_intake = self.tracker_handler.get_daily_intake()
        self.assertAlmostEqual(daily_intake.get('Caloric Value', 0), 165)
        self.assertAlmostEqual(daily_intake.get('Protein', 0), 31)


    def test_get_goal(self):
        goals = {'Caloric Value': 1800.0, 'Protein': 65.0}
        self.tracker_handler.set_daily_goal(goals)
        retrieved_goals = self.tracker_handler.get_goal()
        self.assertEqual(retrieved_goals, goals)


    def test_get_daily_intake_no_data(self):
        daily_intake = self.tracker_handler.get_daily_intake()
        self.assertEqual(daily_intake, {})

    def test_get_goal_no_data(self):
        retrieved_goals = self.tracker_handler.get_goal()
        self.assertEqual(retrieved_goals, {})

    def test_reset_user_data(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 2000.0})
        self.tracker_handler.log_food_intake('apple', 1)
        self.data_handler.reset_user_data()
        self.assertEqual(self.tracker_handler.get_daily_intake(), {})
        self.assertEqual(self.tracker_handler.get_goal(), {})

    def test_log_food_intake_invalid_food(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.log_food_intake('nonexistent food', 1)

    def test_log_food_intake_date_none(self):
        self.tracker_handler.log_food_intake('apple', 1) 
        today = datetime.now().strftime('%Y-%m-%d')
        daily_intake = self.tracker_handler.get_daily_intake(today)
        self.assertGreater(len(daily_intake), 0)

    def test_log_food_intake_specific_date(self):
        specific_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        self.tracker_handler.log_food_intake('apple', 1, date=specific_date)
        daily_intake = self.tracker_handler.get_daily_intake(specific_date)
        self.assertGreater(len(daily_intake), 0)

    def test_check_goal_progress_no_intake(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 2000.0})
        progress = self.tracker_handler.check_goal_progress()
        self.assertEqual(progress, {'Caloric Value': 0})

    def test_check_goal_progress_no_goals(self):
        self.tracker_handler.log_food_intake('apple', 1)
        progress = self.tracker_handler.check_goal_progress()
        self.assertEqual(progress, {})

    def test_overall_progress_no_goals(self):
        self.tracker_handler.log_food_intake('apple', 1)
        overall_progress = self.tracker_handler.overall_progress()
        self.assertEqual(overall_progress, 0)

    def test_overall_progress_no_intake(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 2000.0})
        overall_progress = self.tracker_handler.overall_progress()
        self.assertEqual(overall_progress, 0)

    def test_get_daily_intake_specific_date(self):
        specific_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        self.tracker_handler.log_food_intake('apple', 1, date=specific_date)
        daily_intake = self.tracker_handler.get_daily_intake(specific_date)
        self.assertGreater(len(daily_intake), 0)

    def test_get_goal_specific_date(self):
        specific_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        goals = {'Caloric Value': 1800.0, 'Protein': 65.0}
        self.tracker_handler.set_daily_goal(goals, date=specific_date)
        retrieved_goals = self.tracker_handler.get_goal(specific_date)
        self.assertEqual(retrieved_goals, goals)

    def test_check_goal_progress_zero_goal(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 0.0, 'Protein': 50.0})
        self.tracker_handler.log_food_intake('apple', 2)
        progress = self.tracker_handler.check_goal_progress()
        expected_progress = {
            'Protein': 0.6 / 50.0
        }
        self.assertNotIn('Caloric Value', progress)
        self.assertIn('Protein', progress)
        self.assertAlmostEqual(progress.get('Protein', 0), expected_progress['Protein'])

    def test_overall_progress_zero_goal(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 0.0, 'Protein': 0.0})
        self.tracker_handler.log_food_intake('apple', 2)
        overall_progress = self.tracker_handler.overall_progress()

        self.assertEqual(overall_progress, 0)

    def test_overall_progress_zero_and_nonzero_goals(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 0.0, 'Protein': 50.0})
        self.tracker_handler.log_food_intake('apple', 2)
        overall_progress = self.tracker_handler.overall_progress()
        expected_progress = (0.6 / 50.0)
        self.assertAlmostEqual(overall_progress, expected_progress)

    def test_check_goal_progress_goal_zero_intake_zero(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 0.0})
        progress = self.tracker_handler.check_goal_progress()
        self.assertEqual(progress, {})

    def test_check_goal_progress_goal_zero_intake_exists(self):
        self.tracker_handler.set_daily_goal({'Caloric Value': 0.0})
        self.tracker_handler.log_food_intake('apple', 1)
        progress = self.tracker_handler.check_goal_progress()
        self.assertEqual(progress, {})

    def test_check_goal_progress_intake_not_in_goal(self):
        self.tracker_handler.set_daily_goal({'Protein': 50.0})
        self.tracker_handler.log_food_intake('banana', 1)
        progress = self.tracker_handler.check_goal_progress()
        self.assertIn('Protein', progress)
        self.assertNotIn('Caloric Value', progress)
        self.assertNotIn('Carbohydrates', progress)

    def test_check_goal_progress_all_goals_zero(self):
        goals = {'Caloric Value': 0.0, 'Protein': 0.0, 'Fat': 0.0}
        self.tracker_handler.set_daily_goal(goals)
        self.tracker_handler.log_food_intake('apple', 1)
        progress = self.tracker_handler.check_goal_progress()
        self.assertEqual(progress, {})

    def test_overall_progress_with_no_goals(self):
        self.data_handler.reset_user_data()
        overall_progress = self.tracker_handler.overall_progress()
        self.assertEqual(overall_progress, 0)

    def test_overall_progress_with_no_intake(self):
        self.tracker_handler.set_daily_goal({'Protein': 50.0})
        overall_progress = self.tracker_handler.overall_progress()
        self.assertEqual(overall_progress, 0)

    def test_overall_progress_with_zero_goals_and_intake(self):
        self.tracker_handler.set_daily_goal({'Protein': 0.0})
        overall_progress = self.tracker_handler.overall_progress()
        self.assertEqual(overall_progress, 0)

    def test_log_food_intake_quantity_zero(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.log_food_intake('apple', 0)

    def test_log_food_intake_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.log_food_intake('apple', -1)

    def test_set_daily_goal_invalid_data(self):
        with self.assertRaises(TypeError):
            self.tracker_handler.set_daily_goal('invalid data')

    def test_set_daily_goal_empty_dict(self):
        self.tracker_handler.set_daily_goal({})
        retrieved_goals = self.tracker_handler.get_goal()
        self.assertEqual(retrieved_goals, {})

    def test_get_daily_intake_invalid_date(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.get_daily_intake(date='invalid date')

    def test_get_goal_invalid_date(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.get_goal(date='invalid date')

    def test_check_goal_progress_invalid_date(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.check_goal_progress(date='invalid date')

    def test_overall_progress_invalid_date(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.overall_progress(date='invalid date')

    def test_log_food_intake_none_food_name(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.log_food_intake(None, 1)

    def test_log_food_intake_empty_food_name(self):
        with self.assertRaises(ValueError):
            self.tracker_handler.log_food_intake('', 1)
