# Project files description
create_tables.sql
This file contains only table creation commands. It first deletes the database and creates a new one with fresh tables all the time.

## fake_data_generator.py
This file can be used to generate new fake data for all the tables.

## Steps to run the script:

First install the faker library pip install faker
Run the script python fake_data_generator.py
fake_data.sql
This is the generated fake data from the above script.

backfill.sql
These cammands can be used to update certain attirbutes in the table as a backfill job.

===========================================================

## Tables to create:
Employee Information (FirstName, Lastname, DOB, Mobile, Email, DOB) - Kush
Employee Designation( Email, Position) - Yadav
Performance Table (EmployeeID, Performance Period(duration), Sales Target, Project Milestones, Customer Satisfaction Ratings, Performance Score(this will be calcualated using the previous 3 columns), Comments/Feedback, Overall Performance(use this column to apply adjustments) - Yadav
Review Table: Review ID, Employee ID, Reviewer ID, Review Date, Review Period, Performance Ratings, Goals/Targets, Strengths, Areas for Improvement, Actionable Steps, Training/Development Needs, Career Aspirations, Overall Assessment. - Yadav
Salary Information Table: (Employee ID, Base Salary, Bonus, Allowances, Deductions, Total Salary, Payment Frequency, Payment Method) - Yadav
Attendance/Leave Management Table: (Employee ID, Date, Attendance Status (Present/Absent), Leave Type (Sick Leave, Vacation Leave, etc.), Leave Balance) - Bhatla
Overtime Management - Bhatla
Key Performance Indicator
Salary Increment V/S Inflation Rate
Different department but same designation salary comparison
