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