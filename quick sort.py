

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        # Find pivot position
        pivot_position = partition(arr, low, high)

        # Sort left part
        quick_sort(arr, low, pivot_position - 1)

        # Sort right part
        quick_sort(arr, pivot_position + 1, high)


# Main program
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("Original array:", arr)

quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)

