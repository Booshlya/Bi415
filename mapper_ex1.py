#!/usr/bin/env python
import sys
import time

# reading
for line in sys.stdin:
    line = line.strip()  
    columns = line.split('\t')  
    if len(columns) == 4:
        timestamp = int(columns[3])  
        date = time.strftime("%Y-%m", time.gmtime(timestamp))  
        print(f"{date}\t1")  