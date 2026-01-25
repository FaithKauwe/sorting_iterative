#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Time Complexity: O(n), its just determined by the length of the list, there are no nested loops
    Space Complexity: O(1), jut a single variable i which is constant space, no matter list size. No new lists or data structures. """
    # for nums: start at the beginning of list, index 0, eachtime through the loop. compare index i with index i+1, 
    # if at any time the value of i+1 is smaller than i, return False and exit the loop.
    # else complete the loop and return True. the for loop will automatically increase the value of i by 1 each time through the loop.
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time Complexity: O(n^2), its determined by the nested loops. The outer loop runs n times, and the inner loop runs n-1 times for each iteration of the outer loop.
    Space Complexity: O(1), just the 2 variables swapped and i which are constant space, no matter list size. No new lists or data structures. """
    # the boolean flag is used to check if the list is sorted
    swapped = True
    # the conditional that keeps the loop running
    while swapped:
        swapped = False
        
        for i in range(len(items) - 1):
            # compare with the next item
            if items[i + 1] < items[i]:
                # swap the items
                items[i], items[i + 1] = items[i + 1], items[i]
                
                # set the flag to True to continue the loop
                swapped = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items