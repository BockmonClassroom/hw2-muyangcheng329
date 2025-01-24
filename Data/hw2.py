import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset 
df = pd.read_csv('Plants.csv')

# Statistical Analysis
stats = df.groupby('Plant_Name').agg(['mean', 'median', 'std', 'var'])
print("Statistical Analysis:")
print(stats)

# Data Visualization

# Histograms
for col in ['Leaf_Width', 'Leaf_Length']:
    sns.histplot(data=df, x=col, hue='Plant_Name', kde=False, multiple='dodge')
    plt.title(f'{col} Histogram')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.legend(title='Plant Type')
    plt.show()

# Boxplots
for col in ['Leaf_Width', 'Leaf_Length']:
    sns.boxplot(data=df, x='Plant_Name', y=col)
    plt.title(f'{col} Boxplot')
    plt.xlabel('Plant Type')
    plt.ylabel(col)
    plt.show()

# Scatter Plot
sns.scatterplot(data=df, x='Leaf_Width', y='Leaf_Length', hue='Plant_Name')
plt.title('Leaf Width vs. Leaf Length Scatter Plot')
plt.xlabel('Leaf Width')
plt.ylabel('Leaf Length')
plt.legend(title='Plant Type')
plt.show()
