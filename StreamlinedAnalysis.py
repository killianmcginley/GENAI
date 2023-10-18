import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')
print(df.head())

overdue_tasks = df[df['OverDue'] == 'Yes']  # Ensured correct spelling of 'OverDue' column
total_overdue = len(overdue_tasks)
print(f"Total number of tasks that are overdue: {total_overdue}")

task_counts = df[df['Status'].isin(['Open', 'Closed'])].groupby(['Task Group', 'Status']).size().unstack()
print(task_counts)

task_counts.plot(kind='bar', stacked=False, figsize=(12, 8))
plt.title('Total Number of Open and Closed Tasks by Each Task Group')
plt.ylabel('Number of Tasks')
plt.xlabel('Task Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('task_group_chart.png')
plt.close()

overdue_by_project = overdue_tasks.groupby('project').size()
plt.figure(figsize=(12, 6))
overdue_by_project.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()