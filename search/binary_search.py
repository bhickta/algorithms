arr = [1, 3, 3, 4, 5, 6, 7, 8]

# Python implementation of Binary Search
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1

def binary_search_range(low, high):
    while low <= high:
        mid = (low + high) // 2

        # Your condition to determine whether to go left or right
        if is_correct(mid):
            return mid  # Desired condition met
        elif is_left_of_target(mid):
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Desired condition not met

def is_correct(index):
    # Your condition to check if the index is correct
    # Example: return True if the index meets some criteria, else False
    return index == "desired_value"

def is_left_of_target(index):
    # Your condition to check if you need to move left
    # Example: return True if you need to move left, else False
    return index < "desired_value"