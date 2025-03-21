#!/usr/bin/env python3
import sys
from collections import defaultdict

street_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    street_code, value = line.strip().split("\t")
    
    try:
        value = int(value)
        street_counts[street_code] += value
    except ValueError:
        continue  # Skip invalid lines

# Sort by count in descending order
sorted_streets = sorted(street_counts.items(), key=lambda x: x[1], reverse=True)

# Print sorted results
for street_code, count in sorted_streets:
    print(f"{street_code}\t{count}")
