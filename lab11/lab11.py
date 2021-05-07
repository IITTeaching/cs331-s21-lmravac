from unittest import TestCase
import random

pivots = []

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if low < high:
        p = hoare(lst, low, high, pivot_fn)
        qsort(lst, low, p, pivot_fn)
        qsort(lst, p + 1, high, pivot_fn)
        
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return lst[low]
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return lst[random.randrange(low, high)]
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    numA = lst[low]
    numB = lst[(low + high) // 2]
    numC = lst[high]
    l = [numA, numB, numC]
    minl = min(l)
    maxl = max(l)
    i = 0
    for a in l:
        i += 1
        if a == minl or a == maxl:
            del l[i]
            i -= 1
    return l[0]
    
    ### END SOLUTION
def hoare(lst, low, high, pivot_fn):
    ppos = pivot_fn(lst, low, high)
    pivot = lst[ppos]
    swap(lst, ppos, low) #moving the pivot to the very front so that this partitioning can work if it isnt min pivot
    i = low
    j = high
    while i < j:
        #moving i and j in closer together
        #print("PIVOT: " + str(pivot))
        #print(lst)
        while lst[i] < pivot and i < j:
            i += 1
            #print("i: " + str(i) + " and j: " + str(j))
        while lst[j] > pivot and i < j:
            j -= 1
            #print("i: " + str(i) + " and j: " + str(j))
        swap(lst, i, j) #swap if i is still less than j
    swap(lst, low, j) #move the pivot into its proper position when i >= j
    return j    #return j As per instructions

def swap(lst, i, j):
    temp = lst[i] 
    lst[i] = lst[j]
    lst[j] = temp
################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
