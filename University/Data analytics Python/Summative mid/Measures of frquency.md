
```
frequency = df['Complaint Type'].value_counts().sort_values()


frequency

-----------------------------------------------------------------------------
# Relative Frequency

total_complaints = df['Complaint Type'].count()

relative_frequency = (frequency / total_complaints) * 100

  

relative_frequency

-----------------------------------------------------------------------------
cumulative_frequency = frequency.cumsum()

cumulative_frequency



cumulative_relative_frequency = cumulative_frequency / total_complaints * 100

  

cumulative_relative_frequency

-----------------------------------------------------------------------------

import matplotlib.pyplot as plt

  

# Directly read complaint types and their counts from df for the pie chart

complaint_counts = df['Complaint Type'].value_counts()

  

# Plotting the pie chart

plt.figure(figsize=(10, 7))

plt.pie(complaint_counts, labels=df['Complaint Type'].unique(), autopct='%1.1f%%',startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])

plt.title('Ratio of Each Type of Complaint to Total Complaints')

plt.show()

-----------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.hist(df['Resolution Time (Days)'], bins=range(1, 9), color='skyblue', edgecolor='black')

plt.title('Histogram of Resolution Time (Days)')

plt.xlabel('Resolution Time (Days)')

plt.ylabel('Number of Complaints')

plt.show()

-----------------------------------------------------------------------------

grouped_data = df.groupby(['Customer Region', 'Complaint Type']).size().unstack(fill_value=0)

  

# Now, let's plot bar charts for each region with Complaint Types

grouped_data.plot(kind='bar', figsize=(14, 8), width=0.8)

plt.title('Number of Complaints by Type in Each Region')

plt.xlabel('Customer Region')

plt.ylabel('Number of Complaints')

plt.xticks(rotation=0)  # Keep the region labels horizontal for clarity

plt.legend(title='Complaint Type')

plt.show()

-----------------------------------------------------------------------------

grouped = df.groupby(['Customer Region', 'Complaint Type']).count()

  

grouped
-----------------------------------------------------------------------------

grouped = df.groupby(['Customer Region', 'Complaint Type']).count()

grouped = grouped['Record ID'].reset_index(name='Count')

pivot_table = grouped.pivot(index='Customer Region', columns='Complaint Type', values='Count')

pivot_table.plot(kind='bar', figsize=(14, 8), width=0.8)

plt.title('Number of Complaints by Type in Each Region')

plt.xlabel('Customer Region')

plt.ylabel('Number of Complaints')

plt.xticks(rotation=0)

plt.legend(title='Complaint Type')

plt.show()

x = 5

y='Non-negative' if x >= 0 else 'Negative'

print(y)
```