

```
something = 1
```


```
height = 100
weight = 50
bmi = height / weight * 2
```


to see what type a data is 
```
type(bmi)
```


# Python types

`int`
`str`
`bool`
`float`


## Variables


```python
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Kill yourself fag"
  
# Create a variable is_good
is_good = True

# Create a int
hello = 100 
```

## How it behaves with other stuff

```python
2 + 3
5
```

```python
'ab' + 'cd'
'abcd'
```



Script that just adds stuff

```python
# Create the variables monthly_savings and num_months
savings = 100
monthly_savings = 10
num_months = 4


# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months 

  

# Add new_savings to your savings
total_savings = new_savings + savings

# Print total_savings
print(total_savings)
```


## Changing variables

```python

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
```


## Outputting numbers in print

They have to be converted to string


```python
In [1]:
"The correct answer to this multiple choice exercise is answer number " + 2
Out[1]:
Traceback (most recent call last):
  File "<stdin>", line 72, in exceptionCatcher
    raise exception
  File "<stdin>", line 3361, in run_ast_nodes
    if (await self.run_code(code, result,  async_=asy)):
  File "<stdin>", line 3458, in run_code
    self.showtraceback(running_compiled_code=True)
  File "<stdin>", line 2066, in showtraceback
    self._showtraceback(etype, value, stb)
  File "<stdin>", line 72, in exceptionCatcher
    raise exception
  File "<stdin>", line 3441, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<stdin>", line 1, in <module>
    "The correct answer to this multiple choice exercise is answer number " + 2
TypeError: can only concatenate str (not "int") to str


In [2]:
"The correct answer to this multiple choice exercise is answer number " + str(2)  

Out[2]:
'The correct answer to this multiple choice exercise is answer number 2'
```


```python
# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

```



# Python lists


```python
fam_height = [1.73. 1.65, 1.45, 178]
```


```python
fam = ['saif', 1.73, 'zaina', 1.65]
```


you can also create sublists within a single list

```python
fam = [['saif', 1.73], ['zaina', 1.65]]

fam = [
	   ['saif', 1.73], 
	   ['zaina', 1.65]
	   ]
```


```python
# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

  

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)


<script.py> output: [11.25, 18.0, 20.0, 10.75, 9.5]
```


## Using multiple types in one list

```python
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

  

# Adapt list areas
areas = ['hallway',hall, 'kitchen', kit, "living room", liv,"bedroom", bed, "bathroom", bath]

  

# Print areas
print(areas)
```


Sublists example

```python
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

  
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

  
# Print out house
print(house)

# Print out the type of house
print(type(house))
```



# Subsetting lists


How to interact with lists, lets say we want to call the living room value 
```python
areas = [hall, kit, liv, bed, bath]
fam[3]
```

`fam[-1]` calls for basically the last object on the list


## List slicing


where the slice starts is what gets included and where the slice ends is what gets excluded
`[ start : end]`


```python
areas = [hall, kit, liv, bed, bath]
fam[3:5]
liv,bed
```

you can also do very different forms of slicing where you can leave one empty

In this case this includes everything after the second index  
```python
fam[2:]
```

In a case where we want to do a certain section we can do that with leaving the front part empty 
```python
fam[:4]
```

lets apply some of this with an exercise

## Exercise 1

```python

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

  

# Print out second element from areas
print(areas[1])


# Print out last element from areas
print(areas[-1])

  

# Print out the area of the living room
print(areas[1:-1])
```

output
```python
<script.py> output: 11.25 9.5 [11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom']
```



### Exercise 2

```python
# Using a combination of list subsetting and variable assignment, create a new variable, `eat_sleep_area`, that contains the sum of the area of the kitchen and the area of the bedroom.
# Print the new variable `eat_sleep_area`.


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


# Sum of kitchen and bedroom area: eat_sleep_area, i can add certain parts of arrays to create a variable
eat_sleep_area = areas[3] + areas[7]
  

# Print the variable eat_sleep_area
print(eat_sleep_area)
```


# Exercise 3

```python
#- Use slicing to create a list, `downstairs`, that contains the first 6 elements of `areas`.

# Do a similar thing to create a new variable, `upstairs`, that contains the last 4 elements of `areas`.

# Print both `downstairs` and `upstairs` using [`print()`](https://docs.python.org/3/library/functions.html#print).

# REMEMBER THESE NOTES
# The `start` index will be included, while the `end` index is _not_.




areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  

# Use slicing to create downstairs
downstairs = areas[:6]


# Use slicing to create upstairs
upstairs = areas[6:]

  

# Print out downstairs and upstairs
print(upstairs)
print(downstairs)
```



# Subnetting of lists

```python
# What will `house[-1][1]` return? `house`, the list of lists that you created before, is already defined for you in the workspace. You can experiment with it in the IPython Shell.
# Hint: `house[-1]` selects the last element of `house`, which is the list `["bathroom", 9.50]`. What's the result if you then subset this sublist with `[1]`? You can always try out the command in the IPython Shell!

In [1]:
house[-1]  
Out[1]:
['bathroom', 9.5]

In [2]:
house[-1][1]  
Out[2]:
9.5

```


# Manipulating lists


Normally changing stuff
```
fam = ["saif",1.65, "zaina", 1.4]
fam[2] = 1.70
```

You can change entire slices
```
fam[0:2] = ["saif", 172]
```

## adding and removing lists

