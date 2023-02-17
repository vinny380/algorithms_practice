import time
import random

def linear_search(list_target, list_source):
  if len(list_target) == 0:
    print('list_target must have len 1 at least.')
  else:
   for element in list_target:
     if element in list_source:
       print(f'Index: {list_source.index(element)}\t Element: {element}')


def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    pivot = unsorted_list[len(unsorted_list) // 2]
    left = [x for x in unsorted_list if x < pivot]
    middle = [x for x in unsorted_list if x == pivot]
    right = [x for x in unsorted_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


  
def binary_search(list_target, list_source):
    list_source = quick_sort(list_source)
    for i in list_target:
        low = 0
        high = len(list_source) - 1
        while low <= high:
            mid = (low + high) // 2
            if i == list_source[mid]:
                print(f'Index: {list_source.index(i)}\t Element: {i}')
                break
            elif i < list_source[mid]:
                high = mid - 1
            else:
                low = mid + 1

def run_search(k):
  random.seed(12345)
  list_source = random.sample(range(0,1000), k)
  list_target = random.sample(list_source, k=int(len(list_source)/2))

  for i in range(len(list_target)):
    n = random.randint(1001,5000)
    if (n not in list_target) and (n not in list_source):
      list_target.append(n)
    else:
      continue
  start_time_linear = time.time()
  linear_search(list_target, list_source)
  end_time_linear = time.time()

  
  start_time_binary = time.time()
  binary_search(list_target, list_source)
  end_time_binary = time.time()
  print(f'Linear: Search time: {end_time_linear}\t Execution time: {end_time_linear - start_time_linear}\n')
  print(f'Binary: Search time: {end_time_binary}\t Execution time: {end_time_binary - start_time_binary}\n')
  print(f'Binary is faster: {(end_time_linear - start_time_linear) > (end_time_binary - start_time_binary)}')
  print(f'Linear is faster: {(end_time_linear - start_time_linear) < (end_time_binary - start_time_binary)}')


run_search(25)