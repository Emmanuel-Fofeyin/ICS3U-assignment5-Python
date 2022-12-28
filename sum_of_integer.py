#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program of integers and then prints the sum of the even & odd integers


def main():
    # This program calculates the positive an negative integer sum

    #  process & output
    repeat = 0
    positive_answer = 0
    negative_answer = 0
    try:
        while repeat < 4:
            repeat = repeat + 1
            input_number = input("Enter an integer: ")
            input_number_int = int(input_number)
            if input_number_int >= 0:
                positive_answer = positive_answer + input_number_int
            if input_number_int < 0:
                negative_answer = negative_answer + input_number_int
        print(
            "\nThe negative sum is {1}, The positive sum is {0}.".format(
                positive_answer, negative_answer
            )
        )
    except ValueError:
        print("\n\nThis is invalid input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
