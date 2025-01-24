from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import numpy as np
import pandas as pd

class ModelTrainer:
    def __init__(self):
        """Initializes the Model Trainer."""
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
        self.feature_importance = None
    
    def train(self, X_train, y_train):
        """Trains the model."""
        print("Training model...")
        self.model.fit(X_train, y_train)
        self.feature_importance = pd.Series(
            self.model.feature_importances_,
            index=X_train.columns
        )
        print("Model training completed")
    
    def evaluate(self, X_test, y_test):
        """Evaluates the model."""
        print("Evaluating model...")
        y_pred = self.model.predict(X_test)
        
        # Generate evaluation reports
        report = classification_report(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        # Calculate feature importance
        feature_imp = pd.DataFrame({
            'feature': X_test.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return {
            'classification_report': report,
            'confusion_matrix': conf_matrix,
            'feature_importance': feature_imp
        }
    
    def save_model(self, path='../results/files/model.joblib'):
        """Saves the model."""
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")