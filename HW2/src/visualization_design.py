import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_improved_airline_visualization():
    # Sample data
    airlines = ['Delta', 'Southwest', 'Alaska', 'Allegiant', 'United', 
                'JetBlue', 'American', 'Spirit', 'Frontier']
    metrics = {
        'On-time Performance': [81.9, 78.5, 76.2, 75.8, 75.1, 74.3, 73.2, 71.5, 70.8],
        'Flight Completion Rate': [99.2, 99.1, 98.9, 98.7, 98.5, 98.2, 98.0, 97.8, 97.5],
        'Punctuality Score': [92.2, 91.5, 90.8, 90.2, 89.5, 88.8, 88.1, 87.5, 86.8],
        'Baggage Handling Score': [95.5, 94.8, 94.2, 93.5, 92.8, 92.1, 91.5, 90.8, 90.1]
    }
    
    # 设置图表风格
    plt.style.use('seaborn')
    
    # 创建图形和子图
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Airline Performance Metrics (2024)', y=0.98, fontsize=16)
    
    # 设置全局样式
    bar_color = '#6B8EB8'
    background_color = '#F0F1F4'
    
    # 绘制每个指标
    for (metric, values), ax in zip(metrics.items(), axes.flat):
        # 设置背景色
        ax.set_facecolor(background_color)
        
        # 创建水平条形图
        y_pos = range(len(airlines))
        bars = ax.barh(y_pos, values, alpha=1, color=bar_color)
        
        # 自定义外观
        ax.set_yticks(y_pos)
        ax.set_yticklabels(airlines)
        ax.set_title(metric, pad=10)
        
        # 设置坐标轴
        if metric in ['On-time Performance', 'Punctuality Score']:
            ax.set_xlim(0, 85)
        else:
            ax.set_xlim(0, 100)
            
        # 移除边框
        for spine in ax.spines.values():
            spine.set_visible(False)
            
        # 设置网格线
        ax.grid(True, axis='x', linestyle='-', alpha=0.1)
        
        # 添加数值标签
        for bar in bars:
            width = bar.get_width()
            # 使用偏移量（0.5）来替代 padding
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                   f'{width:.1f}%', 
                   ha='left', va='center',
                   fontsize=8)
    
    # 调整布局
    plt.tight_layout()
    
    return fig

def save_visualization():
    # 创建保存路径
    save_dir = os.path.join('..', 'results', 'figures')
    
    # 确保目录存在
    os.makedirs(save_dir, exist_ok=True)
    
    # 创建完整的保存路径
    save_path = os.path.join(save_dir, 'improved_airline_visualization.png')
    
    # 创建和保存图表
    fig = create_improved_airline_visualization()
    fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    
    print(f"Visualization saved to: {save_path}")

if __name__ == "__main__":
    save_visualization()