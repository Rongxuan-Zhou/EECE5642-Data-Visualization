import numpy as np
import colorsys
import matplotlib.pyplot as plt
import os

def rgb_to_xyz(r, g, b):
    # Normalize RGB values to [0,1]
    r = r/255
    g = g/255
    b = b/255
    
    # Apply sRGB to XYZ conversion matrix
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    
    return x, y, z

def rgb_to_cmyk(r, g, b):
    # Normalize RGB values to [0,1]
    r = r/255
    g = g/255
    b = b/255
    
    k = 1 - max(r, g, b)
    if k == 1:
        return 0, 0, 0, 1
    
    c = (1-r-k)/(1-k)
    m = (1-g-k)/(1-k)
    y = (1-b-k)/(1-k)
    
    return c, m, y, k

# Original RGB values
rgb = [137, 56, 146]
r, g, b = rgb

# 1. RGB to XYZ conversion
x, y, z = rgb_to_xyz(r, g, b)
print(f"XYZ: ({x:.4f}, {y:.4f}, {z:.4f})")

# 2. XYZ to xyY conversion
sum_xyz = x + y + z
if sum_xyz == 0:
    x_chrom = y_chrom = 0
else:
    x_chrom = x / sum_xyz
    y_chrom = y / sum_xyz
print(f"xyY: ({x_chrom:.4f}, {y_chrom:.4f}, {y:.4f})")

# 3. RGB to CMYK conversion
c, m, y, k = rgb_to_cmyk(r, g, b)
print(f"CMYK: ({c:.4f}, {m:.4f}, {y:.4f}, {k:.4f})")

# 4. RGB to HSV conversion
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
print(f"HSV: ({h:.4f}, {s:.4f}, {v:.4f})")

# 5. RGB to HSL conversion
h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
print(f"HSL: ({h:.4f}, {s:.4f}, {l:.4f})")

# Create save directory
save_dir = os.path.join('..', 'results', 'figures')
os.makedirs(save_dir, exist_ok=True)

# Create color swatch and save
plt.figure(figsize=(2, 2))
plt.imshow([[rgb]])
plt.axis('off')

# Save image
save_path = os.path.join(save_dir, 'color_sample.png')
plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=300)
plt.close()

print(f"\nColor swatch saved to: {save_path}")