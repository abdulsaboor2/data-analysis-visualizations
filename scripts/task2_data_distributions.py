import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the CSV file
file_path = '../data/data3.csv'
data = pd.read_csv(file_path)

# Parse the Date column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Create a box plot for 'Close' and 'Volume' separately
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 8))
sns.boxplot(y=data['Close'], ax=axes[0], palette="Set3")
sns.boxplot(y=data['Volume'], ax=axes[1], palette="Set3")

# Customize the plots
axes[0].set_title('Distribution of Closing Prices', fontsize=16)
axes[0].set_ylabel('Closing Price', fontsize=14)
axes[0].set_xlabel('XYZ Corp.', fontsize=14)

axes[1].set_title('Distribution of Trade Volumes', fontsize=16)
axes[1].set_ylabel('Trade Volume', fontsize=14)
axes[1].set_xlabel('XYZ Corp.', fontsize=14)

for ax in axes:
    ax.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()

# Save the plot
plt.savefig('../plots/data_distributions_plot.png')
plt.close()

logging.info('Data distribution visualizations successfully generated.')
