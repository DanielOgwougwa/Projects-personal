# Libaries  
import os
import time 
import datetime

# Diet Plan Project - Daniel Ogwougwa:
# Conversion Notes:
#   1 lb = 0.453592 kg
#   1 in = 2.54 cm 

# Activity Factor:
#   No exercise = 1.2 
#   3-5 days per week = 1.55
#   6-7 days per week = 1.725

# Global Variables that will need to be accessed in different fucntions
male = int(+5);  
female = int(-161);
current_time = datetime.datetime.now()
maintenance = float;

def calorie_calculator():
    print()
    print("This calculator will now work out how many calories you should be consuming per day")
    time.sleep(2)
    print("The details that you have uploaded are: ")
    time.sleep(2)
    print("Weight: " + (str(user_weight)) + " kg")
    time.sleep(1)
    print("Height: " + (str(user_height)) + " cm")
    time.sleep(1)
    print("Age: " + (str(user_age)) + " years old")
    print() # Empty Line 
    time.sleep(1)
    user_gender = input("Are you male or female? Please enter 'male' or 'female': ")
    gender_factor = int()
    if user_gender == 'male': # If male is entered, the gender factor will be set to male which is +5
       gender_factor = male 
    elif user_gender == 'female': # If female is entered, the gemder factor will be set to female which is -161
       gender_factor = female 
    print() # Empty Line 
    time.sleep(1)
    print("How often do you exercise per week: ")
    time.sleep(1)
    print("1: No exercise")
    print("2: 3-5 days per week")
    print("3: 6-7 days per week")
    user_activity = input("Please choose an option: ")
    activity_factor = float() 
    if user_activity == '1':
       activity_factor = 1.2
    elif user_activity == '2':
       activity_factor = 1.55 
    elif user_activity == '3':
       activity_factor = 1.725
    print()
    print("Your calorie maintenance is based on your weight, height and age")
    time.sleep(2)
    print("Based on the details you have entered, your calorie maintenance is: ")
    maintenance = (10 * user_weight) + (6.25 * user_height) - (5 * user_age) + (gender_factor) * activity_factor
    print(maintenance)

def user_profile(): # Store users profile details: Weight, Height, Age, Activity Level
    global user_weight
    global user_height 
    global user_age
    os.system('cls')
    print("User Profile: ")
    user_weightinput = input("Please enter your weight in kilograms: ") # Input is requested and stored 
    user_weight = int(user_weightinput)
    user_heightinput = input("Please enter your height in cm: ") # Input is requested and stored 
    user_height = int(user_heightinput)
    user_ageinput = input("Please enter your age: ") # Input is requested and stored
    user_age = int(user_ageinput)
    time.sleep(2)
    print("Your details have now been saved!")

def main_menu(): # Main menu of program. User will enter option
    print(current_time.strftime("%d-%m-%Y %H:%M:%S")) # Outputs the current date and time 
    print() # Empty Line 
    print("Welcome to the Diet Plan Program! ")
    print() # Empty Line 
    print() # Empty Line
    time.sleep(2)
    print("You will first have to upload your details")
    time.sleep(2)
    print("After uploading your details the program will work out your calorie maintenance! ")
    time.sleep(3)
    print() # Empty Line 
    print("Loading.....")
    time.sleep(3)

main_menu()
user_profile()
calorie_calculator()
