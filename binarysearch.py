def binary_search(arr, key):
    # Step 3: Initialize low = 0 and high = n - 1
    low = 0
    high = len(arr) - 1

    # Step 6: Repeat Steps 4–5 until low > high
    while low <= high:
        # Step 4: Find the middle element
        mid = (low + high) // 2

        # Step 5: Compare A[mid] with key
        if arr[mid] == key:
            print(f"Element found at position (index): {mid}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    # Step 6: If the element is not found
    print("Element not found")
    return -1


# Example Usage
if __name__ == "__main__":
    # Step 2: Read the sorted array A of n elements and the search element key
    A = [10, 20, 30, 50, 70, 80, 90]  # Array must be sorted
    key = 70

    print(f"Sorted Array: {A}")
    print(f"Searching for key: {key}")

    binary_search(A, key)

    # Step 7: Stop / Print Enrollment Number at last
    print("Enrollment number:92460118193")
