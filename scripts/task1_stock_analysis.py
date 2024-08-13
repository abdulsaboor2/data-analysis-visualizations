import pandas as pd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the CSV file
file_path = '../data/data3.csv'
data = pd.read_csv(file_path)

# Parse the Date column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Create a line plot of the closing prices over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], marker='o', linestyle='-')

# Enhance the plot with title and labels
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Prices of XYZ Corp. Over Time')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate the x-axis labels so it looks better
plt.tight_layout()  # Adjust layout to prevent overlap of labels

# Save the plot
plt.savefig('../plots/closing_prices_plot.png')
plt.close()

logging.info('Stock data analysis plot successfully generated.')
