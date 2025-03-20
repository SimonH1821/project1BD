#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    if len(fields) > 4 and fields[2] and fields[5]:  # Ensure columns exist and are not empty
        vehicle_year = fields[2].strip()
        vehicle_make = fields[5].strip()
        print(f"{vehicle_year},{vehicle_make}\t1")
