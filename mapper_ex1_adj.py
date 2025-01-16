#!/usr/bin/env python
# mapper_ex1_adj.py

import sys
import time
import os

# Чтение переменной окружения
use_day_of_week = os.getenv("USE_DAY_OF_WEEK", "false").lower() == "true"

# Чтение входных данных
for line in sys.stdin:
    line = line.strip()
    columns = line.split('\t')

    if len(columns) == 4:
        timestamp = int(columns[3])
        
        if use_day_of_week:
            # Если нужно использовать день недели
            date = time.strftime("%A", time.gmtime(timestamp))  # День недели (например, "Monday")
        else:
            # Если нужно использовать месяц
            date = time.strftime("%Y-%m", time.gmtime(timestamp))  # Месяц в формате YYYY-MM

        print(f"{date}\t1")