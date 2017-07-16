# Random Number
# 7/16/2017
# CTI-110 M6HW1 - Random Number File Writer
# Bobby McFadden

import random

def main():
        more = 'y'

        while more.lower() == 'y':

                random_numbers = open('Unit 4 numbers.txt', 'w')
                NumtoBeWr = random.randint(1, 20)
                print(NumtoBeWr, 'numbers added to output file: ')

                for count in range(NumtoBeWr):
                      number = random.randint(1, 500)
                      print(number)
                      random_numbers.write(str(number) + '\n')

                random_numbers.close()

                random_numbers = open('Unit 4 numbers.txt', 'r')


                # This the code to read the file

                line = random_numbers.readline()
                number = 0
                total = 0

                while line != " ":
                        number = int(line)

                        line = line.rstrip('\n')
                        print(number)
                        total = total + int(line)
                        number = number + number
                        line = random_numbers.readline()

                        print("The total of the numbers: "+ str (total))
                        print("Total count of numbers read from file: "+ str (number))
                        more = input("Do you want to run again to write and read more numbers. (Y/N): ")
                random_numbers.close()

        print("Thank for using this program")


main()
