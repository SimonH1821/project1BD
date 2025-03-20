#!/usr/bin/env python3
import sys

current_hour = None
count = 0

for line in sys.stdin:
    hour, value = line.strip().split("\t")
    
    try:
        value = int(value)
        
        if current_hour == hour:
            count += value
        else:
            if current_hour is not None:
                print(f"{current_hour}\t{count}")
            
            current_hour = hour
            count = value
    except ValueError:
        continue  # Ignore lines with invalid values

# Print the last accumulated result
if current_hour is not None:
    print(f"{current_hour}\t{count}")
