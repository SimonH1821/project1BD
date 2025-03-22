#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    if len(fields) > 34 and fields[33]:  # Ensure column exists and is not empty
        vehicle_color = fields[33].strip().upper()  # Convert to uppercase for consistency
        print(f"{vehicle_color}\t1")
