#!/bin/bash
python3 generate_test_files.py
mv streakconditions.csv backup_streakconditions.csv
mv test_streakconditions.csv streakconditions.csv