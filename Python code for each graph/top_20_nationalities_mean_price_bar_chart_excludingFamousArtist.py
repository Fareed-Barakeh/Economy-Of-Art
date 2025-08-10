# bar chart with the Mean Price and the Top 20 Nationalities
import pathlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the dataset with read_csv
parent = pathlib.Path(__file__).parent.parent.resolve()
file_path = parent / "data.txt"
df = pd.read_csv(file_path, sep="\t", low_memory=False)

# List of artists to exclude
artists_to_exclude = [
    "Andy Warhol", "Mark Rothko", "Pablo Picasso", "Vincent van Gogh",
    "Gustav Klimt", "Paul Cezanne", "Francis Bacon", "Edvard Munch"
]

# Ensure 'price' is numeric (float) and 'country' is string
df_clean = df[
    ~df['artist'].isin(artists_to_exclude) &  # Exclude specific artists
    df['price'].apply(lambda x: isinstance(x, (int, float))) &  # Filter numeric prices
    df['country'].apply(lambda x: isinstance(x, str))  # Filter string countries
]

# Calculate the mean price by country
mean_price_by_country = df_clean.groupby('country')['price'].mean().reset_index()

# Count the number of entries per country and get the top 20 countries
top_20_countries = df_clean['country'].value_counts().head(20).index

# Filter the mean price data to include only the top 20 countries
mean_price_top_20 = mean_price_by_country[mean_price_by_country['country'].isin(top_20_countries)]

# Sort by mean price in descending order
mean_price_top_20_sorted = mean_price_top_20.sort_values(by='price', ascending=False)

# Create the barplot
plt.figure(figsize=(14, 6))
sns.barplot(x='country', y='price', data=mean_price_top_20_sorted)

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Set the y-axis ticks to display values like 10, 100, 1000, 10000, etc.
plt.yticks([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000], 
           ['10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000'])

# Set labels and title
plt.title('Mean Price of Artwork by Top 20 Countries')
plt.xlabel('Country')
plt.ylabel('Mean Price in $')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to make sure labels don't get cut off
plt.tight_layout()

# Display the plot
plt.show()