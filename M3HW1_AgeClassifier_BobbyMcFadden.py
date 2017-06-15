#Code for stage of Age.
#6-15-2017
#CTI-110 M3HW1-Age Classifier
#Bobby McFadden

age = int(input('Enter the age of person:'))

if age <= 1:
    print ('You are an infant.')

elif age <= 12:
    print ('You are a child.')

elif age <= 19:
    print ('You are a teenager.')

elif age >= 20:
    print ('You are an adult.')
           
