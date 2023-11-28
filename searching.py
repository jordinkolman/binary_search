import random
from timeit import repeat, timeit
import bisect

def run_search_algorithm(algorithm, array, value):
     # Set up context and algorithm call using supplied array
    
    # Only import algorithm function if its not the built-in sorted()
    setup_code = f"from __main__ import {algorithm}"
        
    stmt = f"{algorithm}({array}, {value})"
    
    # Executed code 10 different times and return time in seconds execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    
    # Display name of algorithm and minimum time it took to run
    print(f"Algorithm: {algorithm}. Element {value} Found. Minimum execution time: {min(times)}")
    

def random_search(array, value):
    # Search for element while it is not found
    while True:
        # Select random element from array and check against value
        random_element = random.choice(array)
        if random_element == value:
            return random_element
        
        
def linear_search(array, value):
    # Iterate through array until you find value
    for index, element in enumerate(array):
        if element == value:
            return index
        
        
# Python's Binary Search implementation
def bisect_left(array, value):
    index = bisect.bisect_left(array, value)
    # ensure index actually contains value instead of where the value 'should' go before returning
    if index < len(array) and array[index] == value:
        return index


#Iterative Binary Search Implementation

#identity function for Binary Search
def identity(element):
    return element
    

# Where Is It?
#Function to find index of a specific value, given a key for that value
def find_index(array, value, key=identity):
    # set values for upper and lower bounds
    left, right = 0, len(array) - 1
    
    # search iteratively until lower and upper bounds are reached
    while left <= right:
        # set middle as midpoint between upper and lower bounds
        middle = (left + right) // 2
        # store key/value (identical) of midpoint
        middle_element = key(array[middle])
        
        # check midpoint against value
        if middle_element == value:
            return middle
        
        # reset upper or lower bound depending if value is above or below midpoint
        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1
            

# Is it there?
# checks if an array contains a specific value
def contains(array, value, key=identity):
    return False if find_index(array, value, key) == None else True


# What is it?
# finds a specific value in an array
def find(array, value, key=identity):
    index = find_index(array, value, key)
    return array[index]
    

# Where is it?
# Finds the leftmost instance of a value in an array
def find_leftmost_index(array, value, key=identity):
    # first make sure that value exists in the array
    index = find_index(array, value, key)
    if index is not None:
        # continue shifting index left until a different value is reached
        while index >= 0 and key(array[index]) == value:
            index -= 1
        # shift index back to leftmost instance of value
        index += 1
    return index


# Where is it?
# Finds the rightmost instance of a value in an array
def find_rightmost_index(array, value, key=identity):
    # first make sure the value exists in the array
    index = find_index(array, value, key)
    if index is not None:
        # continue shifting index to right until a different value is reached
        while index < len(array) and key(array[index]) == value:
            index += 1
        # shift index back to rightmost instance of value
        index -= 1
    return index


# Where is it?
# finds all occurences of a given value in an array
def find_all_indices(array, value, key=identity):
    # Find the leftmost occurence of the value
    left = find_leftmost_index(array, value, key)
    # Find the rightmost occurence of the value
    right = find_rightmost_index(array, value, key)
    # if left and right both exist, return the set of indices between and including left and right
    if left and right:
        return set(range(left, right + 1))
    # otherwise, return an empty set
    return set()


# What is it?
# Returns the value of the leftmost index in the array, or None if not found
def find_leftmost(array, value, key=identity):
    index = find_leftmost_index(array, value, key)
    return None if index is None else array[index]


# What is it?
# Returns the value of the rightmost index of the array, or None if not found
def find_rightmost(array, value, key=identity):
    index = find_rightmost_index(array, value, key)
    return None if index is None else array[index]


# What is it?
# Returns value of all matching elements in an array
def find_all(array, value, key=identity):
    return {array[i] for i in find_all_indices(array, value, key)}


# Recursive implementation of binary search
def contains_recursive(array, value):
    left, right = 0, len(array) - 1
    
    if left <= right:
        middle = (left + right) // 2
        
        if array[middle] == value:
            return True

        if array[middle] < value:
            return contains_recursive(array[middle + 1:], value)
        elif array[middle] > value:
            return contains_recursive(array[:middle], value)

    return False


ARRAY_LENGTH = 10000
    
if __name__ == '__main__':
    # for search, we want a sorted array
    array = sorted([random.randint(0, 10000) for _ in range (ARRAY_LENGTH)])
    value = random.choice(array)
    
    #Random Search Algorithm
    run_search_algorithm(algorithm='random_search', array=array, value=value)
    
    #Linear Search Algorithm
    run_search_algorithm(algorithm='linear_search', array=array, value=value)
    print(f'Index of Located Value: {linear_search(array, value)}')
    
    #Binary Search with Bisect
    run_search_algorithm(algorithm='bisect_left', array=array, value=value)
    print(f'Index of Located Value: {bisect_left(array, value)}')
    
    # Binary Searches 
    # find_index()
    run_search_algorithm(algorithm='find_index', array=array, value=value)
    print(f'Find Index Return Value: {find_index(array, value)}')
    
    # find()
    run_search_algorithm(algorithm='find', array=array, value=value)
    print(f'Find Return Value: {find(array, value)}')
    
    # contains()
    run_search_algorithm(algorithm='contains', array=array, value=value)
    print(f'Contains Return Value: {contains(array, value)}')
    print(f'Contains False Test Value: {contains(array, 100001)}')
    
    # contains_recursive()
    run_search_algorithm(algorithm='contains_recursive', array=array, value=value)
    print(f'Contains Recursive Value: {contains_recursive(array, value)}')
    print(f'Contains Recursive False Test Value: {contains(array, 100001)}')
    
    # find_leftmost_index()
    run_search_algorithm(algorithm='find_leftmost_index', array=array, value=value)
    print(f'Find Leftmost Index Return Value: {find_leftmost_index(array, value)}')
    
    #find_rightmost_index()
    run_search_algorithm(algorithm='find_rightmost_index', array=array, value=value)
    print(f'Find Rightmost Index Return Value: {find_rightmost_index(array, value)}')
    
    # find_all_indices()
    run_search_algorithm(algorithm='find_all_indices', array=array, value=value)
    print(f'Find All Indices Return Value: {find_all_indices(array, value)}')
    
    # find_leftmost()
    run_search_algorithm(algorithm='find_leftmost', array=array, value=value)
    print(f'Find Leftmost Return Value: {find_leftmost(array, value)}')
    
    #find_rightmost()
    run_search_algorithm(algorithm='find_rightmost', array=array, value=value)
    print(f'Find Rightmost Return Value: {find_rightmost(array, value)}')
    
    #find_all()
    run_search_algorithm(algorithm='find_all', array=array, value=value)
    print(f'Find All Value: {find_all(array, value)}')
    
    