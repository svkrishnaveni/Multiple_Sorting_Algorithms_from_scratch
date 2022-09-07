from random import randint
import time

def selection_sort_alg(ls_elements):
    '''
    This function is used to sort the given unsorted ls_elements by using selection sorting technique
    Inputs: unsorted ls_elements of elements
    Outputs: sorted list of given elements
    '''
    #store program starting time
    start = time.time()
    for i in range(len(ls_elements)):
        #initialize min_index with i
        min_index = i
        for j in range(i+1,len(ls_elements)):
            if(ls_elements[j]<ls_elements[min_index]):
                min_index = j
        #swap ls_elements[i] and ls_elements[min_index]
        ls_elements[i], ls_elements[min_index] = ls_elements[min_index],ls_elements[i]
        #print('The elements in ls_elements after iteration '+str(i+1)+' are: '+str(ls_elements))
    #store program ending time
    end = time.time()
    run_time_s = end-start
    print('################################################################ selection sort #################################################################')
    print('\nThe time needed to execute selection sort with '+str(len(ls_elements))+' elements is :'+str(run_time_s)+' seconds\n')
    print('The sorted ls_elements for given elements by using selection sort technique is: '+str(ls_elements))
    print()
    return run_time_s

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

# selection sort
run_time_s = selection_sort_alg(unsorted_ls_elements)