# Data Visualization Homework 2

Repository: [EECE5642-Data-Visualization/HW2](https://github.com/Rongxuan-Zhou/EECE5642-Data-Visualization/tree/main/HW2)

## 1. Visualization Design

### a. Bad Design Analysis
Source: [Junk Charts Blog Post](https://junkcharts.typepad.com/junk_charts/2025/01/ranks-labels-metrics-data-and-alignment.html)

#### Data-ink Ratio Issues:
- 45-degree slanted design creates excessive non-essential white space
- Decorative airplane icons convey no actual information
- Redundant labels and legends occupy too much space

#### Lie Factor Analysis:
- Reverse ranking representation can be misleading
- Asterisk annotations needed to explain meanings
- Longer bars for "best" contradicts intuitive understanding

#### Clarity Issues:
- Text labels at 45-degree angles are difficult to read
- Multi-level information display complicates simple data
- Requires head tilting for proper reading

### b. New Design Principles

#### Readability Improvements:
- Use horizontal bar charts to avoid tilted text
- Display performance values directly instead of rankings
- Use clear metric names and avoid negative phrasing

#### Information Display Optimization:
- Group related metrics together
- Use gridlines to assist value comparison
- Add percentage labels for intuitive performance display

#### Visual Enhancement:
- Remove decorative elements
- Use subtle gridlines
- Adopt a clear color scheme

#### Functional Improvements:
- Display actual performance data directly
- Simplify information hierarchy
- Provide intuitive data comparison

## 2. Color Analysis

### a. Coding Resources:
- Python standard library: colorsys module
- Matplotlib library for color swatches
- NumPy library for numerical computations
- Colormath library for precise color space conversions
- Reference resources:
  - EasyRGB's conversion formulas
  - Wikipedia's color space entries
  - Bruce Lindbloom's transformation equations

### b. Color Values:
```
RGB: (137/255, 56/255, 146/255) = (0.5373, 0.2196, 0.5725)
XYZ: (0.4034, 0.3126, 0.5808)
xyY: (0.3111, 0.2411, 0.3126)
CMYK: (0.0616, 0.6164, 0.0000, 0.4275)
HSV: (0.8167, 0.6164, 0.5725)
HSL: (0.8167, 0.4455, 0.3961)
```

Description: Purple hue leaning towards magenta, medium brightness, moderate saturation

## 3. Table & Graph Comparison

### Visualization Comparison Analysis:

#### Table Advantages:
- Precise presentation of exact values
- Easy to look up specific numbers
- Good for comparing individual values
- Shows all three metrics

#### Table Disadvantages:
- Difficult to see trends over time
- Takes more space
- Requires more time to process information

#### Graph Advantages:
- Clear visualization of trends
- Easy to compare patterns
- Intuitive understanding of changes
- Compact representation

#### Graph Disadvantages:
- Only shows acceptance rate
- Can become cluttered
- Less precise for exact values

## 4. Visual Perception and Cognition Analysis

### a. Visual Perception Level

#### Physical Similarity:
- Yellow (#FFFF00) background
- Equal spacing arrangement
- Consistent geometric sans-serif font

#### Gestalt Principles:
- Proximity: Characters perceived as unit
- Continuity: Sequential arrangement
- Closure: Unified visual element

### b. Cognitive Processing Level

#### Context Effects:
- Left image: Alphabet sequence (A→B→C)
- Right image: Numerical sequence (12→13→14)

#### Processing:
- Automatic: Shape recognition
- Controlled: Context-based interpretation

### c. Cognitive Conflict and Resolution

#### Conflicts:
- Symbol ambiguity
- Category switching

#### Resolution:
- Context dependency
- Experience application
- Pattern completion