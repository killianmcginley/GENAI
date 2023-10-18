import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')
print(df.head())
overdue_tasks = df[df['OverDue'] == True]
total_overdue = len(overdue_tasks)
print(f"Total number of tasks that are overdue: {total_overdue}")
grouped_data = df[df['Status'].isin(['Open', 'Closed'])].groupby(['Task Group', 'Status']).size().unstack()
grouped_data.plot(kind='bar', stacked=False, figsize=(12, 8))
plt.title('Total Number of Open and Closed Tasks by Each Task Group')
plt.ylabel('Number of Tasks')
plt.xlabel('Task Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/workspaces/GENAI/task_group_chart.png')
plt.close()
os.chdir("/workspaces/GENAI")
os.system("git add .")
os.system('git commit -m "Committing the analysis script changes"')
os.system("git push")
overdue_by_project = overdue_tasks.groupby('project').size()
plt.figure(figsize=(12, 6))
overdue_by_project.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import os
print(os.getcwd())