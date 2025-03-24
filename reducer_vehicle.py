#!/usr/bin/env python3
import sys
from collections import defaultdict

vehicle_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    key, value = line.strip().split("\t")
    
    try:
        value = int(value)
        vehicle_counts[key] += value
    except ValueError:
        continue  # Skip invalid lines

# Sort by count in descending order
sorted_vehicles = sorted(vehicle_counts.items(), key=lambda x: x[1], reverse=True)[:100] # added to limit to the top 100 or you will not see the top values in the terminal

# Print sorted results
for vehicle, count in sorted_vehicles:
    print(f"{vehicle}\t{count}")
