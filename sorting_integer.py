#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Time Complexity: O(n) there are no nested loops, even though there are multiple loops, they execute separately so the coefficients are dropped
    it could be O(n+k) where k is the size of the *range of inputs (not the size of inputs themself and if k is very large compared to n, it would be a dominating factor. )
    Space Complexity: O(n) there are several lists created during the function and they are all detemrined by the size of the input """ 
    
# how to find the min and max values, set two starter variables, min and max
# then traverse the list and compare each number to both. if smaller then min or larger than max, replace with 
# current number
    if len(numbers) <= 1:
        return
    min_value = numbers[0]
    max_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    # create a new list called counts and set the indexes to the max-min value +1, this forces the counts list
    # to have a number of elements = the range of the numbers in the input list. set each element in counts at 0 to start

    counts =[0] * (max_value - min_value + 1)
    # now the indexes will be relationally tied to the nums in the input list, and the values of those indees
    # will represent the number of times that number appears in the input list. 
    for num in numbers:
        counts[num - min_value] += 1
    # now convert the counts list back their og values from numbers, they will already be in order since the list was set in a range

# use the indexes of counts to provide the values that correlate back to input nums, the values of counts
# willbe the number of times that number appears in the output list.
    output = []
    for index, count in enumerate(counts):
        value = index + min_value
        output.extend([value] * count)
# items[:] replaces contents in-place (mutates the original list)
    numbers[:] = output

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list