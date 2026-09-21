
# Heap Sort

def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):

        # Move current largest to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify(arr, i, 0)


# Main program
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("Original array:", arr)

heap_sort(arr)

print("Sorted array:", arr)

