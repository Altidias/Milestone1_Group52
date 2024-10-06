from data_handler.data_handler import DataHandler
from difflib import SequenceMatcher


class SearchHandler:
    def __init__(self, data_handler=None, db_path='../data/Food_Nutrition_Dataset.csv', user_data_path='../data/user_data.db'):
        if data_handler is None:
            self.data_handler = DataHandler(db_path=db_path, user_data_path=user_data_path)
        else:
            self.data_handler = data_handler
        self.database_df = self.data_handler.get_database()

    # returns a list of matches and partial matches sorted by similarity score, use get_food_item to get via a
    # specific name only https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
    def search_food(self, query):
        matches = self.database_df[self.database_df['food'].str.contains(query, case=False, na=False)].copy()

        if matches.empty:
            return matches

        def similarity_ratio(food_name):
            return SequenceMatcher(None, query.lower(), food_name.lower()).ratio()

        matches['similarity'] = matches['food'].apply(similarity_ratio)
        sorted_matches = matches.sort_values('similarity', ascending=False).reset_index(drop=True)

        return sorted_matches.drop('similarity', axis=1)

    def filter_by_range(self, nutrient, min_val, max_val):
        return self.database_df[(self.database_df[nutrient] >= min_val) & (self.database_df[nutrient] <= max_val)]

    def filter_by_level(self, nutrient, level):
        max_value = self.database_df[nutrient].max()
        if level == 'low':
            return self.database_df[self.database_df[nutrient] < max_value * 0.33]
        elif level == 'mid':
            return self.database_df[
                (self.database_df[nutrient] >= max_value * 0.33) & (self.database_df[nutrient] < max_value * 0.66)]
        elif level == 'high':
            return self.database_df[self.database_df[nutrient] >= max_value * 0.66]
        else:
            raise ValueError("Invalid level. Use low, mid, or high.")

    def get_food_item(self, food_name):
        return self.database_df[self.database_df['food'] == food_name].iloc[0] if not self.database_df[
            self.database_df['food'] == food_name].empty else None

