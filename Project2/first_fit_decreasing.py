from zipzip_tree import ZipZipTree
from insertion_sort import insertion_sort
from first_fit import first_fit
def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    items = insertion_sort(items).reverse()
    first_fit(items, assignment, free_space)
