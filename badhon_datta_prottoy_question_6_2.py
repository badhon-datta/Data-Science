# -*- coding: utf-8 -*-
"""BADHON DATTA.PROTTOY - Question 6.2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19as2Gd8qhDMIxY_ylasGrUByvIZmA3kr

# 6.2 Visualization using Matplotlib - UK Drivers Death
The dataset containing information about UK driver deaths over time "UKDriversDeaths.csv." is used for this excercise:

1. Visualise the trend in the number of driver deaths as a function of time.

Link for Dataset
https://drive.google.com/file/d/1R6LRO_YIM910H6OL7vqAsQFgWUu9d0KU/view?usp=drive_link
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/MyDrive/m123/UKDriverDeaths.csv')
print(df.head())

plt.figure(figsize=(10,6))
plt.plot(df['time'], df['value'], color='red', marker='o', linestyle='-', linewidth=2, markersize=4)
plt.title('Trend of UK Driver Deaths Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Driver Deaths')
plt.grid(True)
plt.show()

"""As here we are trying to find the relation between death number & year. Mostly in this kind of relations we use line graph."""