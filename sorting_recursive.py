#!python


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
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort