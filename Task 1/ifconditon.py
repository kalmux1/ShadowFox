                                # IF ELSE TASK IN Beginner Level
#-------------------------------------------------------------------------------------------------------------------#

'''
1. Write a program to determine the BMI Category based on user input. Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

def bmi():                                                           # Intializing and Defining the function bmi
    Height = float(input("Enter Your Height in metres : "))          # Taking Height as an input from user 
    Weight = float(input("Enter Your Weight in kilograms : "))       # Taking Weight as an input from user

    BMI = (Weight / (Height * 2))                 # Calculating BMI 

    # Starting the If Else ladder or the Nested If Else 

    if BMI >= 30 :                      # If BMI is 30 or greater, printing "Obesity"           
        print("Obesity")
    elif BMI > 25 and BMI <= 29 :       # If BMI is between 25 and 29, printing "Overweight"
        print("Overweight")
    elif BMI > 18.5 and BMI <= 25 :     # If BMI is between 18.5 and 25, printing "Normal"
        print("Normal")
    elif BMI < 18.5 :                   # If BMI is less than 18.5, printing "Underweight"
        print("Underweight")
    else :
        print ("Wrong Input")           # Wrong Input Handling

bmi()                   # Calling The Main Funtion 

#-----------------------------------------------------------------------------------------------------------------------#   

'''
2. Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi" 
Output: "Abu Dhabi is in UAE"
'''

Australia = ["sydney", "melbourne", "brisbane", "perth"]    #       ---------------------
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]            #       |   Defining List   |
India = ["mumbai", "bangalore", "chennai", "delhi"]         #       ---------------------

city = input("Enter a City Name : ")            # Taking City Name as an input from user 
city_name = city.lower()                        # Coverting that city name in lower case 

# Starting the If Else ladder or the Nested If Else

if city_name in Australia :                     # Checking if the city name comes under the Australia List
    print(f"{city_name} is in Australia")
elif city_name in UAE :                         # Checking if the city name comes under the UAE List
    print(f"{city_name} is in UAE")
elif city_name in India :                       # Checking if the city name comes under the India List
    print (f"{city_name} is in India")
else :
        print ("Wrong Input")           # Wrong Input Handling

#-------------------------------------------------------------------------------------------------------------------------#

'''
3. Write a program to check if two cities belong to the same country. 
Ask the user to enter two cities and print whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''

city1 = input("Enter the first City Name : ")            # Taking Fisrt City Name as an input from user 
city2 = input("Enter the second City Name : ")            # Taking Second City Name as an input from user 
city1_name = city1.lower()                        # Coverting that city name in lower case 
city2_name = city2.lower()                        # Coverting that city name in lower case 

# Starting the If Else ladder or the Nested If Else

if city1_name in Australia and city2_name in Australia :               # Checking if the city names comes under the Australia List
    print("Both cities are in Australia")
elif city1_name in UAE and city2_name in UAE :                         # Checking if the city names comes under the UAE List
    print("Both cities are in UAE")
elif city1_name in India and city2_name in India :                     # Checking if the city names comes under the India List
    print ("Both cities are in India")
else :
    print ("They don't belong to the same country")           # Wrong Input Handling


#-----------------------------------------------------------------------------------------------------------------------------------------#