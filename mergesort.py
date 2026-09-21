
# Merge Sort

def merge(arr, low, mid, high):

    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    # Compare elements of left and right arrays
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements from left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):

    if low < high:

        mid = (low + high) // 2

        # Sort left half
        merge_sort(arr, low, mid)

        # Sort right half
        merge_sort(arr, mid + 1, high)

        # Merge both halves
        merge(arr, low, mid, high)


# Main program
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("Original array:", arr)

merge_sort(arr, 0, n - 1)

print("Sorted array:", arr)

