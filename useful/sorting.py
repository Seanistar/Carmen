''' performance
bulit-in >>> quick > heap > merge > insertion > bubble
'''

# to bubble up the largest(or smallest),
# then the 2nd largest and the the 3rd and so on to the end of the list
# Each bubble up takes a full sweep through the list.
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

# taking elements from the unsorted list and inserting them at the right place in a new sorted list.
# The sorted list is empty in the beginning.
# Since the total number of elements in the new and old list stays the same           
def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

# subdividing the the list into two sub-lists,
# sorting them using Merge sort and then merging them back up.
# As the recursive call is made to subdivide each list into a sublist, they will eventually reach the size of 1
def merge_sort(items):
    if len(items) > 1: # base condition
        mid = len(items) / 2
        left, right = items[0:mid], items[mid:]
            
        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        for i in range(len(items)):     # merging the left and right list
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else: ## it needs to handle when exception incurr due to rval or lval is 0
                raise Exception('Could not merge, sub arrays sizes do not match the main array')

# first selecting a pivot element from the list.
# It then creates two lists, one containing elements less than the pivot and the other containing elements higher than the pivot.
# It then sorts the two lists and join them with the pivot in between.
# Just like the Merge sort, when the lists are subdivided to lists of size 1
#
# partition operation: the pivot is in its final position.
# reorder the array so that all elements with values less than the pivot come before the pivot,
# while all elements with values greater than the pivot come after it.
def quick_sort(items):
    if len(items) > 1: # they are considered as already sorted.
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items

# This implementation uses the built in heap data structures in Python.
# To truly understand haepsort, one must implement the heapify() function themselves.
# This is certainly one obvious area of improvement in this implementation
def heap_sort(items):
    import heapq
    
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]
