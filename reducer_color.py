#!/usr/bin/env python3
import sys
from collections import defaultdict

color_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    color, value = line.strip().split("\t")
    
    try:
        value = int(value)
        color_counts[color] += value
    except ValueError:
        continue  # Skip invalid lines

# Sort by count in descending order
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
for color, count in sorted_colors:
    print(f"{color}\t{count}")
