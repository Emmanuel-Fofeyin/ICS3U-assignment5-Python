#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program of integers and then prints the sum of the even & odd integers


def main():
    # This program calculates the positive an negative integer sum

    # Input
    positive_string = input("Enter an integer >= 0: ")
    negative_string = input ("Enter a integer < 0 ")
    positive_string2 = input("Enter an integer >= 0: ")
    negative_string2 = input ("Enter a integer < 0 ")

    # process
    sum1 = positive_string + positive_string2
    sum2 = negative_string + negative_string2

    # output
    try:
        positive_integer = int(positive_string)
        positive_integer2 = int(positive_string2)
        negative_integer = int(negative_string)
        negative_integer2 = int(negative_string2)
        if positive_integer and positive_integer2 >= 0:
            print("The sum of all positve number =")
            if positive_integer >= 0:
                for loop_counter in range(positive_integer + 1):
                    squared_number = loop_counter * loop_counter
                    print("{0}² = {1}".format(loop_counter, squared_number))
    except ValueError:
        print("This is invalid input.")
    finally:
        print("\nDone.")



if __name__ == "__main__":
    main()
