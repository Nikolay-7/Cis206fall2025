# CIS 206 – Assignment 2: BMI with Functions (Group)
# Group Members:
# - Amtoj Singh
# - Afshin Kerka
# - Wang K Cheung
# - Nikolay
#
# Simple, readable solution that follows the basics we agreed on:
# - snake_case names
# - small functions that do one job
# - short docstrings + a few practical comments
# - supports Metric (kg/m) and Imperial (lb/in)
#Date: September 7th, 2025
#Description: This program calculates a user's BMI (Body Mass Index).
#It converts the users weight in pounds and height in feet/inches.
#Into metric units, then calculates BMI, and then displays the result along with
#Standard BMI ranges from the CDC.


#Constants
#PEP 8 standard: (ALL CAPS for constants makes them easy to spot and understand what they do)
LBS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254
INCHES_IN_FOOT = 12

#Function names use snake_case (PEP 8 standard for readability)
def get_user_input():
    #Gets weight and height input from the user.
    #Standard applied: variables are in snake_case and descriptive.
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height in feet: "))
    height_inches = float(input("Enter additional inches in height: "))
    return weight_pounds, height_feet, height_inches

 #Function uses snake_case and returns a value (abiding by the PEP 8 standard) 
def convert_weight_to_kg(weight_pounds):
    #Converts weight from pounds to kilograms.
    return weight_pounds * LBS_TO_KG

 #Function applies same naming rule and always returns a value
def convert_height_to_meters(height_feet, height_inches):
    #Converts height from feet and inches to meters.   
    total_inches = height_feet * INCHES_IN_FOOT + height_inches
    #Returns Height in meters
    return total_inches * INCHES_TO_METERS

    #Function yet again follows naming rule and returns the value
def calculate_bmi(weight_kg, height_meters):
    #calculates and returns bmi using formula (BMI = weight in kilograms / (height in meters)**2)
    return weight_kg / (height_meters ** 2)

    #function follows naming standard 
def display_results(bmi_value):
    #Displays BMI results and  ranges
    round_bmi = round(bmi_value,1)
    print()
    print("Your BMI:", round_bmi)
    print()
    print("BMI Ranges:")
    print("Underweight: Less than 18.5")
    print("Normal: 18.5 to less than 25")
    print("Overweight: 25 to less than 30")
    print("Obese: 30 or greater")
    print()
    print("Source: CDC (Centers for Disease Control and Prevention)")
    print("https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html")


def main():
    #Gets user input
    weight_pounds, height_feet, height_inches = get_user_input()
    # Convert units
    weight_kg = convert_weight_to_kg(weight_pounds)
    height_meters = convert_height_to_meters(height_feet, height_inches)
    #Calculates BMI
    bmi_value = calculate_bmi(weight_kg, height_meters)
    #Bmi results
    display_results(bmi_value)

   
main()
#Runs functions/whole BMI calculator


