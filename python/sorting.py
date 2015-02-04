def swap(a, b):
    """ Given two things, return them in the opposite order. """
    # TODO: Fill this in.
    return

assert swap(1, 2) == (2, 1)

print("swap completed")

##


def swap_first(items):
    """ Given a list of items, swap the first two items and return the new list. """
    # TODO: Fill this in.
    return

assert swap_first([1, 2, 3, 4]) == [2, 1, 3, 4]

print("swap_first completed")

##


def search(items, target):
    """ Given a list of items, return the position of target. Return None if
    not found. """
    # TODO: Fill this in.
    return

assert search([10, 20, 30, 40], target=20) == 1
assert search([10, 20, 30, 40], target=40) == 3
assert search([30, 20, 10, 40], target=10) == 2
assert search([10, 20, 30, 40], target=50) == None

print("search completed")


##


def binary_search(sorted_items, target):
    """ Given a sorted list of items, return the position of target. Return
    None if not found.

    See if you can use the fact that the items are sorted to optimize the
    search algorithm over the previous challenge.
    """
    # TODO: Fill this in.
    return

assert binary_search([10, 20, 30, 40], target=20) == 1
assert binary_search([10, 20, 30, 40], target=40) == 3
assert binary_search([10, 20, 30, 40], target=50) == None
assert binary_search(range(1000), target=123) == 123

assert binary_search([], target=20) == None
assert binary_search([10], target=10) == 0

print("binary_search completed")


##


def simple_sort(items):
    """ Given a list of items, sort the list and return it. Use any algorithm you can think of. """
    # TODO: Fill this in.
    return


assert simple_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
assert simple_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
assert simple_sort(reversed(range(1000))) == range(1000)
assert simple_sort([]) == []

print("simple_sort completed")

##


def merge(sorted_a, sorted_b):
    """ Given two lists of sorted items, combine them in sorted order. Return a list of both items sorted. """
    # TODO: Fill this in.
    return


assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
assert merge([1], [2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert merge([], [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

print("merge completed")

##


def split_list(items, idx):
    """ Given a list of items, return two lists split on the given idx. """
    # TODO: Fill this in.
    return


assert split_list([1, 2, 3, 4, 5, 6], idx=3) == ([1, 2, 3], [4, 5, 6])
assert split_list([1, 2, 3, 4, 5, 6], idx=1) == ([1], [2, 3, 4, 5, 6])
assert split_list([1, 2, 3, 4, 5, 6], idx=0) == ([], [, 12, 3, 4, 5, 6])
assert split_list([1, 2, 3, 4, 5, 6], idx=1000) == ([1, 2, 3, 4, 5, 6], [])

assert split_list([], idx=0) == ([], [])

print("split_list completed")

##


def merge_sort(items):
    """ Given a list of items, sort them using merge sort.

    Merge sort (recursive):
    - Split items into two halves
    - Call merge sort on each half
    - When each half returns, they should be sorted. Merge the two sorted lists and return
    """
    # TODO: Fill this in.
    return

assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
assert merge_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
assert merge_sort(reversed(range(1000))) == range(1000)
assert merge_sort([]) == []

print("merge_sort completed")

##


def quick_sort(items):
    """ Given a list of items, sort them using quick sort.

    Quick sort is exactly the same as merge sort, except instead of splitting
    in half each time, you pick a random "pivot". The pivot is the index on
    which you split the items.
    """
    # TODO: Fill this in.
    return

assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
assert quick_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
assert quick_sort(reversed(range(1000))) == range(1000)
assert quick_sort([]) == []

print("quick_sort completed")

print("** sorting completed **")
