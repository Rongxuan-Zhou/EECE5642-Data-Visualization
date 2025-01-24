import pandas as pd
import numpy as np
from visualizer import Visualizer
import logging
import os

def setup_logging():
    """设置日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def ensure_directories():
    """确保必要的目录存在"""
    directories = ['../results', '../results/figures']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def preprocess_data(data):
    """数据预处理"""
    # 转换数值型列
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
        # 初始化设置
        setup_logging()
        ensure_directories()
        logging.info("Starting anxiety analysis project")
        
        # 加载数据
        data_path = '../data/anxiety_attack_dataset.csv'
        data = pd.read_csv(data_path)
        logging.info(f"Successfully loaded data with shape: {data.shape}")
        
        # 数据预处理
        data = preprocess_data(data)
        logging.info("Data preprocessing completed")
        
        # 创建可视化
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