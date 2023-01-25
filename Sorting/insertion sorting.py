def sort_k_messed_array(arr, k):
  for i in range(len(arr)):
    for j in range(i,0,-1):
      if arr[j]<arr[j-1]:
        arr[j-1],arr[j] = arr[j],arr[j-1]
      else:
        break
  print(arr)
sort_k_messed_array([9,8,6,7,10],3)


# can also use heap to optimize time 
import heapq
def sort_k_messed_array(arr, k):
  n = len(arr)
  arr = [10,3,1]
  heapq.heapify(arr)
  print(arr)
  for i in range(k + 1, n):
    arr[i - k - 1] = heapq.heappop(minheap)
    heapq.heappush(minheap, arr[i])

  for i in range(k+1):
    arr.append(heapq.heappop(minheap))
  print(arr)