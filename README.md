# Data Analysis Visualizations

This repository contains Python scripts for advanced data analysis and visualization tasks. The project demonstrates:
1. **Stock Data Analysis**: Visualization of stock closing prices over time.
2. **Data Distribution Visualization**: Box plots for stock closing prices and trade volumes.
3. **Geographic Data Visualization**: Choropleth map of global population distribution.

#### Folder Structure
- `scripts/`: Contains Python scripts for each task.
  - `task1_stock_analysis.py`: Script for stock data analysis.
  - `task2_data_distributions.py`: Script for data distribution visualizations.
  - `task3_geographic_visualization.py`: Script for geographic data visualization.
- `data/`: Contains example datasets.
  - `data3.csv`: Example CSV file for stock data.
- `shapefiles/`: Contains shapefiles for geographic data.
  - `ne_10m_admin_0_countries.shp`: Shapefile for global country boundaries.
- `plots/`: Folder where generated plots are saved.
  - `closing_prices_plot.png`
  - `data_distributions_plot.png`
  - `geographic_data_plot.png`
- `README.md`: Provides an overview of the project and instructions for running the code.

#### Instructions for Running the Code
1. **Install Dependencies**:
   ```bash
   pip install pandas matplotlib seaborn geopandas
   ```
2. **Run Scripts**:
   - `task1_stock_analysis.py`: Analyzes stock data and generates a line plot.
   - `task2_data_distributions.py`: Creates box plots for data distributions.
   - `task3_geographic_visualization.py`: Generates a choropleth map for geographic data.

3. **View Results**:
   - Plots will be saved in the `plots/` folder.

## Video

https://github.com/user-attachments/assets/22961eac-e3b4-41f1-8f63-7198b003a08c

## License
This project is licensed under the MIT License.
