# Task-Completion-Scoring
A Python script for calculating the adjusted-Wald confidence intervals for task completion data. 

Script: Score_Task_Completion.py <br>
Sample Data: Fake_Task_Completion_Data.csv

## About
Scoring test data in a spreadsheet can be tedious. After each test, you may find yourself making many spreadsheet adjustments. Data samples are rarely the same size, and columns, rows, and formulas frequently need readjustment. It can be tedious.

The intent of this script is to ease the scoring process by allowing you to point to a column of data within a .csv file and score it with minimal spreadsheet manipulation. The script works for samples of any size, and is appropriate for samples obtained during moderated and unmoderated testing sessions.

## Data Preparation
The datafile should be devoid of extra columns and rows. The column names should exist within a single header row. The participant or sample number should exist in a single header column.

The data values must be numeric, either as integers (e.g. 60) or decimal values (60.0). All cells must contain a value. Blank or text-filled cells will result in a failed script.

## Usage
You will need a Python 3.10 or greater installation in order to use this script.

Convert your test data file to a .csv file, and locate which column(s) contain the task completion rate data you would like to score. Ideally, your column names do not contain spaces. For this type of scoring, your data values should be coded as '1' for success, and '0' for failure.

Find the desired column and modify the name to remove spaces. For example 'Fake Task Completion Data' should be modified to 'Fake_Task_Completion_Data'.

Be sure to resave your .csv file after you make adjustments!
Save the data file to the same directory where your script is located.

Open the script. Find the line **infile = 'Fake_Task_Completion_Data.csv'** near the bottom of the page.

Replace the 'Fake_Task_Completion_Data.csv' with the name of your file. Be sure to include the '' around the entire file name and the '.csv' extension!

Find the line **scores = df['Task_Completion_1']** at the bottom of the page. Copy the column name from your file and paste it into the brackets. Be sure to include '' surrounding the column name.

Run the script. The selected column will score and calculate the confidence interval for the sample. A statement about the population confidence 
interval should appear in the Output panel.

## Limitations
The script will fail if the sample cells contain blanks or text values, or if the data columns are uneven in length (eg. 'ragged data').

### References
Sauro, J., &; Lewis, J. R. (2016). In Quantifying the user experience: Practical statistics for user research (pp. 19–60). essay, Morgan Kaufmann.