```
fam + ["me", 1.79]
fam_ext = fam + ["me", 1.79]

# Deleting stuff
del(fam[2])
```


Time to practice i guess

Adding new stuff and correcting stuff
```Python
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

  

# Correct the bathroom area to 10.50
areas[-1] = 10.50

  

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

Practicing adding

```python
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,

         "bedroom", 10.75, "bathroom", 10.50]


# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]


# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

Practicing removing stuff with slicing
```python
# Please remove poolhouse
In [5]:

areas = ["hallway", 11.25, "kitchen", 18.0,  
        "chill zone", 20.0, "bedroom", 10.75,  
         "bathroom", 10.50, "poolhouse", 24.5,  
         "garage", 15.45]  

In [6]:
del(areas[-4:-2])  

In [7]:
print(areas)  

['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'garage', 15.45]
```


To create a copy of lists
```python

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
# In this case areas_copy = areas is wrong, because this is a pointer always do this when you want to create a copy of a list
areas_copy = list(areas)


# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


```


# Functions

```python
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True


# Print out type of var1
print(type(var1))


# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

```

the `help()` function assists me, i can run a function inside of it and gives me the help menu an example would be `help(max)`

```python
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)


# Print out full_sorted
print(full_sorted)

```

# Methods

List methosd

```python
in() = fam.index("mom") # Call method index() on fam
out() = 4
```

```python
in() = fam.count(1.73) # Count how many people have this height
out() = 1
```

## Str methods

```python
sister = "liz"
sister.capitalize()
"Liz"
```


```python
sister.replace("z","sa")
'lisa'
```

Methods behave differently depending on the data type, for example using `.count` if its a list itll count the elements if its a string you get the index of the letters of a string  

practice

```python
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

```


Counting stuff

```python
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
```


Creating a list, appending stuff, reversing stuff
```python
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas = (areas.reverse())

# Print out areas
print(areas)
```


# Packages

```python
get-pip.y
pip install something
```

```python
import numpy as np

#if you only one 1 function from a package
from numpy import array
```


Practicing with math

```python
# Import the math package
import math <-----

# Definition of radius
r = 0.43

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

more math ig

```python
# Import radians function of math package
from math import radians


# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist. use the function radians
dist = r * radians(12)

# Print out dist
print(dist)
```


NumPy I guess is pretty important

```python
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
```

NumPy can only contain 1 certain type. NumPy array is a new data type of its own with its own methods a perfect example would be that when using `+` NumPy takes it as if you are quite literally adding the numeric value of both lists

```python
list = [1,2,3]
list + list
[1,2,3,1,2,3]

num = numpy.array(list)
num + num = [2, 4, 6] #it added the 1 with 1, 2 with 2, and 3 with 3
```

it also has a cool feature like the boolean
```python
num > 4 # it will check for values larger than 4 and give a boolean output
[false, true, true]
```

```python
num[num>4] #it will return the values it finds like this
array([4,6])
```

practice time

```python
# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

```python
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m dont forget to multiply n shit
np_height_m = np_height_in * 0.0254 

# Print np_height_m
print(np_height_m)
```



```python
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi, this is how its done
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
```


```python
# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

```


```python
# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

```


# 2D NumPy Arrays

```python
        1      2     3    4     5
array([1.73, 1.68, 1.71, 1.89, 1.79],          0
	 [65.4, 59.2, 63.6, 88.4, 68.7])           1


np_2d = np.array

np_2d = np.array([1.73, 1.68, 1.71, 1.89, 1.79],          
	 [65.4, 59.2, 63.6, 88.4, 68.7])           
	
# shape is not a method, this is an attribute to see what its like
np_2d.shape
(2,5) # two rows and five columns
```


More advanced subsetting can be done

```python
np_2d[0][2]
np_2d[0,2]
```


lets say we want columns at index 1 and 2

```python
        1      2     3    4     5
array([1.73, 1.68, 1.71, 1.89, 1.79],          0
	 [65.4, 59.2, 63.6, 88.4, 68.7])           1

#remember saif when using the subsetting, the first one is for rows the second for columns
np_2d[rows : columns]

# We have specified all rows here using the :, and we have selected both of columns from all the rows
np_2d[: , 1:3]

array([1.68, 1.71], [59.2, 63.2])

#Lets say we want all everything at the second row, and only the second row
np_2d[1, :]
```



Creating a numpy 2d array

```python
# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball) 

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

multidimensional 2d array

```python

#Column 1 has the players height the second has their weight the shape is as follows (1015, 2)

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])

```


```python
# You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D `numpy` array, `updated`. Add `np_baseball` and `updated` and print out the result.

# You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a `numpy` array with three values: `0.0254`, `0.453592` and `1`. Name this array `conversion`.

# Multiply `np_baseball` with `conversion` and print out the result.

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```



# Numpy Basic statistics


to find median

```python
np.median(np_array[:,:]) #To check fof median
np.corrcoef(np_array[:,:]) #To check if theres a correlation
np.std(np_array[:,:]) #To check if for standard deviation
np.sum(np_array[:,:]) #To check if theres a correlation
np.sort(np_array[:,:]) #To check if theres a correlation
```

```python
# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
```


```python
# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column, this is done by using commas
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```


```python
# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights = np.array(heights)
np_positions = np.array(positions)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']  #!= is basically just ! space =

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
```


Do the execrises again i got lost a little near the end 


