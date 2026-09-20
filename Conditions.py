num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")             

age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# Example 1: Grading system
marks = 82
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")         
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C or below")

# Example 2: Traffic light
light = "yellow"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")       
else:
    print("Go")



# Example 1: Multiple conditions with and
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive")

# Example 2: Using or / not
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
if not day == "Monday":
    print("Not Monday!")