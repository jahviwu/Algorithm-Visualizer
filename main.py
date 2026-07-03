from Algorithms.bubble_sort import bubble_sort
from Algorithms.selection_sort import selection_sort
from Algorithms.heap_sort import heap_sort
from visualizer import run_visualizer

def main():
    arr = [5, 3, 8, 4, 2, 9, 1, 6]

    print("Choose an algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Heap Sort")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        _, steps = bubble_sort(arr.copy())
    elif choice == "2":
        _, steps = selection_sort(arr.copy())
    elif choice == "3":
        _, steps = heap_sort(arr.copy())
    else:
        print("Invalid choice.")
        return

    run_visualizer(steps)

if __name__ == "__main__":
    main()
