import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

class Visualizer:
    def __init__(self, save_path='../results/figures/'):
        """
        初始化可视化器
        Args:
            save_path: 图表保存路径
        """
        self.save_path = save_path
        self.setup_visualization_settings()
        os.makedirs(save_path, exist_ok=True)

    def setup_visualization_settings(self):
        """设置可视化参数"""
        plt.style.use('seaborn')
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = [10, 6]
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 300

    def save_plot(self, name, fig=None, is_plotly=False):
        """
        保存图表的通用方法
        """
        try:
            if is_plotly:
                fig.write_html(f'{self.save_path}{name}.html')
            else:
                plt.savefig(f'{self.save_path}{name}.png', bbox_inches='tight')
                plt.close()
        except Exception as e:
            print(f"Error saving {name}: {str(e)}")

    def plot_anxiety_severity_distribution(self, data):
        """绘制焦虑严重程度分布图"""
        plt.figure(figsize=(12, 6))
        sns.histplot(data=data, x='Severity of Anxiety Attack (1-10)', 
                    bins=10, kde=True)
        plt.title('Distribution of Anxiety Attack Severity', pad=20)
        plt.xlabel('Severity Level')
        plt.ylabel('Count')
        self.save_plot('anxiety_severity_distribution')

    def plot_correlation_matrix(self, data):
        """绘制相关性矩阵"""
        numerical_cols = [
            'Age', 'Sleep Hours', 'Physical Activity (hrs/week)',
            'Caffeine Intake (mg/day)', 'Alcohol Consumption (drinks/week)',
            'Stress Level (1-10)', 'Heart Rate (bpm during attack)',
            'Breathing Rate (breaths/min)', 'Sweating Level (1-5)',
            'Therapy Sessions (per month)', 'Diet Quality (1-10)',
            'Severity of Anxiety Attack (1-10)'
        ]
        
        correlation_matrix = data[numerical_cols].corr()
        
        plt.figure(figsize=(14, 12))
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   center=0,
                   fmt='.2f',
                   square=True)
        plt.title('Correlation Matrix of Anxiety Factors', pad=20)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        self.save_plot('correlation_matrix')

    def plot_physical_factors(self, data):
        """绘制身体症状与焦虑程度的关系图"""
        fig = plt.figure(figsize=(16, 12))
        
        # Heart Rate
        plt.subplot(2, 2, 1)
        sns.scatterplot(data=data, 
                       x='Heart Rate (bpm during attack)', 
                       y='Severity of Anxiety Attack (1-10)',
                       alpha=0.6)
        plt.title('Heart Rate vs Anxiety Severity')
        
        # Breathing Rate
        plt.subplot(2, 2, 2)
        sns.scatterplot(data=data, 
                       x='Breathing Rate (breaths/min)', 
                       y='Severity of Anxiety Attack (1-10)',
                       alpha=0.6)
        plt.title('Breathing Rate vs Anxiety Severity')
        
        # Sweating Level
        plt.subplot(2, 2, 3)
        sns.boxplot(data=data, 
                   x='Sweating Level (1-5)', 
                   y='Severity of Anxiety Attack (1-10)')
        plt.title('Sweating Level vs Anxiety Severity')
        
        # Stress Level
        plt.subplot(2, 2, 4)
        sns.scatterplot(data=data, 
                       x='Stress Level (1-10)', 
                       y='Severity of Anxiety Attack (1-10)',
                       alpha=0.6)
        plt.title('Stress Level vs Anxiety Severity')
        
        plt.tight_layout()
        self.save_plot('physical_factors')

    def plot_lifestyle_factors(self, data):
        """创建生活方式因素的交互式图表"""
        try:
            fig = px.scatter_matrix(
                data,
                dimensions=[
                    'Sleep Hours', 
                    'Physical Activity (hrs/week)',
                    'Caffeine Intake (mg/day)',
                    'Diet Quality (1-10)'
                ],
                color='Severity of Anxiety Attack (1-10)',
                title='Lifestyle Factors Relationship Matrix'
            )
            
            fig.update_layout(
                title_x=0.5,
                height=800,
                width=800,
                showlegend=True
            )
            
            self.save_plot('lifestyle_factors', fig, True)
            
        except Exception as e:
            print(f"Error in lifestyle factors plot: {str(e)}")

    def plot_demographic_analysis(self, data):
        """绘制人口统计学分析图"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
        
        # Age groups
        data['Age_Group'] = pd.cut(
            data['Age'], 
            bins=[0, 25, 35, 45, 55, 100],
            labels=['18-25', '26-35', '36-45', '46-55', '55+']
        )
        
        sns.boxplot(data=data, 
                   x='Age_Group', 
                   y='Severity of Anxiety Attack (1-10)', 
                   ax=ax1)
        ax1.set_title('Anxiety Severity by Age Group', pad=20)
        ax1.set_xlabel('Age Group')
        ax1.set_ylabel('Anxiety Severity')
        
        sns.boxplot(data=data, 
                   x='Gender', 
                   y='Severity of Anxiety Attack (1-10)', 
                   ax=ax2)
        ax2.set_title('Anxiety Severity by Gender', pad=20)
        ax2.set_xlabel('Gender')
        ax2.set_ylabel('Anxiety Severity')
        
        plt.tight_layout()
        self.save_plot('demographic_analysis')

    def plot_dimensionality_reduction(self, data):
        """绘制降维分析图 (PCA, t-SNE, UMAP)"""
        # 准备数据
        numerical_cols = [
            'Age', 'Sleep Hours', 'Physical Activity (hrs/week)',
            'Caffeine Intake (mg/day)', 'Alcohol Consumption (drinks/week)',
            'Stress Level (1-10)', 'Heart Rate (bpm during attack)',
            'Breathing Rate (breaths/min)', 'Sweating Level (1-5)',
            'Therapy Sessions (per month)', 'Diet Quality (1-10)'
        ]
        
        X = data[numerical_cols].values
        y = data['Severity of Anxiety Attack (1-10)'].values
        
        # 数据标准化
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # PCA
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        
        # t-SNE
        tsne = TSNE(n_components=2, random_state=42)
        X_tsne = tsne.fit_transform(X_scaled)
        
        # UMAP
        reducer = umap.UMAP(random_state=42)
        X_umap = reducer.fit_transform(X_scaled)
        
        # 创建图表
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 8))
        
        # PCA plot
        scatter1 = ax1.scatter(X_pca[:, 0], X_pca[:, 1], c=y, 
                             cmap='viridis', alpha=0.6)
        ax1.set_title('PCA Analysis')
        ax1.set_xlabel('First Principal Component')
        ax1.set_ylabel('Second Principal Component')
        plt.colorbar(scatter1, ax=ax1, label='Anxiety Severity')
        
        # t-SNE plot
        scatter2 = ax2.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, 
                             cmap='viridis', alpha=0.6)
        ax2.set_title('t-SNE Analysis')
        ax2.set_xlabel('t-SNE Component 1')
        ax2.set_ylabel('t-SNE Component 2')
        plt.colorbar(scatter2, ax=ax2, label='Anxiety Severity')
        
        # UMAP plot
        scatter3 = ax3.scatter(X_umap[:, 0], X_umap[:, 1], c=y, 
                             cmap='viridis', alpha=0.6)
        ax3.set_title('UMAP Analysis')
        ax3.set_xlabel('UMAP Component 1')
        ax3.set_ylabel('UMAP Component 2')
        plt.colorbar(scatter3, ax=ax3, label='Anxiety Severity')
        
        plt.tight_layout()
        self.save_plot('dimensionality_reduction')

    def generate_all_visualizations(self, data):
        """生成所有可视化图表"""
        print("\nStarting visualization generation...")
        
        try:
            self.plot_anxiety_severity_distribution(data)
            print("1. Anxiety severity distribution plot created")
            
            self.plot_correlation_matrix(data)
            print("2. Correlation matrix created")
            
            self.plot_physical_factors(data)
            print("3. Physical factors analysis created")
            
            self.plot_lifestyle_factors(data)
            print("4. Lifestyle factors analysis created")
            
            self.plot_demographic_analysis(data)
            print("5. Demographic analysis created")
            
            self.plot_dimensionality_reduction(data)
            print("6. Dimensionality reduction analysis created")
            
            print("\nAll visualizations completed successfully!")
            
        except Exception as e:
            print(f"\nError during visualization generation: {str(e)}")