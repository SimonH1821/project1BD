#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')
    
    if len(fields) > 5 and fields[19]:  # Ensure column index exists and is not empty
        violation_time = fields[19].strip()
        
        # Extracting hour from Violation Time (Format: HHMM(A/P))
        if len(violation_time) >= 4:
            hour = violation_time[:2] + violation_time[-1]  # Get first two characters as hour and the A/p for AM or PM
            print(f"{hour}\t1")
