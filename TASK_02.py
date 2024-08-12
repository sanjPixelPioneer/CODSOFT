#SIMPLE CALCULATOR

#Input two numbers 
number_1 = float(input("Enter the number 1: "))
number_2 = float(input("Enter the number 2: "))

#operation of choice
Type_of_operation = input("Enter the operation required: ")

if Type_of_operation == '+':
    print(number_1 + number_2)
    
elif Type_of_operation == '-':
    print(number_1 - number_2)
    
elif Type_of_operation == '*':
    print(number_1 * number_2)
    
elif Type_of_operation == '/':
    print(number_1 / number_2)
    
elif Type_of_operation == '%':
    print(number_1 % number_2)
    
elif Type_of_operation == '//':
    print(number_1 // number_2)

else:
    print("ERROR!")