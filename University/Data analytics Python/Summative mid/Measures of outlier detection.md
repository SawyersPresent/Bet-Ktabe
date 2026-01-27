Measures of Position, Outlier detections, Relationship Analysis_LAB3.ipynb


```
import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

import numpy as np

from scipy import stats

  

data=pd.read_csv("marathon_data.csv")

data.head()

----------------------------------------------------------------------------------

  

# Assuming the dataset has columns named 'Age' and 'Finishing_Time' for the analysis

# Calculate Percentiles for Age and Finishing Time

percentiles_age = np.percentile(data['Age'], [10, 25, 50, 75, 90])

percentiles_finishing_time = np.percentile(data['Finishing Time'], [10, 25, 50, 75, 90])

  

print("percentiles_age:\n",percentiles_age)

print("percentiles_finishing_time\n",percentiles_finishing_time)

----------------------------------------------------------------------------------


# Calculate Quartiles for Age and Finishing Time (equivalent to 25th, 50th, and 75th percentiles)

quartiles_age = np.percentile(data['Age'], [25, 50, 75])

quartiles_finishing_time = np.percentile(data['Finishing Time'], [25, 50, 75])

  
  

print("quartiles_age:\n",quartiles_age)

print("quartiles_finishing_time\n",quartiles_finishing_time)

----------------------------------------------------------------------------------

# Calculate Deciles for Age and Finishing Time

deciles_age = np.percentile(data['Age'], np.arange(10, 100, 10))

deciles_finishing_time = np.percentile(data['Finishing Time'], np.arange(10, 100, 10))

print("deciles_age:\n",deciles_age)

print("deciles_finishing_time\n",deciles_finishing_time)

----------------------------------------------------------------------------------

# Calculate Z-scores for Age and Finishing Time

z_scores_age = stats.zscore(data['Age'])

z_scores_finishing_time = stats.zscore(data['Finishing Time'])

  

# Find the range of Z-scores for Age and Finishing Time

z_score_range_age = (z_scores_age.min(), z_scores_age.max())

z_score_range_finishing_time = (z_scores_finishing_time.min(), z_scores_finishing_time.max())

print("z_score_range_age:\n",z_score_range_age)

print("z_score_range_finishing_time\n",z_score_range_finishing_time)

----------------------------------------------------------------------------------

sns.boxplot(y=data['Finishing Time'])

plt.title('Boxplot of Finishing Time')

  

plt.tight_layout()

plt.show()
----------------------------------------------------------------------------------
sns.boxplot(y=data['Age'])

plt.title('Boxplot of Age')

  

plt.tight_layout()

plt.show()

----------------------------------------------------------------------------------
#Outlier detection

import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

  

credit_card_data=pd.read_csv("credit_card_transactions.csv")

# Data Exploration: Descriptive statistics

credit_card_data.describe()


----------------------------------------------------------------------------------
# Using Zscore
from scipy import stats

  

z_scores = stats.zscore(credit_card_data['Transaction Amount'])

credit_card_data['Z-scores'] = z_scores

outliers_z_lower = credit_card_data[(z_scores < -3)]

outliers_z_upper = credit_card_data[(z_scores > 3)]

  

print(len(outliers_z_lower))

print(len(outliers_z_upper))
------------------------------
from scipy import stats

  

z_scores = stats.zscore(credit_card_data['Customer Average Transaction'])

credit_card_data['Z-scores'] = z_scores

outliers_z_lower = credit_card_data[(z_scores < -3)]

outliers_z_upper = credit_card_data[(z_scores > 3)]

  

print(len(outliers_z_lower))

print(len(outliers_z_upper))


----------------------------------------------------------------------------------


# IQR

Q1 = credit_card_data['Transaction Amount'].quantile(0.25)

Q3 = credit_card_data['Transaction Amount'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

  

outliers_iqr_lower = credit_card_data[(credit_card_data['Transaction Amount'] < lower_bound)]

outliers_iqr_upper = credit_card_data[(credit_card_data['Transaction Amount'] > upper_bound)]

  

print(len(outliers_iqr_lower))

print(len(outliers_iqr_upper))

Q1 = credit_card_data['Customer Average Transaction'].quantile(0.25)

Q3 = credit_card_data['Customer Average Transaction'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

  

outliers_iqr_lower = credit_card_data[(credit_card_data['Customer Average Transaction'] < lower_bound)]

outliers_iqr_upper = credit_card_data[(credit_card_data['Customer Average Transaction'] > upper_bound)]

  

print(len(outliers_iqr_lower))

print(len(outliers_iqr_upper))


----------------------------------------------------------------------------------


plt.figure(figsize=[10,8])

sns.boxplot(x=credit_card_data['Customer Average Transaction'])

plt.title('Box Plot of Customer Average Transaction')

plt.show()

----------------------------------------------------------------------------------

# Density plot
plt.figure(figsize=[10,8])

sns.kdeplot(credit_card_data['Transaction Amount'], shade=True)

plt.title('Density Plot of Transaction Amount')

plt.show()


----------------------------------------------------------------------------------

# Contingency tables

contingency_table = pd.crosstab(data['Gender'], data['Category'], margins=True)

contingency_table

# Calculate row percentages

  

row_percentages = contingency_table.div(contingency_table['All'], axis=0) * 100

row_percentages

# Calculate column percentages

column_percentages = contingency_table.div(contingency_table.loc['All'], axis=1) * 100

column_percentages


sns.scatterplot(data=data, x='Age', y='Finishing Time', alpha=0.6)  # Adjust 'Finishing Time (minutes)' as needed

  

plt.title('Age vs. Finishing Time')

plt.xlabel('Age')

plt.ylabel('Finishing Time (minutes)')  # Adjust label as per your conversion

plt.show()


----------------------------------------------------------------------------------

import matplotlib.pyplot as plt

import numpy as np

  

# Generating synthetic data for examples

  

# Trend Identification example data (Positive Linear Relationship)

np.random.seed(0)  # For reproducibility

x_linear = np.random.rand(100) * 100

y_linear = x_linear * 0.5 + np.random.normal(10, 10, size=x_linear.shape)

  

# Strength and Nature of Relationship example data (Exponential Relationship)

x_exponential = np.random.rand(100) * 10

y_exponential = np.exp(x_exponential) + np.random.normal(0, 60, size=x_exponential.shape)

  

# Creating plots

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

  

# Trend Identification: Positive Linear Relationship

axs[0].scatter(x_linear, y_linear, color='blue')

axs[0].set_title('Positive Linear Relationship')

axs[0].set_xlabel('X Value')

axs[0].set_ylabel('Y Value')

  

# Strength and Nature of Relationship: Exponential Relationship

axs[1].scatter(x_exponential, y_exponential, color='red')

axs[1].set_title('Exponential Relationship')

axs[1].set_xlabel('X Value')

axs[1].set_ylabel('Y Value')

  

plt.tight_layout()

plt.show()


----------------------------------------------------------------------------------


corr = data[['Finishing Time','Age']].corr()

  

# Now, let's draw the heatmap

plt.figure(figsize=(10, 8))  # Adjust the size of the heatmap as needed

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, cbar_kws={"shrink": .5})

plt.title('Correlation Heatmap')

plt.show()



----------------------------------------------------------------------------------



import seaborn as sns

import matplotlib.pyplot as plt

  

# Load the Iris dataset

iris = sns.load_dataset('iris')

  

# Calculate the correlation matrix

corr = iris.corr()

  

# Set up the matplotlib figure

plt.figure(figsize=(10, 8))

  

# Draw the heatmap with the mask and correct aspect ratio

sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5, cbar_kws={"shrink": .5})

  

# Adding title

plt.title('Correlation Matrix of Iris Dataset Features')

  

# Show the plot

plt.show()



----------------------------------------------------------------------------------


import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

  

# Sample data: Monthly sales figures for a year

data = {

    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    'Sales': [200, 220, 250, 275, 300, 320, 330, 310, 295, 280, 270, 300]

}

df = pd.DataFrame(data)

# Create the line chart

sns.lineplot(data=df, x='Month', y='Sales')

  

# Adding titles and labels for clarity

plt.title('Monthly Sales Figures')

plt.xlabel('Month')

plt.ylabel('Sales')

  

# Show the plot

plt.show()
```


- Measures of position
- outlier detection
- z- score
- IQR
- box plot
- density plot
- contingency tables
- scatter plot
- heatmap