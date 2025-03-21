#!/usr/bin/env python3
import sys
from collections import defaultdict

hour_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    hour, value = line.strip().split("\t")
    
    try:
        value = int(value)
        hour_counts[hour] += value
    except ValueError:
        continue  # Skip invalid lines

# Sort hours by count in descending order
sorted_hours = sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
for hour, count in sorted_hours:
    print(f"{hour}\t{count}")

