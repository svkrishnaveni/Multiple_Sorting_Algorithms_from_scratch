import time
from random import randint

def Insertion_sort_alg(ls_elements):
    '''
    This function is used to sort the given unsorted ls_elements by using Insertion sorting technique
    Inputs: unsorted ls_elements of elements
    Outputs: sorted list of given elements
    '''
    #store program starting time
    start_i = time.time()
    for i in range(1,len(ls_elements)):
        key = ls_elements[i]
        j = i-1
        while j>=0 and key<ls_elements[j]:
            ls_elements[j+1] = ls_elements[j]
            j = j-1
        ls_elements[j+1] = key
        #print('The elements in ls_elements after iteration '+str(i)+' are: '+str(ls_elements))
    #store program ending time
    end_i = time.time()
    run_time_i = end_i-start_i
    print('################################################################ Insertion sort #################################################################')
    print('\nThe time needed to execute Insertion sort with '+str(len(ls_elements))+' elements is :'+str(run_time_i)+' seconds\n')
    print('The sorted ls_elements for given elements by using Insertion sort technique is: '+str(ls_elements))
    print()
    return run_time_i

def random_list(size,lowest,highest):
    '''
    This function is used to generate random list of elements
    Inputs: size of the list, lowest element in the list, highest element in the list
    Outputs: random list of elements
    '''
    list = []
    #generating random elements
    for _ in range(size):
        value = randint(lowest, highest)
        list.append(value)
    ls_elements = list
    return ls_elements

# Asking input for list size
print('Enter size of the list : ')
size = int(input())

# Asking input for lowest number in the list
print('Enter Lowest number in the list : ')
lowest = int(input())

# Asking input for highest number in the list
print('Enter Highest number in the list : ')
highest = int(input())


unsorted_ls_elements = random_list(size, lowest, highest)

# insertion sort
run_time_i = Insertion_sort_alg(unsorted_ls_elements)
