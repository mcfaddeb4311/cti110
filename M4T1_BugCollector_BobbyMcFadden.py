# Write Program that keeps running total number of bugs. 
# 6-23-2017
# CTI-110 M4T1 - Bug Collector
# Bobby McFadden

total = 0

#Get bugs collected for each day.

for day in range(1, 6) :
    print ('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

#Display the total bugs.

print('You collected a total of', total, 'bugs.')
