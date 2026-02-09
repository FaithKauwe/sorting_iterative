#!python
from sorting_iterative import insertion_sort

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
    
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

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

# use min and max to find the range of the values in the input list
    range_of_values = max_value - min_value + 1
# create list of empty lists ("buckets")
    buckets = [[] for _ in range(num_buckets)]
# set bucket sixe, it's okay if it doesn't equate to a whole number, it will get converted 
# to an int at the which_buckt_to_assign step
    bucket_size = range_of_values / num_buckets
# loop through and determine which bucket to place each num in. the core of this approach is
# determining how far from the start num and then how many "bucket widths" away. it uses the determined
# range to create even bucket widths that are relational to the numbers and the range
    for num in numbers:
        which_bucket_to_place_num = int((num - min_value) / bucket_size)
# in the the case where the num is exactly max_value which could give a buckets[index] that is out of range
# handle by "clamping" (forcing a value to stay within a certain range)     
        if which_bucket_to_place_num == num_buckets:
            which_bucket_to_place_num = num_buckets - 1
        buckets[which_bucket_to_place_num].append(num)
    
    output_list = []
    for bucket in buckets:
        insertion_sort(bucket) # insertion mutates in place and does not return a sorted list, cannot be chained to the extend
        output_list.extend(bucket)
    numbers[:] = output_list
    


# inputs list : [35, 12, 87, 23, 35, 42, 15]
# step through: min = 12, max = 87, range = 76, bicket_size = 7.6. first num in nums = 35, 
# (35-12)/7.6 >> 23/7.6 >> 3.02 >> bucket at index 3