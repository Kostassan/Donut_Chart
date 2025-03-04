# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:50:36 2024

@author: ksideris
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as mpatches

# Load data from CSV
data = pd.read_csv(r'C:\Users\ksideris\Documents\Diageo Calculations\Piechart_Arbilot_Separate.csv')


# Extract data for inner and outer rings, including labels
labels = data['Label'].tolist()
inner_values = data['Inner Value'].tolist()
outer_values = data['Outer Value'].tolist()
inner_labels = data['Inner Label'].tolist()  # New field for inner ring labels
outer_labels = data['Outer Label'].tolist()  # New field for outer ring labels

# Colors for the rings
inner_colors = ['#88BBEE', '#CC6677', '#999933']
outer_colors = ['#88BBEE', '#CC6677', '#999933']

# Border color for the rings
border_color = 'grey'  # Color for the border of the rings
inside_border_color = 'grey'  # Color for the border around the inner ring's hole

# Create the figure
fig, ax = plt.subplots()

# Create the **white circle** in the middle (the hole of the donut)
inner_circle = plt.Circle((0, 0), 0.7, color='white', edgecolor=inside_border_color, linewidth=3, linestyle='solid')
ax.add_artist(inner_circle)

# Create the outer ring with border (donut band)
outer_wedges, _ = ax.pie(outer_values, radius=1.3, colors=outer_colors,
                         wedgeprops=dict(width=0.3, edgecolor=border_color, linewidth=1))

# Create the inner ring with border (donut band)
inner_wedges, _ = ax.pie(inner_values, radius=1, colors=inner_colors,
                         wedgeprops=dict(width=0.3, edgecolor=border_color, linewidth=1))

# Add values inside the inner ring (displaying the inner labels)
for i, p in enumerate(inner_wedges):
    # Midpoint angle of the wedge
    theta = np.deg2rad((p.theta1 + p.theta2) / 2)
    # Position for the inner ring value
    x_inner, y_inner = 0.85 * np.cos(theta), 0.85 * np.sin(theta)
    ax.text(x_inner, y_inner, f"{inner_labels[i]}", ha='center', va='center', fontsize=8, color='black')

# Add values inside the outer ring (displaying the outer labels)
for i, p in enumerate(outer_wedges):
    # Midpoint angle of the wedge
    theta = np.deg2rad((p.theta1 + p.theta2) / 2)
    # Position for the outer ring value (aligned but further out)
    x_outer, y_outer = 1.15 * np.cos(theta), 1.15 * np.sin(theta)
    ax.text(x_outer, y_outer, f"{outer_labels[i]}", ha='center', va='center', fontsize=8, color='black')

# Create the legend using the colors from the wedges
# Create a list of patches with the appropriate colors and labels
legend_patches = [mpatches.Patch(color=outer_colors[i], label=labels[i]) for i in range(len(labels))]

# Add legend with correct colors in the lower-right corner
ax.legend(handles=legend_patches, loc='lower right', bbox_to_anchor=(1.8, -0.1), fontsize=10)

# Adjust the aspect ratio to be equal so the pie chart is circular
ax.set(aspect="equal")

# Save the chart as a high-resolution PNG

plt.savefig("Pie_Chart_Arbilot.png", dpi=300, bbox_inches='tight')  # High-resolution save
plt.show()