import pandas as pd
data = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')
print(data.head())

overdue_tasks = data[data['OverDue'] == True]
total_overdue = len(overdue_tasks)
print(f"Total number of tasks that are overdue: {total_overdue}")
task_counts = data.groupby(['Task Group', 'Status']).size().unstack()
task_counts = task_counts[['Open', 'Closed']]
print(task_counts)


import matplotlib.pyplot as plt

data = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')
grouped_data = data[data['Status'].isin(['Open', 'Closed'])].groupby(['Task Group', 'Status']).size().unstack()
grouped_data.plot(kind='bar', stacked=False, figsize=(12, 8))
plt.title('Total Number of Open and Closed Tasks by Each Task Group')
plt.ylabel('Number of Tasks')
plt.xlabel('Task Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/workspaces/GENAI/task_group_chart.png')
plt.close()

import os
os.system("cd /workspaces/GENAI")
os.system("git add .")
os.system('git commit -m "Committing the analysis script changes"')
os.system("git push")

overdue_tasks_by_project = data[data['OverDue'] == True]
overdue_counts_by_project = overdue_tasks_by_project.groupby('project').size()
plt.figure(figsize=(12, 6))
overdue_counts_by_project.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/workspaces/GENAI/overdue_tasks_by_project.png')
plt.close()