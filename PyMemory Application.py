# ================================================= Program to convert a number system to another and add them ====================================================== #

""" This is a program which helps you to convert a value from one number of system to another using string formatting and
    other methods like converting a number into integer with different base (16,8,2). This program aims at converting
    values from Decimal, Hexadecimal, Octal, binary and Engineering notation to Decimal, Hexadecimal, Octal, binary and
    Engineering notation. So,
        Total chances in set A = {1,2,3,4,5} = 5
        Total chances in set B = {1,2,3,4,5} = 5
        So, total chances in Relations : 5*5 = 25
    So, There are 50 Ways to Convert in PyMemory Convertor.

    This is a program which helps you to perform basic arithmetic operations on any number system using string formatting
    and other methods like converting a number into integer with different base (16,8,2) and using in-built arithmetic
    operators in python . This program aims at performing arithmetic operation with values in Decimal, Hexadecimal, Octal,
    binary and Engineering notation. This program also gives you the Decimal equivalent thus providing hands-free access
    to PyMemory Convertor also. So,
        Total chances in set A = {1,2,3,4,5} = 5
        Total chances in set B = {+,-,*,/} = 4
        So, total chances in Relations : 5*4 = 20
        So, total decimal equivalences : 4*4 = 16
    So, There are 36 Ways to perform arithmetic operations in PyMemory Calculator. """

# ========================================================= Defining the Convertor function =========================================================================== #

def PyMemory_Conv():
    # Try-exception method for the whole function
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
                print("Please enter only decimal numbers as you have chosen the base value to be in decimal number system")
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
                print("Please enter only hexadecimal numbers as you have chosen the base value to be in hexadecimal number system")
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
                    print("You have entered Octal - Engineering notation conversion")
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
                print("Please enter only binary numbers as you have chosen the base value to be in binary number system")
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
                print("Please enter only in Engineering notation as you have chosen the base value to be in Engineering notation")
                print("Please don't enter space between numbers and operations")
                print("Engineering notation Example: 4.7000e+10")
                print("Please rerun the program")
        else:
            print("Please enter a proper combination for base value")
            print("Please only enter 1,2,3 or 4")
            print("Please rerun the program")

    except:
        pass

# ========================================================= END of defining the Convertor function ==================================================================== #

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

