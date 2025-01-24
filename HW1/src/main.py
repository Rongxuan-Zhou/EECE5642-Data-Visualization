import pandas as pd
import numpy as np
from visualizer import Visualizer
import logging
import os

def setup_logging():
    """Configures logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def ensure_directories():
    """Ensures necessary directories exist."""
    directories = ['../results', '../results/figures']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def preprocess_data(data):
    """Preprocesses the data."""
    # Convert numeric columns
    numeric_cols = [
        'Age', 'Sleep Hours', 'Physical Activity (hrs/week)',
        'Caffeine Intake (mg/day)', 'Alcohol Consumption (drinks/week)',
        'Stress Level (1-10)', 'Heart Rate (bpm during attack)',
        'Breathing Rate (breaths/min)', 'Sweating Level (1-5)',
        'Therapy Sessions (per month)', 'Diet Quality (1-10)',
        'Severity of Anxiety Attack (1-10)'
    ]
    
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    return data

def main():
    try:
        # Initialize settings
        setup_logging()
        ensure_directories()
        logging.info("Starting anxiety analysis project")
        
        # Load data
        data_path = '../data/anxiety_attack_dataset.csv'
        data = pd.read_csv(data_path)
        logging.info(f"Successfully loaded data with shape: {data.shape}")
        
        # Preprocess data
        data = preprocess_data(data)
        logging.info("Data preprocessing completed")
        
        # Create visualizations
        visualizer = Visualizer()
        visualizer.generate_all_visualizations(data)
        
        logging.info("Analysis completed successfully")
        
    except FileNotFoundError:
        logging.error(f"Data file not found at: {data_path}")
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()