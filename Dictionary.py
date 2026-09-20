# Example 1: Create and access
student = {"name": "Ali", "age": 20, "course": "Python"}
print(student["name"])        
student["age"] = 21           
student["city"] = "Lahore"    
print(student)

# Example 2: Loop through a dictionary
prices = {"apple": 100, "banana": 50, "mango": 150}
for fruit, price in prices.items():
    print(fruit, "costs", price)