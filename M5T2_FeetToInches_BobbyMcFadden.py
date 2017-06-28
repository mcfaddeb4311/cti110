# Function To Convert Feet To Inches
# 6-28-2017
# CTI-110 M5T2_FeetToInches 
# Bobby mcFadden

#Constant for the number of inches per foot. 
INCHES_PER_FOOT = 12

# Main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches
    print (feet, 'equals', feet_to_inches(feet), 'inches.')
    
#The feet_to_inches (feet):
def feet_to_inches (feet):
    return feet * INCHES_PER_FOOT   

#Call the main function.
main()
