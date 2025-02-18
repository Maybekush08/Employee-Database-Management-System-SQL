import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random dates in YYYY-MM-DD format
def random_date(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

# Generate random values for Employee_Information table
employee_data = []
for i in range(1, 101):
    employee_id = i
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = random_date("1960-01-01", "2004-12-31")  # Adjust range as needed
    address = fake.address()
    city = fake.city()
    zipcode = fake.zipcode()
    gender = random.choice(['Male', 'Female'])
    mobile = fake.phone_number()
    ssn = fake.random_number(digits=9)
    company_email = fake.email()
    personal_email = fake.email()
    employee_data.append((employee_id, first_name, last_name, dob, address, city, zipcode, gender, mobile, ssn, company_email, personal_email))

performance_data = []
for employee_id in range(1, 101):
    performance_id = random.randint(1, 1000)
    cycle_start_date = random_date("2020-01-01", "2024-12-31")  # Adjust range as needed
    cycle_end_date = random_date(cycle_start_date, "2024-12-31")
    days_in_cycle = random.randint(1, 30)
    sales_revenue = random.randint(1000, 10000)
    hours_worked = random.randint(20, 200)
    project_completion_rate = round(random.uniform(0, 1), 1)
    milestones = fake.sentence()
    punctuality = round(random.uniform(0, 1), 2)
    efficiency = round(random.uniform(0, 1), 2)
    norm_efficiency = round(random.uniform(0, 1), 2)
    performance = round(random.uniform(0, 1), 2)
    performance_data.append((performance_id, employee_id, cycle_start_date, cycle_end_date, days_in_cycle, sales_revenue, hours_worked, project_completion_rate, milestones, punctuality, efficiency, norm_efficiency, performance))

# Generate random values for Review table
review_data = []
for employee_id in range(1, 101):
    review_id = random.randint(1, 100)
    reviewer_id = random.randint(1, 100)
    review_date = random_date("2020-01-01", "2024-12-31")  # Adjust range as needed
    review_period = fake.random_element(elements=('Quarterly', 'Bi-Annual', 'Annual'))
    performance_ratings = round(random.uniform(1, 5), 2)
    goals_targets = fake.sentence()
    strengths = fake.sentence()
    areas_for_improvement = fake.sentence()
    actionable_steps = fake.sentence()
    training_development_needs = fake.sentence()
    career_aspirations = fake.sentence()
    overall_assessment = fake.random_element(elements=('Excellent', 'Good', 'Fair', 'Poor'))
    review_data.append((review_id, employee_id, reviewer_id, review_date, review_period, performance_ratings, goals_targets, strengths, areas_for_improvement, actionable_steps, training_development_needs, career_aspirations, overall_assessment))

# Generate random values for ProbationEmployeesTraining table
probation_training_data = []
for employee_id in range(1, 101):
    training_id = random.randint(1, 100)
    training_type = fake.random_element(elements=('Orientation', 'Technical Training', 'Soft Skills Training'))
    training_date = random_date("2020-01-01", "2024-12-31")  # Adjust range as needed
    completion_status = fake.random_element(elements=('Completed', 'Pending'))
    probation_training_data.append((training_id, employee_id, training_type, training_date, completion_status))

# Generate random values for Department table
department_data = []
for department_id in range(1, 11):
    department_name = fake.company_suffix()
    department_data.append((department_id, department_name))

# Generate random values for Attendance table
attendance_data = []
for employee_id in range(1, 101):
    attendance_id = random.randint(1, 100)
    attendance_date = random_date("2020-01-01", "2024-12-31")  # Adjust range as needed
    start_time = fake.time(pattern='%H:%M:%S', end_datetime=None)
    end_time = fake.time(pattern='%H:%M:%S', end_datetime=None)
    attendance_data.append((attendance_id, employee_id, attendance_date, start_time, end_time))

# Generate random values for HistoryLog table
history_log_data = []
for log_id in range(1, 101):
    log_type = fake.random_element(elements=('Update', 'Insert', 'Delete'))
    log_date = random_date("2020-01-01", "2024-12-31")  # Adjust range as needed
    log_details = fake.sentence()
    employee_id = random.randint(1, 100)
    history_log_data.append((log_id, log_type, log_date, log_details, employee_id))

# Generate random values for Pay_Grades table
pay_grade_data = []
for i in range(1, 11):
    pay_grade_id = fake.word().upper()  # Assuming PayGradeID is alphanumeric
    grade_name = fake.job()
    min_salary = round(random.uniform(30000, 80000), 2)
    max_salary = round(min_salary + random.uniform(10000, 40000), 2)
    pay_grade_data.append((pay_grade_id, grade_name, min_salary, max_salary))

# Generate random values for Positions table
position_data = []
for i in range(1, 101):
    position_id = i
    position_title = fake.job()
    responsibilities = fake.text()
    qualifications = fake.text()
    department_id = random.randint(1, 10)  # Assuming 10 departments
    pay_grade_id = random.choice(pay_grade_data)[0]  # Randomly select a PayGradeID from the generated Pay_Grades data
    position_data.append((position_id, position_title, responsibilities, qualifications, department_id, pay_grade_id))

# Generate insert commands for each table
employee_insert_commands = [f"INSERT INTO Employee_Information VALUES {data};" for data in employee_data]
performance_insert_commands = [f"INSERT INTO PerformanceMetrics VALUES {data};" for data in performance_data]
review_insert_commands = [f"INSERT INTO Review VALUES {data};" for data in review_data]
probation_training_insert_commands = [f"INSERT INTO ProbationEmployeesTraining VALUES {data};" for data in probation_training_data]
department_insert_commands = [f"INSERT INTO Department VALUES {data};" for data in department_data]
attendance_insert_commands = [f"INSERT INTO Attendance VALUES {data};" for data in attendance_data]
history_log_insert_commands = [f"INSERT INTO HistoryLog VALUES {data};" for data in history_log_data]
pay_grade_insert_commands = [f"INSERT INTO Pay_Grades VALUES {data};" for data in pay_grade_data]
position_insert_commands = [f"INSERT INTO Positions VALUES {data};" for data in position_data]

# Write insert commands to file
with open('fake_data.sql', 'w') as file:
    file.write('\n'.join(employee_insert_commands))
    file.write('\n'.join(performance_insert_commands))
    file.write('\n'.join(review_insert_commands))
    file.write('\n'.join(probation_training_insert_commands))
    file.write('\n'.join(department_insert_commands))
    file.write('\n'.join(attendance_insert_commands))
    file.write('\n'.join(history_log_insert_commands))
    file.write('\n'.join(pay_grade_insert_commands))
    file.write('\n'.join(position_insert_commands))
