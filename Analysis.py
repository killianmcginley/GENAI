import pandas as pd
data = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')
print(data.head())

overdue_tasks = data[data['OverDue'] == True]
total_overdue = len(overdue_tasks)
print(f"Total number of tasks that are overdue: {total_overdue}")