def PyMemory_Calc():
    print("Select number system of the numbers")
    print("1. Decimal \n"
          "2. Hexadecimal \n"
          "3. Octal \n"
          "4. Binary \n"
          "5. Engineering notation")

    # Selecting the base number system
    num_sys = int(input("Enter choice(1/2/3/4/5): "))

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # If the base number system is Decimal, so chances are:

    if num_sys == 1:

        try:

            # Selecting the operation:
            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                num1 = int(num1)
                num2 = int(num2)

                if choice == '1':
                    print(num1, "+", num2, "=", (num1 + num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", (num1 - num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", (num1 * num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", (num1 / num2))

            else:
                print("Invalid Input")

        except:
            print("Please only enter 1,2,3 or 4")
            print("Please rerun the program")

    # If the base number system is Decimal, so chances are:
    elif num_sys == 2:

        try:

            # Selecting the operation:
            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                num1 = int(num1, 16)
                num2 = int(num2, 16)

                if choice == '1':
                    print("Hexadecimal addition: ", "%X + %X = %X" % (num1, num2, num1 + num2))
                    print("Decimal equivalent: ", num1, "+", num2, "=", (num1 + num2))

                elif choice == '2':
                    print("Hexadecimal addition: ", "%X - %X = %X" % (num1, num2, num1 - num2))
                    print("Decimal equivalent: ", num1, "-", num2, "=", (num1 - num2))

                elif choice == '3':
                    print("Hexadecimal addition: ", "%X * %X = %X" % (num1, num2, num1 * num2))
                    print("Decimal equivalent: ", num1, "*", num2, "=", (num1 * num2))

                elif choice == '4':
                    print("Hexadecimal addition: ", "%X / %X = %X" % (num1, num2, num1 / num2))
                    print("Decimal equivalent: ", num1, "/", num2, "=", (num1 / num2))

            else:
                print("Invalid Input")

        except:
            print("Please only enter 1,2,3 or 4")
            print("Please rerun the program")

    # If the base number system is Decimal, so chances are:
    elif num_sys == 3:

        while True:

            # Selecting the operation:
            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                num1 = int(num1, 8)
                num2 = int(num2, 8)

                if choice == '1':
                    print("Octal addition: ", "%o + %o = %o" % (num1, num2, num1 + num2))
                    print("Decimal equivalent: ", num1, "+", num2, "=", (num1 + num2))

                elif choice == '2':
                    print("Octal addition: ", "%o - %o = %o" % (num1, num2, num1 - num2))
                    print("Decimal equivalent: ", num1, "-", num2, "=", (num1 - num2))

                elif choice == '3':
                    print("Octal addition: ", "%o * %o = %o" % (num1, num2, num1 * num2))
                    print("Decimal equivalent: ", num1, "*", num2, "=", (num1 * num2))

                elif choice == '4':
                    print("Octal addition: ", "%o / %o = %o" % (num1, num2, num1 / num2))
                    print("Decimal equivalent: ", num1, "/", num2, "=", (num1 / num2))
                break

            else:
                print("Invalid Input")

    # If the base number system is Decimal, so chances are:
    elif num_sys == 4:

        while True:

            # Selecting the operation:
            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                num1 = int(num1, 2)
                num2 = int(num2, 2)
                num1_new, num2_new = bin(num1), bin(num2)
                num1_str, num2_str = str(num1_new), str(num2_new)
                num1_fin, num2_fin = num1_str[2:], num2_str[2:]

                if choice == '1':
                    num3 = num1 + num2
                    num3 = bin(num3)
                    num3_str = str(num3)
                    num3 = num3_str[2:]
                    print("Binary addition: ", "%s + %s = %s" % (num1_fin, num2_fin, num3))
                    print("Decimal equivalent: ", num1, "+", num2, "=", (num1 + num2))

                elif choice == '2':
                    num3 = num1 - num2
                    num3 = bin(num3)
                    num3_str = str(num3)
                    num3 = num3_str[2:]
                    print("Binary addition: ", "%s - %s = %s" % (num1_fin, num2_fin, num3))
                    print("Decimal equivalent: ", num1, "-", num2, "=", (num1 - num2))

                elif choice == '3':
                    num3 = num1 * num2
                    num3 = bin(num3)
                    num3_str = str(num3)
                    num3 = num3_str[2:]
                    print("Binary addition: ", "%s 8 %s = %s" % (num1_fin, num2_fin, num3))
                    print("Decimal equivalent: ", num1, "*", num2, "=", (num1 * num2))

                elif choice == '4':
                    num3 = num1 / num2
                    num3 = bin(int(num3))
                    num3_str = str(num3)
                    num3 = num3_str[2:]
                    print("Binary addition: ", "%s / %s = %s" % (num1_fin, num2_fin, num3))
                    print("Decimal equivalent: ", num1, "/", num2, "=", (num1 / num2))

                break

            else:
                print("Invalid Input")

    # If the base number system is Decimal, so chances are:
    elif num_sys == 5:

        while True:

            # Selecting the operation:
            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Engineering notation addition: ", "%e + %e = %e" % (num1, num2, num1 + num2))
                    print("Decimal equivalent: ", num1, "+", num2, "=", (num1 + num2))

                elif choice == '2':
                    print("Engineering notation addition: ", "%e - %e = %e" % (num1, num2, num1 - num2))
                    print("Decimal equivalent: ", num1, "-", num2, "=", (num1 - num2))

                elif choice == '3':
                    print("Engineering notation addition: ", "%e * %e = %e" % (num1, num2, num1 * num2))
                    print("Decimal equivalent: ", num1, "*", num2, "=", (num1 * num2))

                elif choice == '4':
                    print("Engineering notation addition: ", "%e / %e = %e" % (num1, num2, num1 / num2))
                    print("Decimal equivalent: ", num1, "/", num2, "=", (num1 / num2))

                break

            else:
                print("Invalid Input")

    # If the base number system is supported:
    else:
        print("Wrong combination entered!!!")
        print("Please only enter 1,2,3 or 4")
        print("Please rerun the program")


# ============================================================ Defining the initialisation function ======================================================================== #

def PyMemory_init():
    main_q = int(input("Do you want to convert numbers or perform arithmetic operations on them \n"
                       "1. Converter (click 1) \n"
                       "2. Calculator (click 2) \n"
                       "click 0 to quit the program \n"
                       " : "))
    if main_q == 1:
        PyMemory_Conv()
    elif main_q == 2:
        PyMemory_Calc()
    elif main_q == 0:
        Proj_Credits()
        quit()

# ========================================================= END of defining the Process function ==================================================================== #

# ============================================================ Defining the Mainloop ======================================================================== #

def PyMemory_mainloop():

    # Initialising the program
    PyMemory_init()

    # Asking the user's consent to continue the application
    cont = input("Do you want to continue? (Use Y for yes and N for no): ")

    # Looping process
    while cont == "Y":
        PyMemory_init()
        cont = input("Do you want to continue? (Use Y for yes and N for no): ")

    # Credits
    Proj_Credits()

# ========================================================= END of defining the Mainloop ==================================================================== #

# ============================================================ The main program ======================================================================== #

PyMemory_mainloop()

# ==================================================== Termination of program ---------- THE END ! ============================================================
