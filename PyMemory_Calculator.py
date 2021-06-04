# ================================================= Program to convert a number system to another =================================================================== #

""" This is a program which helps you to convert a value from one number of system to another using string formatting and
    other methods like converting a number into integer with different base (16,8,2). This program aims at converting
    values from Decimal, Hexadecimal, Octal, binary and Engineering notation to Decimal, Hexadecimal, Octal, binary and
    Engineering notation. So,
        Total chances in set A = {1,2,3,4,5} = 5
        Total chances in set B = {1,2,3,4,5} = 5
        So, total chances in Relations : 5*5 = 25
    So, There are 25 Ways to Convert in PyMemory Application. PyMemory will soon be integrated with TLA (The Lezends App)  """


# ========================================================= Defining the program function =========================================================================== #

def PyMemory():
    # Try-exception method for the wholeprogram
    # noinspection PyBroadException
    try:

        # Try-exception block for conversion selection
        try:

            # Base value number system
            inp = int(input("Select the base from which you need to convert \n"
                            "1. Decimal (click 1) \n"
                            "2. Hexadecimal (click 2) \n"
                            "3. Octal (click 3) \n"
                            "4. Binary (click 4) \n"
                            "5. Engineering notation (click 5)"
                            " : "))

            # Converted value number system
            inp1 = int(input("Select the sytem to which you need to convert \n"
                             "1. Decimal (click 1) \n"
                             "2. Hexadecimal (click 2) \n"
                             "3. Octal (click 3) \n"
                             "4. Binary (click 4) \n"
                             "5. Engineering notation (click 5) \n"
                             " : "))

        except ValueError:
            print("INVALID INPUT!!!")
            print("Please only enter 1,2,3,4 or 5")
            print("Please rerun the program")

        # If base is Decimal:
        if inp == 1:

            # Try-exception block for combination mis-selection (Decimal chances)
            try:

                # If base is Decimal, so chances are:
                if inp == 1 and inp1 == 1:
                    print("You have entered Decimal - Decimal conversion")
                    print("The same number will be displayed")
                    number = int(input("Enter the base value: "))
                    print("The converted value is %d" % number)
                    print("Please re-run the program if this was mistakenly selected")
                elif inp == 1 and inp1 == 2:
                    print("You have entered Decimal - Hexadecimal conversion")
                    number = int(input("Enter the base value: "))
                    print("The converted value is %X" % number)
                elif inp == 1 and inp1 == 3:
                    print("You have entered Decimal - Octal conversion")
                    number = int(input("Enter the base value: "))
                    print("The converted value is %o" % number)
                elif inp == 1 and inp1 == 4:
                    print("You have entered Decimal - Binary conversion")
                    number = int(input("Enter the base value: "))
                    binary_value = bin(number)
                    string = str(binary_value)
                    fin_string = string[2:]
                    print("The converted value is %s" % fin_string)
                elif inp == 1 and inp1 == 5:
                    print("You have entered Decimal - Engineering notation conversion")
                    number = int(input("Enter the base value: "))
                    print("The converted value is %e" % number)
                else:
                    print("Wrong combination of conversion entered!!!")
                    print("Please only enter 1,2,3 or 4")
                    print("Please rerun the program")

            except ValueError:
                print(
                    "Please enter only decimal numbers as you have chosen the base value to be in decimal number system")
                print("The values in decimal system are 0,1,2,3,4,5,6,7,8,9")
                print("Please rerun the program")

        # If base is Hexadecimal:
        elif inp == 2:

            # Try-exception block for combination mis-selection (Hexadecimal chances)
            try:

                # If base is Hexadecimal, so chances are:
                if inp == 2 and inp1 == 1:
                    print("You have entered Hexadecimal - Decimal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 16)
                    print("The converted value is %d" % number)
                elif inp == 2 and inp1 == 2:
                    print("You have entered Hexadecimal - Hexadecimal conversion")
                    print("The same number will be displayed")
                    number = input("Enter the base value: ")
                    number = int(number, 16)
                    print("The converted value is %X" % number)
                    print("Please re-run the program if this was mistakenly selected")
                elif inp == 2 and inp1 == 3:
                    print("You have entered Hexadecimal - Octal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 16)
                    print("The converted value is %o" % number)
                elif inp == 2 and inp1 == 4:
                    print("You have entered Hexadecimal - binary conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 16)
                    binary_value = bin(number)
                    string = str(binary_value)
                    fin_string = string[2:]
                    print("The converted value is %s" % fin_string)
                elif inp == 2 and inp1 == 5:
                    print("You have entered Hexadecimal - Engineering notation conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 16)
                    print("The converted value is %e" % number)
                else:
                    print("Wrong combination of conversion entered!!!")
                    print("Please only enter 1,2,3 or 4")
                    print("Please rerun the program")

            except ValueError:
                print(
                    "Please enter only hexadecimal numbers as you have chosen the base value to be in hexadecimal number system")
                print("The values in hexadecimal system are 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F")
                print("Please rerun the program")

        # If base is Octal:
        elif inp == 3:

            # Try-exception block for combination mis-selection (Octal chances)
            try:

                # If base is Octal, so chances are:
                if inp == 3 and inp1 == 1:
                    print("You have entered Octal - Decimal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 8)
                    print("The converted value is %d" % number)
                elif inp == 3 and inp1 == 2:
                    print("You have entered Octal - Hexadecimal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 8)
                    print("The converted value is %X" % number)
                elif inp == 3 and inp1 == 3:
                    print("You have entered Octal - Octal conversion")
                    print("The same number will be displayed")
                    number = input("Enter the base value: ")
                    number = int(number, 8)
                    print("The converted value is %o" % number)
                    print("Please re-run the program if this was mistakenly selected")
                elif inp == 3 and inp1 == 4:
                    print("You have entered Octal - binary conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 8)
                    binary_value = bin(number)
                    string = str(binary_value)
                    fin_string = string[2:]
                    print("The converted value is %s" % fin_string)
                elif inp == 3 and inp1 == 5:
                    print("You have enteredOctal - Engineering notation conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 8)
                    print("The converted value is %e" % number)
                else:
                    print("Wrong combination of conversion entered!!!")
                    print("Please only enter 1,2,3 or 4")
                    print("Please rerun the program")

            except ValueError:
                print("Please enter only octal numbers as you have chosen the base value to be in octal number system")
                print("The values in octal system are 0,1,2,3,4,5,6,7")
                print("Please rerun the program")

        # If base is binary:
        elif inp == 4:

            # Try-exception block for combination mis-selection (binary chances)
            try:

                # If base is binary, so chances are:
                if inp == 4 and inp1 == 1:
                    print("You have entered binary - Decimal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 2)
                    print("The converted value is %d" % number)
                elif inp == 4 and inp1 == 2:
                    print("You have entered binary - Hexadecimal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 2)
                    print("The converted value is %X" % number)
                elif inp == 4 and inp1 == 3:
                    print("You have entered binary - Octal conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 2)
                    print("The converted value is %o" % number)
                elif inp == 4 and inp1 == 4:
                    print("You have entered binary - binary conversion")
                    print("The same number will be displayed")
                    number = input("Enter the base value: ")
                    number = int(number, 2)
                    binary_value = bin(number)
                    string = str(binary_value)
                    print("The converted value is %s" % string)
                elif inp == 4 and inp1 == 5:
                    print("You have entered binary - Engineering notation conversion")
                    number = input("Enter the base value: ")
                    number = int(number, 2)
                    print("The converted value is %e" % number)
                else:
                    print("Wrong combination for conversion entered!!!")
                    print("Please only enter 1,2,3 or 4")
                    print("Please rerun the program")

            except ValueError:
                print(
                    "Please enter only binary numbers as you have chosen the base value to be in binary number system")
                print("The values in binary system are 0,1")
                print("Please rerun the program")

        # If base is Engineering notation:
        elif inp == 5:

            # Try-exception block for combination mis-selection (Engineering notation chances)
            try:

                # If base is Engineering notation, so chances are:
                if inp == 5 and inp1 == 1:
                    print("You have entered Engineering notation - Decimal conversion")
                    number = input("Enter the base value: ")
                    number = float(number)
                    print("The converted value is %d" % number)
                elif inp == 5 and inp1 == 2:
                    print("You have entered Engineering notation - Hexadecimal conversion")
                    number = input("Enter the base value: ")
                    number = float(number)
                    number = int(number)
                    print("The converted value is %X" % number)
                elif inp == 5 and inp1 == 3:
                    print("You have entered Engineering notation - Octal conversion")
                    number = input("Enter the base value: ")
                    number = float(number)
                    number = int(number)
                    print("The converted value is %o" % number)
                elif inp == 5 and inp1 == 4:
                    print("You have entered Engineering notation - binary conversion")
                    number = input("Enter the base value: ")
                    number = float(number)
                    number = int(number, 2)
                    binary_value = bin(number)
                    string = str(binary_value)
                    print("The converted value is %s" % string)
                elif inp == 5 and inp1 == 5:
                    print("You have entered Engineering notation - Engineering notation conversion")
                    print("The same number will be displayed")
                    number = input("Enter the base value: ")
                    number = float(number)
                    print("The converted value is %e" % number)
                    print("Please re-run the program if this was mistakenly selected")
                else:
                    print("Wrong combination of conversion entered!!!")
                    print("Please only enter 1,2,3 or 4")
                    print("Please rerun the program")

            except ValueError:
                print(
                    "Please enter only in Engineering notation as you have chosen the base value to be in Engineering notation")
                print("Please don't enter space between numbers and operations")
                print("Engineering notation Example: 4.7000e+10")
                print("Please rerun the program")
        else:
            print("Please enter a proper combination for base value")
            print("Please only enter 1,2,3 or 4")
            print("Please rerun the program")

    except:
        pass


# ========================================================= END of defining the program function ==================================================================== #


# ============================================================ Defining the Credits function ======================================================================== #

def Proj_Credits():
    print("Thank you for using PyMemory Calculator - your trustable converter")
    print("Copyrights 2020. All rights reserved - Studies Overloaded")
    print("PyMemory is brought to you by Studies Overloaded - A product of the franchise CM and AK Enterprises")
    print("Other apps are available at www.studiesoverloaded.com")
    print("Mail at studiesoverloaded@gmail.com")
    print("Created by Chandramouli.M")
    print("PROGRAM TERMINATED")


# ========================================================= END of defining the Credits function ==================================================================== #


# ============================================================ Defining the Process function ======================================================================== #

def PyMemory_Process():
    PyMemory()
    cont = input("Do you want to continue? (Use Y for yes and N for no): ")
    while cont == "Y":
        PyMemory()
        cont = input("Do you want to continue? (Use Y for yes and N for no): ")
    Proj_Credits()


# ========================================================= END of defining the Process function ==================================================================== #

PyMemory_Process()

# ====================================================== Termination of program ---------- THE END ! ================================================================ #
