import csv
import os
import glob
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder_path = "/Users/willtran/PycharmProjects/cs165/Project1/csv"
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

avg_folder_path = "/Users/willtran/PycharmProjects/cs165/Project1/avg"
avg_csv_files = glob.glob(os.path.join(avg_folder_path, "*.csv"))

def gather_averages():
    for file_path in csv_files:
        print(file_path)
        file_name = Path(file_path).stem
        column_names = ["x", "Time(ns)"]
        df = pd.read_csv(file_path, header=None, names=column_names)
        result_dict = {}
        for i, j in zip(df["x"], df["Time(ns)"]):
            try:
                result_dict[i] = result_dict.setdefault(i, 0) + j
            except Exception as e:
                print(e)
                continue
        for key in result_dict.keys():
            result_dict[key] /= 10
        with open(f"{avg_folder_path}/{file_name}_avg.csv", mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["x", "avg Time (ns)"])
            for i, j in result_dict.items():
                writer.writerow([f"{i}", f"{j}"])



def graph_averages():
    for file_path in avg_csv_files:
        file_name = Path(file_path).stem
        df = pd.read_csv(file_path)

        x = np.array(df["x"])
        y = np.array(df["avg Time (ns)"])

        # Avoid log(0) by clipping very small values
        x = np.clip(x, 1e-10, None)
        y = np.clip(y, 1e-10, None)

        # Log transform for linear fitting
        log_x = np.log2(x)
        log_y = np.log2(y)

        # Linear fit in log-log space
        slope, intercept = np.polyfit(log_x, log_y, 1)

        # Corrected: use original x to compute fit_y in linear space
        fit_y = 2 ** intercept * np.log2(x) ** slope

        # Plot on log-log scale
        plt.figure(figsize=(8, 6))
        plt.loglog(x, y, marker="o", label="Data")
        plt.loglog(x, fit_y, linestyle="--", color="r", label=f"Fit: y ≈ x^{slope:.2f}")

        plt.xlabel("x", fontsize=12)
        plt.ylabel("avg Time (ns)", fontsize=12)
        plt.title(f'Log-Log Plot {file_name}', fontsize=14)
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.show()


def graph_averages2():
    for file_path in avg_csv_files:
        file_name = Path(file_path).stem
        df = pd.read_csv(file_path)


        df["avg Time (ns)"] = df["avg Time (ns)"] / 1e9

        df["x"] = 2 ** df["x"]
        x = df["x"]
        print(x)
        y = df["avg Time (ns)"]


        # Log transform for linear fitting
        log_x = np.log2(x)
        log_y = np.log2(y)

        # Linear fit in log-log space
        slope, intercept = np.polyfit(log_x, log_y, 1)

        # Corrected: use original x to compute fit_y in linear space
        # fit_y = 2 ** intercept * np.log2(x) ** slope

        # Plot on log-log scale
        # plt.figure(figsize=(8, 6))
        plt.loglog(x, y, marker="o", label="Data")
        plt.loglog(x, 2 ** (slope * np.log2(x) + intercept), base=2, linestyle="--", color="r",
                   label=f"Fit: y ≈ {slope:.5f}log N + {intercept:.5f}")

        plt.xlabel("x", fontsize=12)
        plt.ylabel("avg Time (s)", fontsize=12)
        plt.title(f'Log-Log Plot {file_name}', fontsize=14)
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.show()





def plot_group(file_pattern, title):
    files = glob.glob(file_pattern)
    plt.figure(figsize=(10, 7))

    for file_path in files:
        print(file_path)
        file_name = Path(file_path).stem
        df = pd.read_csv(file_path)

        # Convert time to seconds
        df["avg Time (ns)"] = df["avg Time (ns)"] / 1e9

        # x values: 2^x
        df["x"] = 2 ** df["x"]
        x = df["x"]
        y = df["avg Time (ns)"]

        # Log transform
        log_x = np.log2(x)
        log_y = np.log2(y)

        # Linear fit in log-log space
        slope, intercept = np.polyfit(log_x, log_y, 1)

        # Plot original data points
        plt.loglog(x, y, marker="o", linestyle='', label=f"{file_name} - {slope:.5f} log N + {intercept:.5f}")

        # Plot fitted curve
        plt.loglog(x, 2 ** (slope * np.log2(x) + intercept), base=2)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time (s)")
    plt.title(title)
    plt.legend(fontsize=8)
    # plt.grid(True, which="both", ls="--")
    plt.show()


# Plot each group

if __name__ == "__main__":
    # gather_averages()
    # graph_averages2()
    # plot_group(f'{avg_folder_path}/*almost_sorted_avg.csv', 'Performance on Almost-Sorted Data (Log-Log)')
    # plot_group(f'{avg_folder_path}/*alt_runs_avg.csv', 'Performance on Alternating Runs Data (Log-Log)')
    # plot_group(f'{avg_folder_path}/*uniform_avg.csv', 'Performance on Uniform Random Data (Log-Log)')
    # plot_group(f'{avg_folder_path}/insertion_sort*.csv', 'Insertion Sort')
    # plot_group(f'{avg_folder_path}/shell_sort1*.csv', 'Shell Sort 1')
    # plot_group(f'{avg_folder_path}/shell_sort2*.csv', 'Shell Sort 2')
    # plot_group(f'{avg_folder_path}/shell_sort3*.csv', 'Shell Sort 3')
    # plot_group(f'{avg_folder_path}/shell_sort4*.csv', 'Shell Sort 4')
    # plot_group(f'{avg_folder_path}/shell_sort5*.csv', 'Shell Sort 5')
    # plot_group(f'{avg_folder_path}/tim_sort*.csv', 'Tim Sort')
    plot_group(f'{avg_folder_path}/shell_sort*.csv', 'Shell Sort')



