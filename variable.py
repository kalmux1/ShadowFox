

# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = 22/7
print(type (pi))

# It's returninng float as the datatype 


# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.

for = 4   # Kindly Comment out this line for executing rest of the code !
    
# It will throw an error as the "for" is a reserved keyword used for creating loops. As such, it cannot be used as a variable name.


# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100

p_amt = 3000   # Principal Amount 
roi = 7        # Rate Of Intrest
time = 3       # Time

si = ((p_amt * roi * time) / 100)  # Simple Intrest ((Principal Amount * Rate Of Intrest * Time )/ 100)
print (si)

# The calculated Simple Intrest is 630.0 