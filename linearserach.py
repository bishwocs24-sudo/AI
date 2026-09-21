

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Main program
n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

