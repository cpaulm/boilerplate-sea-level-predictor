import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    start_year_fit1 = df['Year'].min()
    end_year_fit1 = 2050 + 1
    years_fit1 = range(start_year_fit1, end_year_fit1)
    plt.plot(years_fit1, intercept + slope*years_fit1, 'r', label='Best Fit Line 1')

    # Create second line of best fit
    start_year_fit2 = 2000
    end_year_fit2 = 2050 + 1
    years_fit2 = range(start_year_fit2, end_year_fit2)
    df2 = df[df['Year'] >= start_year_fit2]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    plt.plot(years_fit2, intercept2 + slope2*years_fit2, 'g', label='Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()