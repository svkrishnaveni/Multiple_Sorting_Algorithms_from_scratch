from random import randint
import time

def bubble_sort_alg(ls_elements):
    '''
    This function is used to sort the given unsorted ls_elements by using bubble sorting technique
    Inputs: unsorted ls_elements of elements
    Outputs: sorted list of given elements
    '''
    #store program starting time
    start = time.time()
    for i in range(len(ls_elements)-1):
        for j in range(len(ls_elements)-1):
            if(ls_elements[j] > ls_elements[j+1]):
                #swap ls_elements[j] and ls_elements[j+1]
                ls_elements[j], ls_elements[j+1] = ls_elements[j+1],ls_elements[j]
        #print('The elements in ls_elements after iteration '+str(i+1)+' are: '+str(ls_elements))
    #store program ending time
    end = time.time()
    run_time_b = end-start
    print('################################################################ Bubble sort #################################################################')
    print('\nThe time needed to execute Bubble sort with '+str(len(ls_elements))+' elements is :'+str(run_time_b)+' seconds\n')
    print('The sorted ls_elements for given elements by using bubble sort technique is: '+str(ls_elements))
    print()
    return run_time_b

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

# bubble sort
run_time_b = bubble_sort_alg(unsorted_ls_elements)