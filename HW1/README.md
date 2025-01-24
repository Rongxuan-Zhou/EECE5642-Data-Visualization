# Homework 1: Data Visualization - EECE 5642

## Overview
This repository contains the work for Homework 1 of the EECE 5642 Data Visualization course. The assignment involves analyzing and visualizing a quantitative dataset, critiquing a visualization, performing 2D convolution, and providing feedback on the course.

## Dataset
The dataset used for this analysis is the **Anxiety Attack Factors, Symptoms, and Severity Dataset**, which contains over 12,000 records detailing various factors related to anxiety attacks. The dataset includes features such as demographics, lifestyle habits, stress levels, and physiological responses.

- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/ashaychoudhary/anxiety-attack-factors-symptoms-and-severity/data)
- **Repository**: [GitHub Repo](https://github.com/Rongxuan-Zhou/EECE5642-Data-Visualization.git)

## Repository Structure
```
.
├── data
│   ├── anxiety_attack_dataset.csv
│   └── anxiety-attack-factors-symptoms-and-severity.zip
├── docs
│   ├── 2. visualization_critique.ipynb
│   ├── 3. 2D_Convolution.ipynb
│   ├── 4. comments_and_suggestions_on_the_course.ipynb
│   └── Analysis on Anxiety Attack Factors, Symptoms, and Severity Dataset.pdf
├── README.md
├── requirements.txt
├── results
│   ├── figures
│   │   ├── anxiety_severity_distribution.png
│   │   ├── correlation_matrix.png
│   │   ├── demographic_analysis.png
│   │   ├── dimensionality_reduction.png
│   │   ├── lifestyle_factors.html
│   │   └── physical_factors.png
│   └── files
└── src
    ├── data_processor.py
    ├── __init__.py
    ├── main.py
    ├── model_trainer.py
    ├── __pycache__
    │   ├── data_processor.cpython-39.pyc
    │   ├── model_trainer.cpython-39.pyc
    │   └── visualizer.cpython-39.pyc
    └── visualizer.py
```

## Tasks

### 1. Visualization Design
- **Objective**: Analyze and visualize the anxiety attack dataset using at least three different visualization types.
- **Visualizations**:
  - **Distribution of Anxiety Severity**: Histogram and density curve (KDE).
  - **Feature Correlation Heatmap**: Symmetric matrix showing correlations between variables.
  - **Physical Factors Analysis**: Scatter/box plots for heart rate, breathing rate, sweating level, and stress level.
  - **Demographic Analysis**: Distribution of anxiety severity across age groups and genders.
  - **Dimensionality Reduction Analysis**: PCA, t-SNE, and UMAP visualizations.

### 2. Visualization Critique
- **Visualization**: "Zoom into the Human Bloodstream" (NSF 2008 Visualization Challenge).
- **Questions Addressed**:
  - Who is the intended audience?
  - What design principles are utilized?
  - Likes/dislikes and reasons.
  - Imagery and color usage.
  - Suggestions for improvement.

### 3. 2D Convolution
- **Task**: Compute a 2D convolution of a pre-defined filter with 2D data, handling boundary conditions by bleeding values.
- **Details**: Detailed calculations provided for results A, B, C, and D.

### 4. Comments and Suggestions on the Course
- **Feedback**: Suggestions for course improvement, topics of interest, and skills to be learned.

## Results
The results of the analysis, including visualizations and critiques, are stored in the `results` directory. Key findings include:
- Anxiety severity follows a natural distribution, with moderate levels being more prevalent.
- Weak correlations between most variables suggest anxiety is influenced by multiple independent factors.
- Physiological factors like heart rate and breathing rate are not strong predictors of anxiety severity.
- Younger individuals and females report higher anxiety levels.

## Requirements
To replicate the analysis, install the required Python packages using:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script to generate visualizations and perform analysis:
```bash
python src/main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.