import pandas as pd
import numpy as np


#cleaning and preprocessing
def handle_missing_values(df, strategy='mean'):
  """Handles missing values in a DataFrame.

  Args:
    df: Pandas DataFrame.
    strategy: Fill strategy ('mean', 'median', 'mode', 'ffill', 'bfill').

  Returns:
    Pandas DataFrame with filled missing values.
  """
  if strategy == 'mean':
    return df.fillna(df.mean())
  elif strategy == 'median':
    return df.fillna(df.median())
  # ... other strategies

def remove_outliers(df, column, method='z-score', threshold=3):
  """Removes outliers from a DataFrame based on a specified method.

  Args:
    df: Pandas DataFrame.
    column: The column to check for outliers.
    method: Outlier detection method ('z-score', 'iqr').
    threshold: Threshold for outlier detection.

  Returns:
    Pandas DataFrame without outliers.
  """
  if method == 'z-score':
    z_scores = (df[column] - df[column].mean()) / df[column].std()
    df = df[abs(z_scores) < threshold]
  # ... other methods
  return df


def detect_outliers_iqr(df, column, factor=1.5):
  """Detects outliers using the Interquartile Range (IQR) method.

  Args:
    df: Pandas DataFrame.
    column: The column to check for outliers.
    factor: The IQR multiplier for outlier detection.

  Returns:
    A list of indices of outliers.
  """
  Q1 = df[column].quantile(0.25)
  Q3 = df[column].quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = Q1 - factor * IQR
  upper_bound = Q3 + factor * IQR
  return df[(df[column] < lower_bound) | (df[column] > upper_bound)].index


def handle_categorical_missing_values(df, column, strategy='most_frequent'):
  """Handles missing values in categorical columns.

  Args:
    df: Pandas DataFrame.
    column: The categorical column.
    strategy: Handling strategy ('most_frequent', 'constant').

  Returns:
    Pandas DataFrame with filled missing values.
  """
  if strategy == 'most_frequent':
    most_frequent = df[column].mode()[0]
    df[column].fillna(most_frequent, inplace=True)
  # ... other strategies
  return df

def handle_categorical_missing_values(df, column, strategy='most_frequent'):
  """Handles missing values in categorical columns.

  Args:
    df: Pandas DataFrame.
    column: The categorical column.
    strategy: Handling strategy ('most_frequent', 'constant').

  Returns:
    Pandas DataFrame with filled missing values.
  """
  if strategy == 'most_frequent':
    most_frequent = df[column].mode()[0]
    df[column].fillna(most_frequent, inplace=True)
  elif strategy == 'constant':
    df[column].fillna('missing', inplace=True)  # Replace with desired constant
  return df

def encode_categorical_features(df, columns, encoding_type='one-hot'):
  """Encodes categorical features.

  Args:
    df: Pandas DataFrame.
    columns: List of categorical columns.
    encoding_type: Encoding type ('one-hot', 'label_encoding').

  Returns:
    Pandas DataFrame with encoded features.
  """
  if encoding_type == 'one-hot':
    return pd.get_dummies(df, columns=columns)
  elif encoding_type == 'label_encoding':
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for col in columns:
      df[col] = le.fit_transform(df[col])
    return df


# loading data
def load_excel(file_path, sheet_name=None):
  """Loads data from an Excel file into a Pandas DataFrame.

  Args:
    file_path: Path to the Excel file.
    sheet_name: Name of the sheet to load. Defaults to None, which loads the first sheet.

  Returns:
    Pandas DataFrame containing the loaded data.
  """
  return pd.read_excel(file_path, sheet_name=sheet_name)

def export_to_excel(data, file_path, sheet_name='Sheet1', index=False):
  """Exports a Pandas DataFrame to an Excel file.

  Args:
    data: Pandas DataFrame to export.
    file_path: Path to the output Excel file.
    sheet_name: Name of the sheet to create. Defaults to 'Sheet1'.
    index: Whether to include the DataFrame index as a column. Defaults to False.
  """
  data.to_excel(file_path, sheet_name=sheet_name, index=index)


# data transformations
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalize_data(df, columns, method='min-max'):
  """Normalizes numerical columns in a DataFrame.

  Args:
    df: Pandas DataFrame.
    columns: List of columns to normalize.
    method: Normalization method ('min-max', 'standard').

  Returns:
    Pandas DataFrame with normalized columns.
  """
  if method == 'min-max':
    scaler = MinMaxScaler()
  elif method == 'standard':
    scaler = StandardScaler()
  df[columns] = scaler.fit_transform(df[columns])
  return df

