# Software Design Document

## Project Name: Nutrition App Development
## Group Number: 52

## Team members

| Student Number | Name                            | 
|----------------|---------------------------------|
| s5278113       | Jacob Barany                    |
| s5345670       | Glyza Lou Sim                   | 
| s5357200       | Chathumika Dimukthi Wijesinghe  | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification: An easy all in one food nutritional database and manager is hard for most people to access, many people dont like the fact that various existing applications require internet connectivity at all times and may worry about their private information being leaked. This system is made to provide user friendly access to food nutrition information without the need for internet access. Many people lack a good way to manage their diet and easily search for a wide range of nutritional information on specific foods, which is specifically important for people with health complications or people who just want to be healthier. These people may need to follow some dietary guidelines, for which this system aims to provide an easy way to track daily caloric/nutritional intake.
- Dataset: The provided **Food_Nutrition_Dataset.csv** database will be used to retrieve food specific nutritional information.
- Data Input/Output: 
  - Data Input: 
    - **Food Search**: Users can input the name of a food item to search for its nutritional information.
    - **Data Filtering**: Users can set advanced filters to search for foods that meet specific nutritional ranges/levels.
    - **Nutrition Tracker**: Users can input their daily intake specifying the food items and quantity (weight or servings) 
    - **Goal Setting**: Users can input/set dietary goals for things such as caloric intake or specific nutritional requirements.
  - Data Output:
    - **Nutritional Information Display**: The GUI will display plain text nutritional information for the searched food item using a table.
    - **Visual Analysis**: The GUI will display pie and bar graphs so users can visually analyze their food's nutrition breakdown.
    - **Filtered Food Lists**: The application will filter multiple food items based on the nutrition level input filters and show them in the GUI.
    - **Progress Tracking**: The application will track the user's intake compared to their goal and provide visual and text feedback on their progress, it will allow them to save the progress into a PDF file or just diplay it on the screen.
- Target Users: 
  - Health conscious people
  - People with dietary requirements 
  - Gym goers or fitness enthusiasts
  - Personal trainers
  - Researchers 
  - Healthcare Professionals (such as dietitians and nutritionists).

### 1.2 System capabilities/overview

- System Functionality: What will the system do?
  - Search the database for a specific food item and retrieve the nutritional information.
  - Filter based searching where the database is search for any foods that match a criteria.
  - Generate and display graphs based on the searched food item.
  - Tracks users’ nutrition intake and allows for the setting of nutrition intake goals.
  - Store user related information in an external file to be able to track intake over time for example.
  - Generate user progress reports for daily intake which is compared against the goals, will allow users to select a time period to generate a report for.

- Features and Functionalities: Describe the key features and functionalities of the system.
  - Search box and button to allow users to input the name of a food item to get information on.
  - A panel to allow for the enabling and setting of level and range filters.
  - A panel to input the user's daily intake, it will have a row format where they can input or not input certain nutrients.
  - A panel to set the user's daily goal with the same format as the intake tracker.
  - A panel to display pie and bar graphs to the user which will be displayed after they search for a specific item.
  - An option to generate a progress report for a time period there will be inputs for start and end date.

### 1.3	Benefit Analysis

How will this system provide value or benefit?
- Provides motivation for users who use the daily tracking system through the visual graphs and user-friendly UI
- Promotes healthy food habits to keep users on track for their goals
- By having an app that provides quick food search and advanced filtering it helps save time for researching purposes or for calculating personal intake
- Valuable for educational purposes since the app can be used by healthcare professionals and researchers 
- Providing detailed descriptions and numbers on what a food item contains can help users make informed decisions on what they consume 
- The app can cater to a wide variety of people who have health conditions and dietary restrictions which gives the app the competitive edge

## 2. Requirements

### 2.1 User Requirements

This application will provide a simple but powerful GUI for users to interact with the system. Designed for the average non-tech-savvy individual to ensure greater accessibility.

