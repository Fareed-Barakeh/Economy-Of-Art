# scatter plot with the brightness from 0 to 255 and mean_price
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

# reading the dataset with read_csv
parent = pathlib.Path(__file__).parent.parent.resolve()
file_path = parent / "data.txt"
df = pd.read_csv(file_path, sep="\t", low_memory=False)

# We are selecting the columns 'brightness' and 'price'
# The dataset has missing values so we are excluding the rows with missing values
df = df[['brightness', 'price']].dropna()

# grouping the dataset by brightness and calculating the mean price
brightness_mean_price = df.groupby('brightness')['price'].mean().reset_index()

# size of the plot
plt.figure(figsize=(12, 6))

# We are doing a scatter plot here
sns.scatterplot(data=brightness_mean_price, x='brightness', y='price', alpha=0.7)

# log-scaling of the x/y-axis
plt.xscale('log')
plt.yscale('log')

# This is for changing the visible scaling of the x/y-axis so we dont get
# 10^x on the x/y-axis
ax = plt.gca()

# We don't want to use useMathText, just regular Text for the scaling on the x/y-axis
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=False))
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=False))

# We don't want to use scientificNotation, because for small numbers we get
# something like -10^x
ax.xaxis.get_major_formatter().set_scientific(False)
ax.yaxis.get_major_formatter().set_scientific(False)

# We are manually scaling the x-axis with this
x_ticks = [10, 25, 50, 100, 150, 200, 255]
plt.xticks(x_ticks)

# labels for the x/y-axis and also the title of the plot
plt.xlabel('Brightness from 0 to 255')
plt.ylabel('Mean price in $')
plt.title('Brightness and Mean Price of Artworks in a Scatter Plot')

# Just so nothing overlaps on the plot like the title, x/y-labels
plt.tight_layout()
plt.show()
