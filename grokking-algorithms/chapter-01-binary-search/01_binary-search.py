def binary_search(pList, pItem):
    # Start the search with the entire array
    low = 0
    high = len(pList) - 1 # O(n)

    while low <= high: 
        # Find the middle, Python rounds to floor
        # mid = (low + high) / 2 # This returns a float value
        mid = (low + high) // 2
        # Get the guess
        guess = pList[mid] 

        # Found the item and return its index
        if pItem == guess:
            return mid

        # If guess is too high the new high is mid-1 (mid was already used)
        if pItem < guess:
            high = mid - 1
        # If guess is too low the new low is mid+1 (mid was already used)
        else:
            low = mid + 1

    # If the item is not found return None
    return None

my_list = [1, 3, 3, 5, 7, 9, 10]
print(binary_search(my_list, 3))
print(binary_search(my_list, 5))
print(binary_search(my_list, 0))
print(binary_search(my_list, -1))