Fictional User: A gym goer who is focused on meeting specific dietary intakes to maintain a healthy diet. This user is fairly knowledgeable on nutrition but needs an easy tool to manage daily food intake, track progress and access nutritional information 

From the user's perspective the application will:
- Allow the searching of specific foods by name and viewing of detailed nutritional information in an easy-to-read format.
- Present nutritional data visually with pie and bar graphs which helps the user understand the nutritional breakdown of different foods.
- Enable advanced filtering/searching options to find foods based on specific nutritional criteria, allowing filtering by range or levels of specific nutrients.
- Provide a daily nutrition/intake tracker to log food intake, track nutritional consumption and monitor progress towards any set goals.
- Allow the user to set and modify daily nutritional goals, showing progress from the tracker.
- The application will automatically save data after updating the tracker or their goals, the user will be able to close and re-open the program without losing any data.

### 2.2	Software Requirements
Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.
- **R1: Data Handling**
  - R1.1 The software shall load the dataset file into memory upon startup.
  - R1.2 The software shall load user data on startup.
  - R1.3 The software shall save user data whenever it is updated.

- **R2: User Interface**
  - R2.1 The software shall employ a graphical user interface to interact with the system.
  - R2.2 The software shall display nutritional data in plain text and using visual aids including pie and bar graphs.
  - R2.3 The software shall display error messages and confirmations.
  - R2.4 The software shall allow the enabling of different filter types in the search panel.
    
- **R3: Data Querying and Filtering**
  - R3.1 The software shall provide search functionality for users to query nutritional information.
  - R3.2 The software shall support data filtering, to query multiple food items that fit a criteria.
    - R3.2.1 Nutritional range filtering, allowing users to specifcy a nutrient and define a min and max.
    - R3.2.2 Nutrition level filtering, categorizing nutrient content into low, mid and high ranges.

- **R4: User Features and Tracking**
  - R4.1 The software shall include a daily nutrition tracker where users can log food items consumed.
  - R4.2 The software shall allow users to set or modify daily nutrition goals.
  - R4.3 The software shall generate and/or display reports on progress towards goals with information from the tracker.
  
- **R5: Error Handling and Logging**
  - R5.1: The software shall appropriately report any errors to the user in a simple manner.
  - R5.2: The software shall log any errors in a more detailed manner to an external file which should provide the developers to identify any bugs
  - R5.3: The software shall log all user interactions and software tasks to trace the error and figure out the problem.



### 2.3 Use Case Diagram
Provide a system-level Use Case Diagram illustrating all required features.

![Use Case Diagram](./UCD.svg)

### 2.4 Use Cases

| Use Case ID    | 001                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Search for Nutritional Information                                                                                                                                                                                                                     |
| Actors         | End Users                                                                                                                                                                                                                                              |
| Description    | The user wants to search for a specific food item's nutritional content.                                                                                                                                                                               |
| Flow of Events | 1. The user enters the name of a specific food item in the search bar.<br/>2. The system retrieves the nutritional information from the database.<br/>3. The system displays the nutritional information in text format and associated bar/pie charts. |
| Alternate Flow | 1. The user enters the name of a food item that does not exist in the database.<br/>2. A message is displayed saying "No Results Found".                                                                                                               |

| Use Case ID    | 002                                                                                                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Filter Food by Nutritional Range                                                                                                                                                                                                                                          |
| Actors         | End Users                                                                                                                                                                                                                                                                 |
| Description    | The user wants to search for foods based on the content of a specific nutrient within a range.                                                                                                                                                                            |
| Flow of Events | 1. The user selects a nutrient (e.g. calories) and specifies a min and max amount (grams).<br/>2. The system filters the foods from the database that fall within the range and creates a new list from them.<br/>3. The system displays the filtered list of food items. |
| Alternate Flow | 1. The user selects a nutrient and specifies min and max amount.<br/>2. No foods in the database match the criteria.<br/>3. A message is displayed saying "No Results Found for the Specified Range".                                                                     |

