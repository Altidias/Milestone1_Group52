from data_handler.data_handler import DataHandler

class SearchHandler:
    def __init__(self):
        self.data_handler = DataHandler()
        self.database_df = self.data_handler.get_database()

    # returns a list of matches and partial matches, use get_food_item to get via a specific name only
    def search_food(self, query):
        return self.database_df[self.database_df['food'].str.contains(query, case=False, na=False)]

    def filter_by_range(self, nutrient, min_val, max_val):
        return self.database_df[(self.database_df[nutrient] >= min_val) & (self.database_df[nutrient] <= max_val)]

    def filter_by_level(self, nutrient, level):
        max_value = self.database_df[nutrient].max()
        if level == 'low':
            return self.database_df[self.database_df[nutrient] < max_value * 0.33]
        elif level == 'mid':
            return self.database_df[(self.database_df[nutrient] >= max_value * 0.33) & (self.database_df[nutrient] < max_value * 0.66)]
        elif level == 'high':
            return self.database_df[self.database_df[nutrient] >= max_value * 0.66]
        else:
            raise ValueError("Invalid level. Use low, mid, or high.")

    def get_food_item(self, food_name):
        return self.database_df[self.database_df['food'] == food_name].iloc[0] if not self.database_df[self.database_df['food'] == food_name].empty else None

# example:
if __name__ == "__main__":
    search_handler = SearchHandler()

    search_results = search_handler.search_food("apple")
    print("Search results for 'apple':")
    print(search_results)

    range_filtered = search_handler.filter_by_range("Caloric Value", 50, 100)
    print("\nFoods with Caloric Value between 50 and 100:")
    print(range_filtered)

    level_filtered = search_handler.filter_by_level("Protein", "high")
    print("\nFoods with high protein content:")
    print(level_filtered)

    food_item = search_handler.get_food_item("apple croissant")
    print("\nNutritional information for 'apple croissant':")
    print(food_item)
