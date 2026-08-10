def linear_search(arr, key):
    # Step 3: Set i = 0
    i = 0
    n = len(arr)

    # Step 5: Repeat Step 4 until i = n
    while i < n:
        # Step 4: Compare A[i] with key. If equal, display position and stop
        if arr[i] == key:
            print(f"Element found at position (index): {i}")
            return i
        i += 1

    # Step 6: If element is not found after checking all elements
    print("Element not found")
    return -1


# Example Usage
if __name__ == "__main__":
    # Step 2: Read the array A of n elements and the search element key
    A = [10, 50, 30, 70, 80, 20, 90]
    key = 30

    print(f"Array: {A}")
    print(f"Searching for key: {key}")

    linear_search(A, key)

    # Step 7: Stop / Print Enrollment Number at last
    print("Enrollment number:92460118193")
