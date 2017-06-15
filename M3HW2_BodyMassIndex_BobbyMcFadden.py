#Calculation of BMI
#6-15-2017
#CTI-110 M3HW2- Body Mass Index
#Bobby McFadden

weight= float(input("Enter the weight:"))

height= float(input("Enter the height:"))

bmi= ( weight * 703) / ( height ** 2)

if bmi < 18.5:
    print ("A person with a bmi of " + format(bmi, ".2f") + " is underweight.")

elif bmi < 26 :
    print ("A person with a bmi of "  + format(bmi, ".2f") + " is optimal.")
   

else:
    print ( "A person with a bmi of " + format(bmi, ".2f") + " is overweight.")

    
            

