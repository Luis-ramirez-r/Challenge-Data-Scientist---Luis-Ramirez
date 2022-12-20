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

def train_base_model(model, X_train, y_train, X_val, y_val, features):
    """    
    Parameters:
    model: a scikit-learn model
    X_train: a Pandas dataframe with the training features
    y_train: a Pandas series with the training target
    X_val: a Pandas dataframe with the validation features
    y_val: a Pandas series with the validation target
    features: a list of strings with the names of the features to be used in the model
    
    Returns:
    None
    """
    X_train = X_train[features]
    X_val = X_val[features]

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions for the training data
    y_pred = model.predict(X_train)

    # Evaluate the model on the validation data
    y_pred_val = model.predict(X_val)

    # Print the classification report
    print('Train data report')
    print(classification_report(y_train, y_pred))

    print('Test data report')
    print(classification_report(y_val, y_pred_val))

    # Plot the confusion matrix
    cm = confusion_matrix(y_val, y_pred_val)
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title('Confusion matrix')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    return model


def plot_feature_importance(model, X,  n_features=None):
    # Get the feature importance
    importance = model.coef_[0]
    # Sort the features by their importance in descending order
    sorted_idx = np.argsort(importance)[::-1]
    # Select the top N features
    if n_features:
        top_N_idx = sorted_idx[:n_features]
        importance = importance[top_N_idx]
        X = X[X.columns[top_N_idx]]
    # Summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))
    # Plot feature importance
    plt.bar([x for x in range(len(importance))], importance)
    # Add the names of the features
    plt.xticks([x for x in range(len(importance))], X.columns, rotation=90)
    # Add grid to the plot
    plt.grid()
    plt.show()



