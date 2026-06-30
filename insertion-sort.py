# divide sequence into two sublists
# 1. sorted - length of 1
# 2. unsorted
# compare val to immediate left and change positions

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            # check left item and make sure not to go into negative indexing
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i] # swap
            i = i - 1 # look at next item

    return list_a

def main():
    user_input = input("Please enter an array with a space between each number:\n")
    user_arr = user_input.split(" ")
    
    print("Sorting...\n")
    result = insertion_sort(user_arr)
    print(f"Sorted: {result}")

    # check if array conversion worked
    # print(f"You entered: {user_arr}")

if __name__ == "__main__":
    main()