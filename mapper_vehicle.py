#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    if len(fields) > 4 and fields[35] and fields[7]:  # Ensure columns exist and are not empty
        vehicle_year = fields[35].strip()
        vehicle_make = fields[7].strip()
        print(f"{vehicle_year},{vehicle_make}\t1")
