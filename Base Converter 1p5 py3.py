from tkinter import *

# To augment this program's ability to accept different bases, modify this dictionary with the values of the characters you wish to represent the corresponding decimal numbers.
number_lookup = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 18,
    "J" : 19,
    "K" : 20,
    "L" : 21,
    "M" : 22,
    "N" : 23,
    "O" : 24,
    "P" : 25,
    "Q" : 26,
    "R" : 27,
    "S" : 28,
    "T" : 29,
    "U" : 30,
    "V" : 31,
    "W" : 32,
    "X" : 33,
    "Y" : 34,
    "Z" : 35,
    "10" : "A",
    "11" : "B",
    "12" : "C",
    "13" : "D",
    "14" : "E",
    "15" : "F",
    "16" : "G",
    "17" : "H",
    "18" : "I",
    "19" : "J",
    "20" : "K",
    "21" : "L",
    "22" : "M",
    "23" : "N",
    "24" : "O",
    "25" : "P",
    "26" : "Q",
    "27" : "R",
    "28" : "S",
    "29" : "T",
    "30" : "U",
    "31" : "V",
    "32" : "W",
    "33" : "X",
    "34" : "Y",
    "35" : "Z",
    }

decimal_numbers = ["0","1","2","3","4","5","6","7","8","9"]

# Initialize the global variables
number = ""
originalbase = 0
newbase = 0

def convert_to_base10(number,base):
    if base > 35: raise ValueError("This converter currently only supports conversion from bases less than 35.")
    for i in number:
        if i == "-" or i == ".":
            raise ValueError("This converter does not support negative number conversion, or floating point operations.")
    digit_list = str(number)
    # Count variable simply represents the power of 10 to multiply by.
    count = 0
    total = 0
    # Iterate backwards over "number", so that we progressively add digits from right to left. This allows us to accept a number of unknown length.
    for n in digit_list[::-1]:
        total += (number_lookup[n] * (base ** count))
        count += 1
    return total

