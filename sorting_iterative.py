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
                # swap the items using tuple unpacking
                items[i], items[i + 1] = items[i + 1], items[i]
                
                # set the flag to True to continue the loop
                swapped = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Time Complexity: O(n^2), its determined by the nested loops. The outer loop runs n times, and the inner loop runs progressively fewer times, n-1, n-2, n-3, etc for each iteration of the outer loop.
    Space Complexity: O(1), just the 2 variables current_minium_index and i which are constant space, no matter list size. No new lists or data structures. """
    # first, find the minimum and put it at index 0, then, ignore index 0 and now look at index 1 and find 
    # the next minimum, then place that at position 1, then ignore index 1 and find the minimum, etc, etc. 
    # so i'd need a for loop to traverse the indexes and then for every index, another loop that runs a check 
    # through the entire list for the minimum. and how would I track that minimum? I guess I could use a current_minimum_index variable 
    # and as the inner loop is traversing, it will compare index with index and if value is lower then replace the value of current_minimum_index. 
    # then when that inner loop is done, set the current_minimum_index as the value of the current index for the outer loop.
    
    # this is the outer loop that traverses the indexes, i starts at index 0 and i is index 0
    for i in range(len(items)):
        current_minimum_index = i
        # this is the inner loop that finds the minimum value of the remaining indexes, using a second iterator, j
        for j in range(i + 1, len(items)):
            # this is the comparison that finds the minimum
            if items[j] < items[current_minimum_index]:
            # rewrite the current_minimum_index if a lower value is found
                current_minimum_index = j
        items[i], items[current_minimum_index] = items[current_minimum_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Time Complexity: O(n^2), its determined by the nested loops. The outer loop runs n times, and the inner loop runs progressively more times, for each iteration of the outer loop.
    Space Complexity: O(1), just the 2 variables current_item and j which are constant space, no matter list size. No new lists or data structures. """
    # this is the outer loop that traverses the indexes, i is index 0 and i is the first unsorted postion
    for i in range(len(items)): 
        # save the value that I'm inserting
        current_item = items[i]
        # j is the index just to the left of i, i-1
        j = i - 1
        # the conditional j >= 0 prevents j from ever being a negative index 
        # this is also the inner loop that checks the sorted portion of the list
        while j >= 0 and items[j] > current_item: # this is checking if there is a bigger value to the left 
            # shift the value to the right, to make room for the current_item
            items[j + 1] = items[j]
            # move the iterator to the left to keep the inner loop going
            j -= 1
        # drop current_item  into the spot created by the inner loop (technically overwriting a duplicate, not an open position)
        # the inner loop ends if we hit the left edge (j < 0) or we find an element <= to current_item
        items[j + 1] = current_item