| Use Case ID    | 003                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Track Daily Nutritional Intake                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Actors         | End Users                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Description    | The user wants to log their daily food intake to monitor their intake over time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Flow of Events | 1. The user clicks the "Track Intake" button from the menu bar.<br/>2. A form panel is displayed.<br/>3. The user inputs the food items consumed and the associated quantities consumed in grams.<br/>3. The system calculates the nutrient intake by querying the database and getting the nutrient content of the specific food item and processing the specific amount for each nutrient.<br/>4. The daily intake part of the global user data structure is updated with the new total by adding the calculated amounts to the existing amounts for the current day. |
| Alternate Flow | 1. The user clicks the "Track Intake" button from the menu bar.<br/>2. A form panel is displayed.<br/>3. The user enters a food item that does not exist in the database.<br/>4. The user is then shown a message saying "Food Item Not Found, Please Enter Valid Food Name".                                                                                                                                                                                                                                                                                           |

| Use Case ID    | 004                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Set or Update Nutritional Goals                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Actors         | End Users                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Description    | The user wants to set or update their daily nutrition goals.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Flow of Events | 1. The user clicks the "Set/Update Nutrition Goals" tab in the menu bar.<br/>2. A form panel is displayed, the user does not have any previously set goals, the panel shows a table of nutrients each with unpopulated input boxes.<br/>3. The user inputs their desired amounts for any of the nutrients.<br/>4. The user clicks the save button.<br/>5. The goal section in the global user data structure is updated with the inputted goals.                                                                                                                                                                                                                                                            |
| Alternate Flow | 1. The user clicks the "Set/Update Nutrition Goals" tab in the menu bar.<br/>2. A form panel is displayed, the user already has set goals, the panel shows nutrients each with either unpopulated or populated input boxes depending on which have previously been set.<br/>3. The user inputs/overrides their desired amounts for any of the nutrients.<br/>4. The user clicks the save button.<br/>5. The user is prompted with a text box containing Yes/No buttons asking "Do You Wish to Override the Previously Set Goals?"<br/>6. The user clicks yes or no.<br/>7. If yes is clicked, the goal section in the global user data structure is updated with the inputted goals, if no nothing happens. |

| Use Case ID    | 005                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Generate Nutritional Progress Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Actors         | End Users                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Description    | The user wants to generate a nutritional progress report showing their progress towards their set goal over a certain period of time showing each day in the period.                                                                                                                                                                                                                                                                                                                                       |
| Flow of Events | 1. The user selects the "Progress Report" button in the menu bar.<br/>2. The user selects a date range to generate reports for.<br/>3. The system retrieves the user's daily intake data over the selected period along with the goal that was being used at the time.<br/>4. The system compiles the data and generates a detailed report showing how far under or over their goals they went, along with graphs.<br/>5. The user is provided with the option to download the report as a PDF or view it. |
| Alternate Flow | 1. The user selects the "Progress Report" button in the menu bar.<br/>2. The user selects a date range that has no logged data.<br/>3. The system displays a message saying "No Data Logged for the Specified Period".                                                                                                                                                                                                                                                                                     |

## 3.	Software Design and System Components 

### 3.1	Software Design
Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

**load_database()**
- Description: Loads the 'Food_Nutrition_Dataset.csv' database into memory.
- Input Parameters:
  - *db_path: str* - Path to the csv file.
- Return Value:
  - *None*
- Side Effects: Updates the global pandas.DataFrame with data extracted from the CSV file.

**search_food()**
- Description: Searches for food items based on a text query, partial matches are also returned to allow the user to select them in the GUI.
- Input Parameters:
  - *query: str* - Food name.
- Return Value:
  - *matches: pandas.DataFrame* - A dataframe containing rows where the food name partially or completely matched the query, each row represent a food item and the columns are nutrients.
- Side Effects: Updates and opens a list component in the GUI bellow the search box showing partial matches.

