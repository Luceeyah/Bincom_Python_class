import os
import re


with open(r"baby2008.html","r") as baby_file:
    read_baby_file = baby_file.read()
    # if search for <td></td>
    res = re.findall(r'<td>[A-Z]?[a-z]+</td>',read_baby_file)

baby_names = []
for i in res:
    baby_names.append(i[4: len(i) - 5])

print(baby_names)

# print individual names
for i in baby_names:
    print(i)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

bubble_sort(baby_names)

def binary_search(lst, x):
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] < x:
            lo = mid + 1
        elif lst[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

name_to_find = "Alice"
index = binary_search(baby_names, name_to_find)
if index >= 0:
    print(f"{name_to_find} found at index {index}")
else:
    print(f"{name_to_find} not found")
    
    
    
