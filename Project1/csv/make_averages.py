import csv
import os
import glob
import pandas as pd
from pathlib import Path

folder_path = "/Users/willtran/PycharmProjects/cs165/Project1/csv"
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

for file_path in csv_files:
    file_name = Path(file_path).stem
    column_names = ["x", "Time(ns)"]
    df = pd.read_csv(file_path, header=None, names=column_names)
    result_dict = {}
    for i, j in zip(df["x"],df["Time(ns)"]):
        result_dict[i] = result_dict.setdefault(i, 0) + j
    for key in result_dict.keys():
       result_dict[key] /= 10
    with open(f"{file_name}_avg.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "avg Time (ns)"])
        for i, j in result_dict.items():
            writer.writerow([f"{i}", f"{j}"])

