#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    if len(fields) > 11 and fields[9]:  # Ensure column exists and is not empty
        street_code = fields[9].strip()
        print(f"{street_code}\t1")