**filter_by_range()**
- Description: Filters food items based on a specific nutrient range.
- Input Parameters:
  - *nutrient: str* - The nutrient to filter for.
  - *min: float* - Minimum value of the nutrient.
  - *max: float* - Maximum value of the nutrient.
 - Return Value:
   - *filtered_df: pandas.DataFrame* - A dataframe containing food items that match the nutrient range criteria.
 - Side Effects: None.

**filter_by_level()**
- Description: Filters food items based on nutrient levels (low, mid, high).
- Input Parameters:
  - *nutrient: str* - The nutrient to filter for.
  - *level: str* - The nutrient level, low < 33%, mid > 33% && < 66%, high > 66%.
- Return Value:
  - *filtered_df: pandas.DataFrame* - A dataframe containing food items that match the nutrient level criteria.
- Side Effects: None.

**generate_pie_chart()**
- Description: Generates a dynamically sized pie chart using matplotlib, embedded in a wxPython panel, to visualize a specific food items nutritional breakdown.
- Input Parameters:
  - *food_item: pandas.Series* - A series containing the nutritional data for the food item to be graphed, including nutrient names and quantities.
- Return Value:
  - *None*
- Side Effects: Updates the GUI panel by embedding the chart using the matplotlib figure which is dynamically resized to fit the dimensions.

**generate_bar_chart()**
- Description: Generates a dynamically sized bar chart using matplotlib, embedded in a wxPython panel, to visualize a specific food items nutritional breakdown.
- Input Parameters:
  - *food_item: pandas.Series* - A series containing the nutritional data for the food item to be graphed, including nutrient names and quantities.
- Return Value:
  - *None*
- Side Effects: Updates the GUI panel by embedding the chart using the matplotlib figure which is dynamically resized to fit the dimensions.

**update_daily_intake()**
- Description: Logs and tracks the user's daily food intake.
- Input Parameters:
  - *food_item: pandas.Series* - A series containing the nutritional data for the food item.
  - *quantity: float* - The amount of food consumed in grams.
- Return Value: None.
- Side Effects: Updates the user's daily intake in the global user data structure, which is saved to a file to be persistent across sessions.

**set_daily_goal()**
- Description: Sets the users daily goal.
- Input Parameters:
  - *nutrients: pandas.Series* - A series of nutrient target values stored as floats.
- Return Value: None.
- Side Effects: Updates the user's daily daily in the global user data structure.

**get_goal_progress()**
- Description: Gets the difference between daily intakes and the set goals for various nutrients over a period of time and writes the results to a formatted PDF file.
- Input Parameters:
  - *start_date: str* - YYYY-MM-DD
  - *end_date: str* - YYYY-MM-DD
- Return Value:
  - *None*
- Side Effects: Generates and saves a PDF file containing a report of the user's progress towards the set daily goals for each day in the time period.

**save_user_data()**
- Description: Saves user data (all the user data stored in the global data structure, e.g intake, goals) to a XML file so that user data is persistent across sessions, if the file exists it appends.
- Input Parameters:
  - *file_path: str* - The path where the file is saved.
- Return Value: None.
- Side Effects: Writes user data to a file.

**load_user_data()**
- Description: Loads the user data saved in a XML file (if it exists).
- Input Parameters:
  - *file_path: str* - The path where the file is saved.
- Return Value: None.
- Side Effects: Writes user data to the global user data structure.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design

Screen 1: Home Page

This is the landing page of the web app. The search bar and goal tracker graph are the only main elements that are taking up the space. When a user types in a food item, those items will be displayed right below the search bar. the filter button is also placed beside the search bar for ease of use and to make users aware of the feature since it is a large database and can be difficult to find what you need. another main element when looking at the home page before any user input, the goal tracker is underlined. This indicates that it is a link, making it clear to the users that there are additional features.

![Home Screen](WF_Home_Screen.png)


![Range Filter](WF_Range_Filter.png)

![Level Filter](WF_Level_Filter.png)

![Goal Tracker](WF_Goal_Tracker.png)

![Nutrition Information](WF_Nutrition_Information.png)