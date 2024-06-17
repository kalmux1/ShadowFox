# NUMBERS TASK IN Beginner Level

# 1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string.
#    Print the result. Try to identify the representation used.

def formatfunc(num , letter) :          # Intializing the function with the two parameters num & letter
    return format(num,letter)           # Returning formatted value 

print(formatfunc(145,'o'))              # Displaying the final result 

# It is returning 221 as the formatted result 


# 2.  In a village, there is a circular pond with a radius of 84 meters. 
# Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
# Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? 
# Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

pond_radius = 84        # Storing the given radius 
pi = 3.14               # Storing the pi value although we can use math function

pond_area = int((pi * pond_radius * pond_radius))       # Calculating the Total Pond Area
total_water = int((pond_area * 1.4))                    # Calculating the Total Water in it

print(f"The total pond area is {pond_area} and the total water in the pond is {total_water} liters") # Displaying the Fianl result via Fstring

# The Output is "The total pond area is 22155 and the total water in the pond is 31016"