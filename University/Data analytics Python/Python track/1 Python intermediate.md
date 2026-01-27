
# Drawing stuff

## Plots

### Normal plot

```python
import matplotlib.pyplot as plt

year = []
pop = []
plt.plot(year, pop)
plt.show()
```


### Scatter plot

```python
import matplotlib.pyplot as plt

year = []
pop = []
plt.scatter(year, pop) #the change is here
plt.show()
```


#### Practice

```python
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

```


```python
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)
  

# Put the x-axis on a logarithmic scale
plt.plot(gdp_cap,life_exp)
plt.xscale('log')

# Show plot
plt.show()
```

## Histograms


```python
help(plt.hist)

values = []
plt.hist(values,bin=3) #Bins is important you use it to specify how many liek categories? you sorta want
plt.show()
```

```python
# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()
```


Practicing building histogram
build histogram

```python
# Histogram of life_exp, 15 bins
plt.hist(life_exp,bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,bins=15)


# Show and clear plot again
plt.show()
plt.clf()
```



## Customizing plots


### plot cheatsheet
```python
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

#Labelling stuff
plt.xlabel('year')
plt.ylabel('population')
plt.title('world population projections')
plt.yticks([0, 2, 4, 6, 8, 19],
		  ["0B", "2B", "4B", "6B", "8B", "10B"])
# Display the plot with plt.show()
plt.show()
```

### adding xlabel, ylabel and title
```python
x# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)


# After customizing, display the plot
plt.show()
```


### Doing ticks example
```python
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()
```

### Changing sizes of large dots. Dots customization

```python
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
```

### Making the plot colorful

```python
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()
```


#### Behind the scenes of htis

```python
# Making our own sort of colors, this is a dicitionary and will learn about later
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

```


## adding a grid 

```python
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
```



## Dictionaries

```python
#Lets create a dictionary
world = {"afghan":30.55,"allbania":20.77}

#To call them
world[albania]
```


#### Practicing dicitonaries

```python
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
```


### Printing Keys

```python
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])
```



## Dictionary part 2

### Adding dictionary, deleting dictionary, modifying dictionary

```python
world["sealand"] = 0.000027
world["key"] = value
sealand in world #to check if its actually in there
print('italy' in europe) # to print something

world["sealand"] = 0.000028 #to update
del(world["sealand"]) #to delete stuff 
```


example
```python
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe["poland"] = 'warsaw'


# Print europe
print(europe)
```


```python
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
```

### Chaining them? ig?

```python
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Print out the capital of France
print(europe['france']['population'])


# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

{'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'italy': {'capital': 'rome', 'population': 59.83}}
```


## Pandas, Part 1

```python

brics = pd.DataFrame(something)


to specify row labels specifically

brics.index = ["BR", "RU", "IN", "US"]
brics = pd.read_csv("/path/to/csvfile", index_col = 0)

```



example

```python
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict, we are adding everything into it
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

<script.py> output:
       cars_per_cap
    0           809
    1           731
    2           588
    3            18
    4           200
    5            70
    6            45
```



### Adding row labels

```python
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

# Print cars again
print(cars)
```


### Reading from CSV

```python
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)

0         US           809  United States          True
1        AUS           731      Australia         False
2        JPN           588          Japan         False
3         IN            18          India         False
4         RU           200         Russia          True
5        MOR            70        Morocco          True
6         EG            45          Egypt          True

----------------------------------------------------------------------------

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)

US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
```


## Pandas part 2

- square brackets for access
- using loc and iloc


```python
#LOC STUFF!! RAW LABELS!!
#to print stuff we use square brackets
#to specify columns
brics["country"]
brics["country", "capital"]

#so specify rows
brics[1:4]
brics[rows:columns]
type(brics["country"])

#Using advanced methods
loc #is label based
iloc #is integer position based

brics.loc["RU"] #shows stuff vertically
brics.loc[["RU"]] #shows stuff horizontally

brics.loc[["RU", "IN", "CH"]] # multipel stuff

brics.loc[["RU", "IN", "CH"], ["country", "capital"]] # to specifiy number of columns
brics.loc[:, ["country", "capital"]] # to specifiy number of columns
```


```python
#USING ILOC
brics.loc[[1,2,3]] # multipel stuff
brics.loc[1,2,3, [0,1]] # to specifiy i want 3 rows and 2 columns
brics.loc[:, [0,1]] # to specifiy number of columns
```