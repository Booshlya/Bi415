#!/usr/bin/env python3
# Improved Combiner
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    
    if len(parts) != 2:
        continue  # Пропуск некорректных строк

    key, value = parts

    try:
        value = int(value)
    except ValueError:
        continue  # Пропуск строк с ошибками в числе

    if key == current_key:
        current_count += value
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = value

if current_key is not None:
    print(f"{current_key}\t{current_count}")