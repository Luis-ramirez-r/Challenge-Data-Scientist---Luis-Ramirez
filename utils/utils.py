import pandas as pd 
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def make_bar_plot(df, target, title, key_map={},color='#3B3B3B'):
    """
    This function creates a bar plot showing the percentage of values in a target column of a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame to plot.
        target (str): The name of the column to use as the target of the plot.
        title (str): The title of the plot.
        key_map (dict, optional): A mapping of values in the target column to their desired order in the plot. Default is an empty dictionary.
    
    Returns:
        None
    """
    
    # Calculate the percentage of values in the target column
    df_pct = (df
    .groupby(target)
    .size()
    .reset_index(name='counts')
    .assign(percentage = lambda x: x['counts'] / x['counts'].sum() * 100)
    .sort_values(by=target, key=lambda x: x.map(key_map))
    )
    
    # Create the bar plot
    sns.barplot(x=df_pct[target], y=df_pct['percentage'],
                palette=[color])

    # Add a title and x-label to the plot
    plt.title(title)
    plt.xlabel(target)
    
    # Add a horizontal reference line and label
    reference = df_pct['percentage'].mean()
    plt.axhline(y=reference ,color='r', linestyle='dashed', linewidth=1)
    #plt.text(x=3, y=reference+0.1, s='Average', size=10)
    # Show the plot
    plt.show()




def get_high_season(df):
    """
    Returns a boolean Series indicating which rows of a pandas DataFrame represent dates in the high season, based on the following criteria:
    - MES is 12 and DIA is greater than or equal to 15
    - MES is 1
    - MES is 2
    - MES is 3 and DIA is less than 3
    - MES is 7 and DIA is between 15 and 31 (inclusive)
    - MES is 9 and DIA is between 11 and 30 (inclusive)
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to be filtered.
    
    Returns:
    pandas.Series: A boolean Series indicating which rows of the DataFrame represent dates in the high season.
    """
    high_season = (  ((df['MES'] == 12) & (df['DIA'] >= 15)) | 
                      (df['MES'] == 1) | (df['MES'] == 2) | ((df['MES'] == 3) & (df['DIA'] < 3)  ) |
                     ((df['MES'] == 7) & ((df['DIA'] >= 15) & (df['DIA'] <= 31))) |
                     ((df['MES'] == 9) & ((df['DIA'] >= 11) & (df['DIA'] <= 30))))
    return high_season.astype(int)



