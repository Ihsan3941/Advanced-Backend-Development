# Example 1: Sets remove duplicates
nums = {1, 2, 2, 3, 3, 3}
print(nums)                   
nums.add(4)
nums.discard(1)
print(nums)                   

# Example 2: Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)                  
print(a & b)                  
print(a - b)               