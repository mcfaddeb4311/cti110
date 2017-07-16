# Number File Reader
# D7/16/17
# CTI-110 M6HW2 - Random Number File Reader
# Bobby McFadden

import random

randfile = open("Randomnm.txt", "w" )

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(1, 500)) + "\n"
    randfile.write(line)
    print(line)

randfile.close()
