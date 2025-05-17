import glob
import os
from pathlib import Path

import pandas as pd
import csv
import math

import numpy as np
from matplotlib import pyplot as plt

from zipzip_tree import ZipZipTree
import random
from first_fit import first_fit, first_fit_decreasing
from next_fit import next_fit
from best_fit import best_fit, best_fit_decreasing

def compute_waste(algorithm, items):
    # number of bins - length of items
    bins_used = algorithm(items)
    total_size = sum(items)
    return bins_used - total_size

def test():
    n_values = [2 ** i for i in range(1, 16)]
    # random.shuffle(n_values)
    num_trials = 3500


    algorithms = {
        'Next Fit': next_fit,
        'First Fit': first_fit,
        'Best Fit': best_fit,
        'First Fit Decreasing' : first_fit_decreasing,
        'Best Fit Decreasing' : best_fit_decreasing
    }

    results = {name: [] for name in algorithms}
    for i in n_values:
        for name, algo in algorithms.items():
            avg_waste = 0
            for _ in range(num_trials):
                items = [random.uniform(0.0, 0.35) for _ in range(i)]
                free = []
                buckets = algo(items, [0] * len(items), free)
                #  len(free_space) - sum(item_list)
                avg_waste += len(free) - sum(items)
                print(len(free), buckets)
                print(f"Function: {name}, num {math.log2(i)}, trial {_} avg_waste: {avg_waste}")
            avg_waste /= num_trials
            results[name].append(avg_waste)


    for name, data in results.items():
        filename = name.lower().replace(" ", "_") + "3500.csv"
        with open(filename, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["n", "avg_waste"])
            for index, waste in enumerate(data, start=1):
                writer.writerow([f"2^{index}", waste])


if __name__ == "__main__":
    test()
    # print(glob.glob("/Users/willtran/PycharmProjects/cs165/Project2/csv"))
    # csv.graph()


