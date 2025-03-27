# !/usr/bin/env python3
# Created by:Angel
# Created on: March 27,2025
# This program uses a try statement.


def main():
    # this function uses a try statement

    # get the number from user
    integer_as_string = input("Enter an integer: ")
    print("")

    #
    try:
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly")
    except Exception:
        print("This was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
