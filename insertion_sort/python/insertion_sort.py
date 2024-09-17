import random

#creating a unsorted list of integers, 100 items long


numbers = [ random.randint(0,10000) for i in range(1, 101)]

#function to insertion sort

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key
    return numbers

insertion_sort(numbers)
print(numbers)