#!python
from sorting_iterative import selection_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Time Complexity: O(n),  no nested loops, time is determined byt th etotal elements in both lists
    Space Complexity: O(n),we have to create a new third list whose size is variable based on lists 1 and 2 """
    # create a new third list "results" from the contents of items1 and items2. 
    # use a pointer variable for each list to track the current index.
    # compare the first item of list1 witht he first item of list. whichever is smaller become the first value
    # of the results list. then increment the pointer for the list that provided the smaller value.
    # repeat the process until one of the lists is empty. How will I know that one of the lists is empty?
    # the conditional for this will be if the pointer for either list ever equals the length of the list -1
    # can run this check for the pointer at the end of every comparison loop and if the pointer has hit the 
    # end of the list, then the list is empty and we can append the remaining items from the non-empty list to the results list.
    # then append the remaining items from the non-empty list to the results list.
    # return the results list.
    results = []
    # setup pointers to track the current index of each list
    pointer1 = 0
    pointer2 = 0
    # while the pointers are still within the bounds of the lists, compare the items at the pointers
    # increase the value of the pointer belonging to the list who's value wss lower and taken
    while pointer1 < len(items1) and pointer2 < len(items2):
        if items1[pointer1] < items2[pointer2]:
            results.append(items1[pointer1])
            pointer1 += 1
        else:
            results.append(items2[pointer2])
            pointer2 += 1
    # AFTER the loop exits, one list might still have items
    # These two lines handle BOTH cases (only one will add anything bc th eother list is empty)
    # use extend bc it adds multiple values as individual items to results. append adds multiple items as
    # one single object (a nested list of the remaining items)
    results.extend(items1[pointer1:])
    results.extend(items2[pointer2:])
    return results
    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Time Complexity: O(n^2), from calling selection_sort, the sort merge has no loops and doesn't
    iterate over every element. 
    Space Complexity: O(n), the size of the list is variable and that determines 
    the size of the two new data structures, also calls selection_sort, which is O(1)"""
    
    # list with 0 or 1 items is already sorted - return the list
    if len(items) <= 1:
        return
    
    # SPLIT: find midpoint and create two halves using splicing
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]
    
    # call selection_sort on both halves
    selection_sort(left_half)
    selection_sort(right_half)

    # merge the two sorted halves into one list, mutate the list in place using items[:]= syntax
    # don't need to return anything because the list is mutated in place
    items[:] = merge(left_half, right_half)
    

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Time Complexity: O(n log n), there are log(n) levels of splitting (keep splitting) and at each level
    there are n elements to be merged (through the merge helper) which is O(n)
    Space Complexity:O(n), merge helper creates a new result list that holds all elements O(n), 
    slicing creates copies but there is only one active copy at a time
    log(n) = "how many times can I cut this in half?"""
    # check for the base case, list is size 0 or 1, then build up from there by calling merge helper
    # the main work of this function will be the splitting. will need to grab the length of the list and divide by 2 to find the halfway point
    # then perform check to see if that halved list is 0 or 1 element, if so start the build out process with merge helper
    # if not continue calling the split recursively until the base case is hit.
    
    # BASE CASE: list with 0 or 1 items is already sorted - stop recursing
    if len(items) <= 1:
        return
    
    # SPLIT: find midpoint and create two halves using splicing
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]
    
    # RECURSIVE CALLS: sort each half (they'll keep splitting until base case)
    merge_sort(left_half)
    merge_sort(right_half)
    
    # MERGE: combine the two sorted halves using merge helper
    merged_result = merge(left_half, right_half)
    
    # COPY BACK: replace original list contents with sorted result
    # items[:] replaces contents in-place (mutates the original list)
    items[:] = merged_result


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` . pivot will start the high index, the last item in the list. partition doesn't
    have to assign high or low, quick_sort will assign high + low before partition is called. 
    partition will create a mutated list with everything smaller than p to it's left and everything
    greater than p to it's right. then partition returns the index of the pivot point.
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Time Complexity: O(n), the loop runs n times, determined by the range
    Space Complexity: O(1), just 3 variables, i, j, and pivot, which is constand space """
    # choose the pivot point as the last element, assign that using indexing -1
    # then split the list into two partitions, using the list range, since I'm using the last 
    # element as the pivot, there will only be one partition, which will be :pivot_index or whatever
    # the correct syntax is. then loop through everything in that partition and move everything
    # smaller that the element at pivot_index to the left of pivot_index and everything greater than the element 
    # at pivot_index to the right of pivot_index.
    # then return the index of the pivot_index.
    
    # this is the value of the element at the high index, which everything else will be compared to
    pivot = items[high]
    
    # i is the index that tracks the boundary of the "small items zone"
    # everything at index <= i is smaller than pivot
    # start at low - 1 because the zone is empty at first
    i = low - 1
    
    # loop through all items from low to high-1 (not including pivot itself)
    # j is the index that tracks the current item being compared to the pivot
    for j in range(low, high):
        # if current item is smaller than pivot, it belongs in the small zone
        if items[j] < pivot:
            i += 1  # expand the small zone
            # swap current item into the small zone using tuple unpacking
            items[i], items[j] = items[j], items[i]
    
    # now put pivot in its correct position (right after the small zone)
    # when the loop that used j finishes (gets to the end of its range), the index i has now
    # changed. everytime an item was found to be smaller than pivot, it got move to the left and 
    # i's index value increased by 1. so now, when the loop has finished, i, representing the boundary of the small zone, 
    # can be used as a marker to find the actual pivot in the list, bc it will be i plus 1
    items[i + 1], items[high] = items[high], items[i + 1]
    
    # return the pivot's final index
    return i + 1
    

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
   
    # based on the TDs, I'll need to check if high and low have deault values, I think I can do tha with a
    # if high and if low conditional- that should check to see if any vale exists, otherwise if they are nil, 
    # I assign them these values low =0 (the first index in the list) high = list[-1] (the last index in the list)
    # then I check if the list is the base case, where the len(list) is <= 1
    # then I call the helper, partition, giving it the values of low and high, and the list
    # i get pivot_index back from partition, now recurse on the left side: quick_sort(items, low, pivot_index - 1)
    # recurse on right side: quick_sort(items, pivot_index + 1, high)
    # then I recursively call quick_sort until the base case is reached and then I build back up 
    # from there
    pass