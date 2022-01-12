"""This program has the Matrix Application and can generate passwords for the use."""
import hashlib
import uuid
import re
import numpy as np


def menu():
    """This function displays the menu"""
    print("\n1. Use the Matrix Application.")
    print("2. Create 10 passwords.")
    print("3. Exit the program.")

    choice = int(input("What is your Selection?: "))
    return int(choice)


def matrix_application():
    """This function will allow the user to use the Matrix Application"""
    print("*****************Welcome to the Python Matrix Application*****************")
    while True:
        print("Do you want to play the Matrix Game?")

        # Reading the choice
        choice = input("Enter Y for yes or N for No:")
        if choice == "N":
            print("*****************Thanks for playing Python Numpy*****************")
        else:
            while True:
                phone = input("Enter your phone number(XXX-XXX-XXXX):")

                # Regular expression for checking the phone number format
                if not re.match("\\d{3}-\\d{3}-\\d{4}", phone):
                    print("Your phone number is not in correct format. Please re-enter:")
                else:
                    break

            while True:
                zip_code = input("Enter your zip code+4(XXXXX-XXXX):")

                # Regular expression for checking the zipcode format
                if not re.match("\\d{5}-\\d{4}", zip_code):
                    print("Your zip code is not in correct format. Please re-enter:")

                else:
                    break

            # Reading the first matrix
            print("Enter your first 3x3 matrix:")

            # Create list a
            a_list = []
            for i in range(3):
                # Reading row by row
                row = input().split()

                # Converting each element to integer
                row = list(map(int, row))

                # Adding row to the matrix
                a_list.append(row)

            # Print first matrix
            print("Your first 3x3 matrix is:")
            for i in range(3):
                for j in range(3):
                    print(a_list[i][j], end=" ")
                print()

            # Read second matrix
            print("Enter your second 3x3 matrix:")

            # create list b
            b_list = []

            for i in range(3):

                # Reading row by row
                row = input().split()

                # Converting each element to integer
                row = list(map(int, row))

                # Adding row to the matrix
                b_list.append(row)

            # Printing second matrix
            print("Your second 3x3 matrix is:")
            for i in range(3):
                for j in range(3):
                    print(a_list[i][j], end=" ")
                print()

            # Menu for Matrix Operation
            print("Select a Matrix Operation from the list below:")
            print("a. Addition")
            print("b. Subtraction")
            print("c. Matrix Multiplication")
            print("d. Element by element multiplication")
            m_ops = input()

            if m_ops == "a":
                print("You selected Addition. The results are:")

                # converting list to numpy arrays
                a_list = np.array(a_list)
                b_list = np.array(b_list)

                # addition of matrices
                c_list = a_list + b_list

                for i in range(3):
                    for j in range(3):
                        print(c_list[i][j], end=" ")
                    print()
                print("\nThe Transpose is:")

                # function for finding the transpose
                transpose_variable = np.transpose(c_list)
                for i in range(3):
                    for j in range(3):
                        print(transpose_variable[i][j], end=" ")
                    print()
                print("\nThe row and column mean values of the results are:")

                # Function mean with axis =1 finds row means
                print("Row:", np.mean(c_list, axis=1))

                # Function mean with axis =0 finds column means
                print("Column:", np.mean(c_list, axis=0))

            if m_ops == "b":
                print("You selected Subtraction. The results are:")
                a_list = np.array(a_list)
                b_list = np.array(b_list)

                # subtraction of matrices
                c_list = a_list - b_list
                for i in range(3):
                    for j in range(3):
                        print(c_list[i][j], end=" ")
                    print()
                print("\nThe Transpose is:")

                # function for finding the transpose
                transpose_variable = np.transpose(c_list)
                for i in range(3):
                    for j in range(3):
                        print(transpose_variable[i][j], end=" ")
                    print()
                print("\nThe row and column mean values of the results are:")

                # Function mean with axis =1 finds row means
                print("Row:", np.mean(c_list, axis=1))

                # Function mean with axis =0 finds column means
                print("Column:", np.mean(c_list, axis=0))

            if m_ops == "c":
                print("You selected Matrix Multiplication. The results are:")

                # get matrix multiplication using matrix function
                c_list = np.matmul(a_list, b_list)
                c_list = np.array(c_list)

                for i in range(3):
                    for j in range(3):
                        print(c_list[i][j], end=" ")
                    print()
                print("\nThe Transpose is:")

                # function for finding the transpose
                transpose_variable = np.transpose(c_list)
                for i in range(3):
                    for j in range(3):
                        print(transpose_variable[i][j], end=" ")
                    print()
                print("\nThe row and column mean values of the results are:")

                # Function mean with axis = 1 finds row means
                print("Row:", np.mean(c_list, axis=1))

                # Function mean with axis = 0 finds column means
                print("Column:", np.mean(c_list, axis=0))

            if m_ops == "d":
                print("You selected Element by element multiplication. The results are:")
                a_list = np.array(a_list)
                b_list = np.array(b_list)

                # multiply and print
                c_list = a_list * b_list
                for i in range(3):
                    for j in range(3):
                        print(c_list[i][j], end=" ")
                    print()

                # Transpose view
                print("\nThe Transpose is:")
                transpose_variable = np.transpose(c_list)

                for i in range(3):
                    for j in range(3):
                        print(transpose_variable[i][j], end=" ")
                    print()

                # Function mean with axis = 1 finds row means
                print("\nThe row and column mean values of the results are:")
                print("Row:", np.mean(c_list, axis=1))

                # Function mean with axis = 0 finds column means
                print("Column:", np.mean(c_list, axis=0))


def create_password():
    """This function creates passwords base on users input."""
    # input a message to encode
    print('Enter a message to encode:')
    message = input()
    # encode it to bytes using UTF-8 encoding
    message = message.encode()

    # hash with MD5
    print('\n' + hashlib.md5(message).hexdigest())

    # hash with sha256
    print('\n' + hashlib.sha256(message).hexdigest())

    # hash with sha512
    print('\n' + hashlib.sha512(message).hexdigest())

    # Auto generate salt using Universal Unique Identifier library
    salt = uuid.uuid4().hex
    # encode it to bytes using UTF-8 encoding
    salt = salt.encode()

    print('\n', "Your salt is: ", salt)

    # salt and hash with MD5
    print('\n' + hashlib.md5(message + salt).hexdigest())

    # salt and hash with sha256
    print('\n' + hashlib.sha256(message + salt).hexdigest())

    # salt and hash with sha512
    print('\n' + hashlib.sha512(message + salt).hexdigest())

    # salt and hash with MD5
    print('\n' + hashlib.md5(salt + message).hexdigest())

    # salt and hash with sha256
    print('\n' + hashlib.sha256(salt + message).hexdigest())

    # salt and hash with sha512
    print('\n' + hashlib.sha512(salt + message).hexdigest())

    # salt front and back then hash with sha512
    print('\n' + hashlib.sha512(salt + message + salt).hexdigest())


while True:
    SELECTION = menu()

    # Selection 1 to use the Matrix Application
    if SELECTION == 1:
        matrix_application()

    # Selection 2 to create ten passwords from user input
    elif SELECTION == 2:
        create_password()

    # Selection 3 to exit
    elif SELECTION == 3:
        print("\nGoodbye.")
        break

    # Else give error and allow re-entry
    else:
        print("Not a valid entry!\n Please Enter a valid Entry\n")
