from typing import List

def merge(left_array: List[int], m: int, right_array: List[int], n: int) -> None:
  # Write code here
  data=[]
  i=0
  j=0
  k=0

  while i < len(left_array) and j < len(right_array):
    if left_array[i] <= right_array[j]:
      data[k] = left_array[i]
      i += 1
    else:
      data[k] = right_array[j]
      j += 1
    k += 1

  while i < len(left_array):
    data[k] = left_array[i]
    i += 1
    k += 1

  while j < len(right_array):
     data[k]=right_array[j]
     j += 1
     k += 1
  return data



# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
nums1 = merge(nums1, m, nums2, n)
print(nums1)
