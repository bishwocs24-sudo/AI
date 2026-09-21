
# Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is already sorted
        if not swapped:
            break


# Main program
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)

