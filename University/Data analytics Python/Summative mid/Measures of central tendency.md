
Measures_of_Central_Tendency_and_Dispersion_lab2

```


mean_satisfaction = data['Overall Satisfaction Rating'].mean()

median_satisfaction = data['Overall Satisfaction Rating'].median()

  
  

print("mean_satisfaction:",mean_satisfaction)

print("median_satisfaction:",median_satisfaction)

-----------------------------------------------------------------------------

mean_visit_frequency = data['Visit Frequency (times/week)'].mean()

median_visit_frequency = data['Visit Frequency (times/week)'].median()

  

print("mean_visit_frequency:",mean_visit_frequency)

print("median_visit_frequency:",median_visit_frequency)

-----------------------------------------------------------------------------

mode_coffee_type = data['Favorite Coffee Type'].mode()[0]  # The mode() function can return multiple values; we'll take the first one if there's more than one.

  

print("mode_coffee_type:",mode_coffee_type)

-----------------------------------------------------------------------------

grades=pd.read_csv("Students_Scores.csv")

grades.head()

min_score_A = grades['Class A Scores'].min()

max_score_A = grades['Class A Scores'].max()

  

min_score_B = grades['Class B Scores'].min()

max_score_B = grades['Class B Scores'].max()

  
  

range_score_Class_A = max_score_A - min_score_A

range_score_Class_B = max_score_B - min_score_B

  

print("range_score_Class_A:",range_score_Class_A)

print("range_score_Class_B:",range_score_Class_B)

-----------------------------------------------------------------------------

# prompt: find the style of the above the code to find the variance_score

  

variance_score_Class_A = grades['Class A Scores'].var()

variance_score_Class_B = grades['Class B Scores'].var()

  

print("variance_score_Class_A:",variance_score_Class_A)

print("variance_score_Class_B:",variance_score_Class_B)

-----------------------------------------------------------------------------
# prompt: the same above style find the std_deviation

  

std_deviation_score_Class_A = grades['Class A Scores'].std()

std_deviation_score_Class_B = grades['Class B Scores'].std()

  

print("std_deviation_score_Class_A:",std_deviation_score_Class_A)

print("std_deviation_score_Class_B:",std_deviation_score_Class_B)

-----------------------------------------------------------------------------

# prompt: find the style of the above the code to find the Interquartile range

  

# **Interquartile range**

Q1_class_A = grades['Class A Scores'].quantile(0.25)

Q3_class_A = grades['Class A Scores'].quantile(0.75)

IQR_class_A = Q3_class_A - Q1_class_A

  

Q1_class_B = grades['Class B Scores'].quantile(0.25)

Q3_class_B = grades['Class B Scores'].quantile(0.75)

IQR_class_B = Q3_class_B - Q1_class_B

  

print("IQR_class_A:",IQR_class_A)

print("IQR_class_B:",IQR_class_B)

-----------------------------------------------------------------------------
mean_score_class_A = grades['Class A Scores'].mean()

mean_score_class_B = grades['Class B Scores'].mean()

  

cv_class_A = std_deviation_score_Class_A / mean_score_class_A

cv_class_B = std_deviation_score_Class_B / mean_score_class_B

  

print("cv_class_A:",cv_class_A)

print("cv_class_B:",cv_class_B)
```