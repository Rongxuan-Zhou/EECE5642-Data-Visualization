import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, data_path='../data/anxiety_attack_dataset.csv'):
        """Initializes the DataProcessor with the given data path."""
        self.data_path = data_path
        self.data = None
        self.X = None
        self.y = None
        self.feature_names = None
        
    def load_data(self):
        """Loads the data"""
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"Successfully loaded data with shape: {self.data.shape}")
            return self.data
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def get_data_info(self):
        """Retrieves basic information about the data"""
        info = {
            'shape': self.data.shape,
            'columns': self.data.columns.tolist(),
            'missing_values': self.data.isnull().sum(),
            'data_types': self.data.dtypes,
            'summary_stats': self.data.describe()
        }
        return info
    
    def preprocess_data(self):
        """Preprocesses the data"""
        if self.data is None:
            print("Please load data first")
            return None
        
        # 1. Check and handle missing values
        missing_values = self.data.isnull().sum()
        if missing_values.any():
            print("Handling missing values...")
            self.data = self.data.dropna()
        
        # 2. Separate features and target variable
        self.y = self.data['Anxiety_Level']
        self.X = self.data.drop('Anxiety_Level', axis=1)
        self.feature_names = self.X.columns
        
        # 3. Standardize features
        scaler = StandardScaler()
        self.X = pd.DataFrame(
            scaler.fit_transform(self.X),
            columns=self.feature_names
        )
        
        return self.X, self.y
    
    def split_data(self, test_size=0.2, random_state=42):
        """Splits the data into training and testing sets"""
        if self.X is None or self.y is None:
            print("Please preprocess data first")
            return None
        
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y,
            test_size=test_size,
            random_state=random_state,
            stratify=self.y
        )
        
        return X_train, X_test, y_train, y_test