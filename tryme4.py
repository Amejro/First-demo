#pre-defined function by instructor.
def new_line():
    print('.')

#pre-defined function by instructor.
def three_lines():
    new_line()
    new_line()
    new_line()

#Defining a function to print nine lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#This function prints 25 blank lines
def clear_screen():
    nine_lines()
    three_lines()
    new_line()
    nine_lines()
    three_lines()

#calling nine_lines() and clear_screen()
    
print(" Calling nine_lines()...")
nine_lines() #prints nine lines with a perion (.) begining each line

print("Calling clear_Screen()...")
clear_screen() #prints 25 blank lines with a perion begining each line.
