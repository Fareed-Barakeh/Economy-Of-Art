# Jitter Plot of the Top Ten Nationalities with the Highest Median Price (smaller Points for better visibility)
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker

# reading the dataset with read_csv
parent = pathlib.Path(__file__).parent.parent.resolve()
file_path = parent / "data.txt"
df = pd.read_csv(file_path, sep="\t", low_memory=False)

# We are selecting the colums 'country' and 'price'
# The dataset has missing values so we are excluding the rows with missing values
df = df[['country', 'price']].dropna()


# With country_counts we are count how man entries we have for certain countries
# country_counts is important because we are taking the median price and low
# country_counts are manipulating are results
# Our threshold is at least 10 entries for a country
country_counts = df['country'].value_counts()
valid_countries = country_counts[country_counts >= 10].index
df = df[df['country'].isin(valid_countries)]

# grouping the dataset by country and calculating the median price
median_price_per_country = df.groupby('country')['price'].median().reset_index()

# We are taking the top 10 countries with the highest median price
top_10_countries_sorted_by_median = median_price_per_country.sort_values(by='price', ascending=False).head(10)

# We need to convert our results to a python list so we can use it in our
# stripplot and also have the exact order if we dont transform it like that
# we dont get the exact same order in our jitter-plot
sorted_countries = top_10_countries_sorted_by_median['country'].tolist()

# Transforming it to a dataframe again and filter it so it only includes the top 10 countries
df_top_10_sorted_by_median = df[df['country'].isin(sorted_countries)]

# size of the plot
plt.figure(figsize=(12, 8))

# We are doing a jitter plot here
sns.stripplot(
    data=df_top_10_sorted_by_median,
    x='country',
    y='price',
    jitter=0.3, # shifting the points horizontally so the points dont overlap to much
    size=2,  # size of the points
    alpha=0.6,  # transparency of the points
    color='blue',
    order=sorted_countries
)

# log-scaling of the y-axis
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))


# labels for the x/y-axis and also the title of the plot
plt.title('Top Ten Nationalities with the Highest Median Price', fontsize=14)
plt.xlabel('Nationalities', fontsize=12)
plt.ylabel('Price in $', fontsize=12)

# rotating the names on the x-axis for better readability
plt.xticks(rotation=45)

# Just so nothing overlaps on the plot like the title, x/y-labels
plt.tight_layout()
plt.show()
