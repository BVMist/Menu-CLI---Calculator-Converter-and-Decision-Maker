#Menu-Calculator, Converter, Decision Maker cli



#Calculator function
def calc(a, b, op):
    """
    Takes in three values and performs arithmetic operation on it, returning the answer. 
    The first two being the numbers to be computed, the last being the operand."""
    
    match op:
        case '+':
            return 'Ans: ' + str(a+b)
        case '-':
            return 'Ans: ' + str(a-b)
        case '/':
            if b==0:
                return "Cannot divide by zero."
            else:
                return 'Ans: ' + str(a/b)
        case '*':
            return 'Ans' + str(a*b)
            

#Converter function
def conv(a, unit_a, unit_b):
    '''
    Takes in the value and the unit to convert from as well as the unit to convert to, then returns the converted value. '''
    
    conv_table = {'s': {'min':1/60, 'hr':1/3600}, 'min': {'s':60, 'hr':1/60}, 'hr': {'s':3600, 'min': 60}}
    return a*(conv_table[unit_a][unit_b])

                        
            
#Decision maker function    
def dec(arg):
    """
    A function that takes in an age value then decides whether it corresponds to being a child, preteen, teen or an adult. Then prints its conclusion.
    """
    if arg>=0 and arg<=10:
            print("Child")
    elif 10<arg<13:
            print("Preteen")      
    elif arg>=13 and arg<20:
            print("Teen")    
    elif arg>=20:
            print("Adult")                              
    else:
            print("Invalid age, must not be less than 0.")





#Main Loop
while True:
    print("\n==========Menu========")
    print("1. Calculator")
    print("2. Converter")
    print("3. Decision maker")
    print("4. Exit")
    
    
    while True:
        try:
            action = int(input("Please enter the number corresponding to the action you'd like to perform: "))
            break
        except:
            print("Must be a number.")
            continue            

    
    if action not in [1,2,3,4]:
        print("Must be either 1, 2, 3 or 4")
        continue
        
    #Calculator        
    elif action == 1:
        print("\n--------Calculator--------")
        print("Operations: +, -, *, / or exit to exit")   
        while True:
            op = input("Operation: ").strip().lower()
            if op not in ['+', '-', '*', '/', 'exit']:
                print("Invalid operation")
                continue
            elif op in ['+','-','*','/']:
                #Validating the first number
                while True:
                    try:
                        a = int(input("First number: "))
                        break
                    except:
                        print("Must be a number.")
                #Validating the second number ensuring it's an integer.                   
                while True:
                    try:
                        b = int(input("Second number: "))           
                        break
                    except:
                         print("Must be a number.")  
                #Output                         
                print(calc(a, b, op))                                                   
            else:
                break     
        
                    
   
                                                             
    #Converter                                                        
    elif action == 2:
            print("\n----------Converter------------")
            units = ['s', 'min', 'hr']
            print(f"Conversion available, from {', '.join(units)} to {', '.join(units)}.")
            
            #Converter main loop
            while True:
                #Getting user action to proceed or exit.
                while True:
                    try:
                        action = int(input("What would you like to do? Type 1 to convert and 2 to exit: "))
                        if action not in [1,2 ]:
                            print("Invalid operation")
                            continue
                        else:
                            break
                    except:
                        print("Must be an integer.")
                    
                if action == 1:
                    #Getting the unit to convert from and verifying it.
                    while True:
                        unit_from = input(f"Please input the starting unit: ").lower().strip()
                        if unit_from not in units:
                            print(f"Can only convert from s, min or hr.")
                        else:
                            break
            
                    #Getting the unit to convert to and validating it.            
                    while True:
                        unit_to = input(f"Please input the unit to convert to: ").lower().strip()
                        if unit_to not in units:
                            print("Can only convert to s, min or hr.")
                        else:
                            break

                    #Getting the value to be converted and validating it.                    
                    while True:
                        try:
                            value = float(input("The value to convert: "))
                            break
                        except:
                            print("Must be a number")
                    print(f"Old value: {value}{unit_from}")                  
                    print(f"New value: {conv(value, unit_from, unit_to)}{unit_to}")
                    
                else:
                    break
     
      
        
    #Decision Maker                                          
    elif action == 3:
            print("\n-----------Decision Maker--------")
            while True:
                    age = input("Age(or exit to exit): ")
                    if age.lower().strip()=='exit':
                        break
                    else:
                        #Validating the age input ensuring its a number.
                        while True:
                            try:
                                age = int(age)
                                break
                            except:
                                print("Must be a number.")   
                       #Display the conclusion.         
                        dec(age)                                    
                        
                        
#Exit                        
    elif action == 4:
        print("Exiting...")
        break                                           