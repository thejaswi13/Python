"""
Bidirectional Bubble Sort is a variation of the classic Bubble Sort algorithm.
It is a simple sorting algorithm that repeatedly steps through the list of elements, compares adjacent items, and swaps them if they are in the wrong order.
What sets it apart from Bubble Sort is its bidirectional approach, which sorts elements from left to right and then from right to left.
"""
def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(n - 1):
            # Sort from left to right
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        for i in range(n - 1, 0, -1):
            # Sort from right to left
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    bidirectional_bubble_sort(arr)
    print("Sorted array is:", arr)