def convert_to_base(number,originalbase,newbase):
    if originalbase > 35 or newbase > 35: raise ValueError("This converter currently only supports conversion in bases less than 35.")
    print("The old number to be converted is: %s and it is currently in base %d. It will be converted into base %d."%(number, originalbase, newbase))
    old_number = convert_to_base10(number,originalbase)
    # Initialize all the variables we need.
    # New_number serves only as a placeholder iterable that we can parse through at the end.
    new_number = []
    final_number = ""
    exp_counter = 0
    digit = 0
    # The following two variables are not explicitly necessary, but are potentially interesting mathematically. Can be added to output later.
    highest_digit = 0
    number_of_digits = 0
    # Find the highest value that the given base with x number of digits can hold. We will iterate over this initialization, continually finding the highest value that
    # the number of arbitrary length can hold. With this information, we will find the highest digit required to store the number in the new base.
    max_value = (newbase ** exp_counter)
    while old_number > max_value:
        exp_counter += 1
        max_value += (newbase ** exp_counter)
    # Next line, number_of_digits is not necessary, as we have that information in exp_counter (hence, simply +1), but I will keep it in as a nicety.
        number_of_digits = exp_counter + 1
    # For each digit in the new base, we will take out the largest possible value of the previous number.
    # Using floor division (in other words, truncation), we will find that value.
    # For example, 244(base10)  // 128(base2, 2^7) = 1. We will then place that digit in the rightmost column using .append() method.
    # Continuing example, the result will be stored in old_number. -> (244 - 128 = 116). We will continue to subtract this way until exp_counter is exhausted, and we are out of possible digits.
    while exp_counter > -1:
        digit = (old_number // (newbase ** exp_counter))
        digit = str(digit)
        # Test to avoid inadvertently add a preceeding zero at the beginning of the string. Number of digits variable ends up helping here.
        if digit == "0" and (exp_counter == number_of_digits - 1):
            exp_counter -= 1
        else:
            # Because we will sometimes be calculating digit as decimal representation instead of alpha, we need to perform our subtraction slightly differently.
            if digit not in decimal_numbers:
                new_number.append(number_lookup[digit])
                old_number = (old_number - (int(digit) * (newbase ** exp_counter)))
                exp_counter -= 1
                continue
            # If the result of the division is zero, we can skip the subtraction step.
            if digit == "0":
                new_number.append(number_lookup[digit])
                exp_counter -= 1
            else:
                new_number.append(number_lookup[digit])
                old_number = (old_number - (number_lookup[digit] * (newbase ** exp_counter)))
                exp_counter -= 1
    # Iterate over the list new_number, and concatenate them into the final number.
    for i in new_number:
        final_number = final_number + str(i)
    # Finally, return final_number as a string.
    return final_number


#############
# Function below takes a given number, in a given base, and converts it to a new base of user specification.
#############

def on_Click_Calculate_New_Number():
    # I overuse the variable name number in this program.
    # First, we gather user input, and see if it is valid (In other words, are the fields completed?)
    number = origNumEntry.get()
    if number == "":
        resultant_num.set("Please complete all relevant fields.")
        return
    # Ensure the user hasn't input lower case letters, decimal points, or negative signs.
    for i in number:
        if i not in number_lookup:
            resultant_num.set("Value error: Please follow the correct syntax for entry.")
            return
    # Same thing below, just testing to see if somebody clicked the button mindlessly.
    if origBaseEntry.get() == "":
        resultant_num.set("Please complete all relevant fields.")
        return
    # Test to see if the base they wish to convert from is within our ability
    # May make these values global variables in future version, and add larger base conversion support with it.
    if int(origBaseEntry.get()) > 35 or int(origBaseEntry.get()) < 2:
        resultant_num.set("Value error. Cannot calculate a base outside range 2-35.")
        return
    # Test if there are invalid characters in the original base entry form
    if isinstance(origBaseEntry.get(), int) == False:
        resultant_num.set("Value error: Please follow the correct syntax for entry.")
    # If the input is valid, set it as an integer
    originalbase = int(origBaseEntry.get())
    # Test for empty field
    if newBEntry.get() == "":
        resultant_num.set("Please complete all relevant fields.")
        return
    # Test for base conversion outside supported range
    if int(newBEntry.get()) > 35 or int(newBEntry.get()) < 2:
        resultant_num.set("Value error. Cannot calculate a base outside range 2-35.")
        return
    # Test for invalid input
    if isinstance(newBEntry.get(), int) == False:
        resultant_num.set("Value error: Please follow the correct syntax for entry.")
    newbase = int(newBEntry.get())
    # Finally, perform the conversion to the new base, and set up the output label to reflect the result.
    resultantConvertedNumber = convert_to_base(number,originalbase,newbase)
    resultant_num.set("The converted number is " + resultantConvertedNumber)
    resultant_num_copypasta_Var.set(resultantConvertedNumber)
    return

#############
# Function below takes a given number, in a given base, and a number of equivalent value in an unknown base, and solves for the unknown base value.
#############

def on_Click_Calculate_Unknown_Base():
    testNumVal = 0
    convArbitraryToBase10 = 0
    base10 = 10
    # Set up the known number string
    number = knownArbitraryBaseNumber.get()
    # Test for blank field
    if number == "":
        unknownBaseResult.set("Please complete all relevant fields.")
        return
    # Test for illegal values in the field, return error message.
    for i in number:
        if i not in number_lookup:
            unknownBaseResult.set("Value error: Please follow the correct syntax for entry.")
            return
    # Test for base range outside our ability to solve
    if int(knownArbitraryBase.get()) > 35 or int(knownArbitraryBase.get()) < 2:
        unknownBaseResult.set("Value error. Cannot calculate a base outside range 2-35.")
        return
    # Test for illegal values in the field with a different method, we can only accept integers in this form.
    if isinstance(knownArbitraryBase.get(), int) == False:
        resultant_num.set("Value error: Please follow the correct syntax for entry.")
    # When form value is confirmed to be valid, set originalArbitraryBase
    originalArbitraryBase = int(knownArbitraryBase.get())
    # Below, we convert the original number in the original base to base 10 to make the function a bit smoother
    convArbitraryToBase10 = convert_to_base(number,originalArbitraryBase,base10)
    # Grab the new number with an equivalent value to that which we just calculated the base 10 representation for
    unknownBaseNum = unknownBaseNumber.get()
    # Test for blank user input
    if unknownBaseNum == "":
        unknownBaseResult.set("Please complete all relevant fields.")
        return
    # Loop and convert the base 10 value of our original number to every other base successively.
    #  If we find a match between this, and the unknown base value, return the function, and update the output label.
    # Same thought here, in future versions, the range will likely draw its value from a global variable.
    for base in range(2,36):
        testNumVal = convert_to_base(convArbitraryToBase10,base10,base)
        if testNumVal == unknownBaseNum:
            unknownBaseResult.set("The base is: " + str(base))
            unknownBaseResultCopyPastaVar.set(str(base))
            return
        else:
            continue
    # If we are unsuccessful at finding a matching value in the supported base range, there is no solution to the problem. Update output label to reflect this.
    unknownBaseResult.set("There was no solution found for the numbers provided.")
    return

app = Tk()
app.title("Base Converter v1.5, Darren Paetz 2018")
app.geometry("615x450")
#Set up the GUI for base conversion
origNumberLabel = Label(app, text="Original Number:").grid(row=1,column=0)
origNumEntry = StringVar()
originalNumberEntry = Entry(app, textvariable=origNumEntry, width=60).grid(row=1,column=1)

origBaseLabel = Label(app, text="Original Base:").grid(row=2,column=0)
origBaseEntry = StringVar()
originalBaseEntry = Entry(app, textvariable=origBaseEntry, width=60).grid(row=2,column=1)

newBaseLabel = Label(app, text="Base to convert to:").grid(row=3,column=0)
newBEntry = StringVar()
newBaseEntry = Entry(app, textvariable=newBEntry, width=60).grid(row=3,column=1)

calculate_button1 = Button(app, text="Convert",width=51,command=on_Click_Calculate_New_Number).grid(row=4,column=1)

resultant_num_copypasta_Var = StringVar()
resultant_num_copypasta = Entry(app,textvariable=resultant_num_copypasta_Var,width=20).grid(row=6,column=0)

resultant_num = StringVar()
resultant_num.set("The result of the conversion will display here, and be able to be copied on the left.")
resultant_number_label = Label(app,textvariable=resultant_num,height = 5).grid(row=6,column=1)

# Set up the GUI for unknown base solving
knownArbitraryBaseNumberLabel = Label(app, text="Known Number Value:").grid(row=7,column=0)
knownArbitraryBaseNumber = StringVar()
knownArbitraryBaseNumberEntry = Entry(app, textvariable=knownArbitraryBaseNumber, width=60).grid(row=7,column=1)

knownArbitraryBaseLabel = Label(app, text="Known Number's Base:").grid(row=8,column=0)
knownArbitraryBase = StringVar()
knownArbitraryBaseEntry = Entry(app, textvariable=knownArbitraryBase,width=60).grid(row=8,column=1)

unknownBaseNumberLabel = Label(app, text="Number in unknown base:").grid(row=9,column=0)
unknownBaseNumber = StringVar()
unknownBaseNumberEntry = Entry(app, textvariable=unknownBaseNumber,width=60).grid(row=9,column=1)

calculate_button2 = Button(app,text="Solve for unknown base",width=51,command=on_Click_Calculate_Unknown_Base).grid(row=10,column=1)

unknownBaseResultCopyPastaVar = StringVar()
unknownBaseResultCopyPasta = Entry(app,textvariable=unknownBaseResultCopyPastaVar,width=20).grid(row=12,column=0)

unknownBaseResult = StringVar()
unknownBaseResult.set("The value of the unknown base will display here, and be able to be copied on the left.")
unknownBaseResultLabel = Label(app, textvariable=unknownBaseResult,height=5).grid(row=12,column=1)

# Gui setup for input rules
syntaxGuideTitleLabel = Label(app, text="Syntax rules:").grid(row=14,column=0)
syntaxGuideLabel = Label(app, text="All numbers greater than base 10 must use capital letters for digit representation").grid(row=14,column=1)
syntaxGuideCont1 = Label(app, text="(I.E. Base 16 will be represented as '1FFA' for decimal 8186.)").grid(row=15,column=1)
syntaxGuideCont2 = Label(app, text="Note this converter has no ability to convert floating point or negative numbers.").grid(row=16,column=1)

# Start the event handler
mainloop()