def one_hot_encode(df, columns):
  """One-hot encodes categorical columns in a DataFrame.

  Args:
    df: Pandas DataFrame.
    columns: List of columns to encode.

  Returns:
    Pandas DataFrame with one-hot encoded columns.
  """
  return pd.get_dummies(df, columns=columns)

from sklearn.preprocessing import PolynomialFeatures

def create_interaction_terms(df, columns):
  """Creates interaction terms between specified columns.

  Args:
    df: Pandas DataFrame.
    columns: List of columns to create interactions for.

  Returns:
    Pandas DataFrame with interaction terms.
  """
  poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
  df_poly = pd.DataFrame(poly.fit_transform(df[columns]), columns=poly.get_feature_names(columns))
  return pd.concat([df, df_poly], axis=1)

def log_transform(df, columns):
  """Applies log transformation to specified columns.

  Args:
    df: Pandas DataFrame.
    columns: List of columns to log transform.

  Returns:
    Pandas DataFrame with log-transformed columns.
  """
  df[columns] = np.log(df[columns])
  return df

from sklearn.preprocessing import PolynomialFeatures

def create_polynomial_features(df, columns, degree=2):
  """Creates polynomial features.

  Args:
    df: Pandas DataFrame.
    columns: List of columns to create polynomial features for.
    degree: Degree of polynomial features.

  Returns:
    Pandas DataFrame with polynomial features.
  """
  poly = PolynomialFeatures(degree=degree, include_bias=False)
  df_poly = pd.DataFrame(poly.fit_transform(df[columns]), columns=poly.get_feature_names(columns))
  return pd.concat([df, df_poly], axis=1)

def binning(df, column, bins):
  """Bins a numerical column into categorical bins.

  Args:
    df: Pandas DataFrame.
    column: The column to bin.
    bins: List of bin edges.

  Returns:
    Pandas DataFrame with the binned column.
  """
  df[column + '_binned'] = pd.cut(df[column], bins=bins)
  return df

# data analysis
from scipy.stats import chi2_contingency

def chi_square_test(df, column1, column2):
  """Performs a chi-square test of independence.

  Args:
    df: Pandas DataFrame.
    column1: First categorical column.
    column2: Second categorical column.

  Returns:
    Chi-square statistic, p-value, degrees of freedom, and expected frequencies.
  """
  contingency_table = pd.crosstab(df[column1], df[column2])
  return chi2_contingency(contingency_table)

from scipy.stats import chi2_contingency
from sklearn.feature_selection import SelectKBest, chi2

def chi_square_test(df, target_column, features):
  """Performs chi-square test for feature selection.

  Args:
    df: Pandas DataFrame.
    target_column: Target variable.
    features: List of features to test.

  Returns:
    A list of selected features.
  """
  X = df[features]
  y = df[target_column]
  selector = SelectKBest(chi2, k='all')
  selector.fit(X, y)
  scores = selector.scores_
  pvalues = selector.pvalues_
  return list(zip(features, scores, pvalues))

import matplotlib.pyplot as plt

def calculate_summary_statistics(df):
  """Calculates summary statistics for numerical columns in a DataFrame.

  Args:
    df: Pandas DataFrame.

  Returns:
    Summary statistics as a DataFrame.
  """
  return df.describe()

def plot_histogram(df, column):
  """Plots a histogram for a given column.

  Args:
    df: Pandas DataFrame.
    column: The column to plot.
  """
  df[column].hist()
  plt.show()


# Process a folder of JSON files.
# Extract file URLs from each JSON file.
# Potentially handle different JSON structures.

import json
import os

def extract_file_urls(folder_path):
  """Extracts file URLs from JSON files in a specified folder.

  Args:
    folder_path: Path to the folder containing JSON files.

  Returns:
    A list of extracted file URLs.
  """

  file_urls = []
  for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
      file_path = os.path.join(folder_path, filename)
      with open(file_path, 'r') as f:
        data = json.load(f)
        # Adjust the following line based on JSON structure
        file_urls.extend([item['file_url'] for item in data if 'file_url' in item])

  return file_urls

# Example usage:
folder_path = 'path/to/json/files'
urls = extract_file_urls(folder_path)
print(urls)

