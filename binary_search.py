def binary_search(array:list,target:int):
   start = 0
   end = len(array) - 1
   while start <= end:
      mid = start + end // 2
      if target < array[mid]:
         end = mid - 1
      elif target > array[mid]:
         start = mid + 1
      else :
         return mid
   return -1
    
