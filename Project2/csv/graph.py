from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def graph():
    directory = "/Users/willtran/PycharmProjects/cs165/Project2/csv"
    files = [f for f in os.listdir(directory) if f.endswith('3500.csv')]
    print(files)

    for file in files:
        file_path = os.path.join(directory, file)
        print(file_path)
        file_name = Path(file).stem
        df = pd.read_csv(file_path)

        # Transform "n" from "2^x" format to exponent, then to actual value
        df['n'] = df['n'].apply(lambda s: 2 ** int(s.strip().replace("2^", "")))

        x = df["n"]
        y = df["avg_waste"]
        print(x, y)

        # Log transform
        log_x = np.log2(x)
        log_y = np.log2(y)

        # Linear fit in log-log space
        slope, intercept = np.polyfit(log_x, log_y, 1)

        # Create a new figure for each plot
        plt.figure(figsize=(10, 7))

        # Plot original data points
        plt.loglog(x, y, marker="o", linestyle='', label=f"{file_name} - {slope:.5f} log N + {intercept:.5f}")

        # Plot fitted curve
        plt.loglog(x, 2 ** (slope * np.log2(x) + intercept), base=2, linestyle='--')

        # Set custom x-axis ticks to match the data range
        max_power = int(np.log2(max(x)))
        ticks = [2 ** i for i in range(max_power + 1)]
        plt.xticks(ticks, [f"2^{i}" for i in range(max_power + 1)])

        min_y_power = int(np.floor(np.log2(min(y))))
        max_y_power = int(np.ceil(np.log2(max(y))))
        y_powers = np.arange(min_y_power, max_y_power + 0.25, 0.25)

        y_ticks = [2 ** i for i in y_powers]
        y_labels = [f"{p:.2f}" if p % 1 != 0 else f"{int(p)}" for p in y_powers]
        plt.yticks(y_ticks, y_labels)

        plt.xlabel("Input Size (n)")
        plt.ylabel("Average Waste")
        plt.title(file_name)
        plt.legend(fontsize=8)
        plt.grid(True, which="both", ls="--")
        plt.show()


# Call the function
graph()