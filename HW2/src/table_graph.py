import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    """Load data from Excel file"""
    df = pd.read_excel(file_path)
    
    # Print column names for debugging
    print("DataFrame Columns:")
    print(df.columns.tolist())
    
    # Extract year from conference name
    df['Year'] = df.iloc[:, 0].str.extract('(\d{2})').astype(int)
    # Filter data for 2016-2020
    df = df[df['Year'].isin([16, 17, 18, 19, 20])]
    return df

def create_table_visualization(df):
    """Create and save table visualization"""
    # Select columns to display
    display_cols = df.columns.tolist()[:4]  # Select first 4 columns
    formatted_df = df[display_cols].copy()
    
    # Convert acceptance rate to percentage format
    formatted_df.iloc[:, 1] = (formatted_df.iloc[:, 1] * 100).round(1).astype(str) + '%'
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')
    
    # Create table
    table = ax.table(cellText=formatted_df.values,
                    colLabels=display_cols,
                    cellLoc='center',
                    loc='center')
    
    # Adjust table style
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)
    
    plt.title('Conference Acceptance Rates - Table View (2016-2020)', pad=20)
    # Ensure output directory exists
    os.makedirs('./results/figures', exist_ok=True)
    plt.savefig('./results/figures/acceptance_table.png', 
                bbox_inches='tight',
                dpi=300)
    plt.close()

def create_graph_visualization(df):
    """Create and save graph visualization"""
    # Extract conference names (without year)
    df['Conference'] = df.iloc[:, 0].str.extract('([A-Za-z]+)')
    
    # Set graph style
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot lines for each conference
    for conference in df['Conference'].unique():
        conf_data = df[df['Conference'] == conference]
        ax.plot(conf_data['Year'], conf_data.iloc[:, 1] * 100, 
                marker='o', label=conference, linewidth=2, markersize=8)
    
    # Set graph style
    ax.set_title('Conference Acceptance Rates Over Time (2016-2020)', pad=20, size=14)
    ax.set_xlabel('Year (20XX)', size=12)
    ax.set_ylabel('Acceptance Rate (%)', size=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Set x-axis ticks
    ax.set_xticks([16, 17, 18, 19, 20])
    ax.set_xticklabels(['2016', '2017', '2018', '2019', '2020'])
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save graph
    os.makedirs('./results/figures', exist_ok=True)
    plt.savefig('./results/figures/acceptance_graph.png', 
                bbox_inches='tight',
                dpi=300)
    plt.close()

def main():
    # Load data
    df = load_data('./data/data-1.xlsx')
    
    # Create visualizations
    create_table_visualization(df)
    create_graph_visualization(df)
    
    # Print comparison analysis
    print("""
    Visualization Comparison Analysis:
    
    Table Visualization:
    Pros:
    - Precise presentation of exact values
    - Easy to look up specific numbers
    - Good for comparing individual values
    - Shows all three metrics (acceptance rate, accepted papers, total submissions)
    
    Cons:
    - Difficult to see trends over time
    - Takes more space to display
    - Requires more time to process information
    
    Graph Visualization:
    Pros:
    - Clear visualization of trends over time
    - Easy to compare patterns between conferences
    - Intuitive understanding of acceptance rate changes
    - Compact representation of temporal patterns
    
    Cons:
    - Only shows acceptance rate (not paper counts)
    - Can become cluttered with too many conferences
    - Less precise for exact values
    """)

if __name__ == "__main__":
    main()