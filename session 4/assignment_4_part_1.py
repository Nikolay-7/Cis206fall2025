#CIS 206 Assignment 4: BMI with conditions


#Constants
LBS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254
INCHES_IN_FOOT = 12

def get_user_input():
    #Gets weight and height input from the user.
    #Activity 1: Allows user to type 'q' to quit. 
    #Activity 1: Keeps asking until valid input is entered.
    while True:
        try:
            weight_input = input("Enter your weight in pounds (or 'q' to quit): ")
            if weight_input.lower() == "q":
                return None, None, None
            weight_pounds = float(weight_input)

            height_input = input("Enter your height in feet (or 'q' to quit): ")
            if height_input.lower() == "q":
                return None, None, None
            height_feet = int(height_input)

            inches_input = input("Enter additional inches in height (or 'q' to quit): ")
            if inches_input.lower() == "q":
                return None, None, None
            height_inches = float(inches_input)

    #Range and constraint validation
            if not (4 <= weight_pounds <= 1400):
                print("Weight must be between 4 and 1400 pounds.")
                continue
            if not (1 <= height_feet <= 8):
                print("Height in feet must be between 1 and 8.")
                continue
            if not (0 <= height_inches < 12):
                print("Inches in height must be between 0 and 11.99.")
                continue

            return weight_pounds, height_feet, height_inches

        except ValueError:
            print("Error: Input must be a number.")

def convert_weight_to_kg(weight_pounds):
    #Converts weight from pounds to kilograms
    #parameter validation validates weight range
    if not (1 <= weight_pounds <= 1400):
        raise ValueError("Weight must be between 1 and 1400 pounds.")
    return weight_pounds * LBS_TO_KG

def convert_height_to_meters(height_feet, height_inches):
    #Converts height from feet and inches to meters
    #parameter validation that checks functions arguments 
    if not (1 <= height_feet <= 8):
        raise ValueError("Height in feet must be between 1 and 8.")
    if not (0 <= height_inches < 12):
        raise ValueError("Inches must be between 0 and 11.99.")
    total_inches = height_feet * INCHES_IN_FOOT + height_inches
    return total_inches * INCHES_TO_METERS

def calculate_bmi(weight_kg, height_meters):
    #Calculates BMI with a parameter validation.
    if weight_kg <= 0 or height_meters <= 0:
        raise ValueError("Weight and height must be positive.")
    return weight_kg / (height_meters ** 2)

def display_results(bmi_value):
    #Displays BMI results with a assertion checks.
    #Confirms BMI output is a number and positive
    assert isinstance(bmi_value, (int, float)), "BMI must be a number"
    assert bmi_value > 0, "BMI must be positive"
    round_bmi = round(bmi_value, 1)
    print()
    print("Your BMI:", round_bmi)
    print()
    print("BMI Ranges:")
    if round_bmi < 18.5:
        print("Underweight: Less than 18.5")
    elif round_bmi < 25:
        print("Normal: 18.5 to less than 25")
    elif round_bmi < 30:
        print("Overweight: 25 to less than 30")
    else:
        print("Obese: 30 or greater")
    print()
    print("Source: CDC (Centers for Disease Control and Prevention)")
    print("https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html")

def main():
    #Main with exception handling.
    #checks that errors and reports are caught
    weight_pounds, height_feet, height_inches = get_user_input()
    if weight_pounds is None:  #user quit
        print("Program terminated by user.")
        return
    try:
        weight_kg = convert_weight_to_kg(weight_pounds)
        height_meters = convert_height_to_meters(height_feet, height_inches)
        bmi_value = calculate_bmi(weight_kg, height_meters)
        display_results(bmi_value)
    except (ValueError, AssertionError) as e:
        print("Error:", e)

main()
#Runs functions/whole BMI calculator



