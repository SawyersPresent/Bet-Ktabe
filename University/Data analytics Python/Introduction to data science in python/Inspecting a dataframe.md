
```python
df.info()
df.head() #prints first 5
```

```python
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())
print(credit_records.info())
```

## Selecting columns

```python
print(credit_records.head())
#from output use those columns to select shit
suspect = credit_records['suspect']
suspect = credit_records.suspect
print(suspect)
```


```python
# Use info() to inspect mpr
header = mpr["Dog Name"]
print(header)

# Use info() to inspect mpr
header = mpr["Dog Name"]
print(header)
0      Bayes
1    Sigmoid
2     Sparky
3    Theorem
Name: Dog Name, dtype: object
```

## Selecting rows with logic


```python
ques = 2 + 2
solu = 4

question == solu
#this return true

credit_records[credit_records.price > 20.00]
credit_records[credit_records.suspect == 'Ronald aylmer fisher']
```
