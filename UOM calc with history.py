def add (a,b):
   return a+b 

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def division (a,b):
  if (b==0):
    print("Float division by zero")
  else:
    return a/b

def power (a,b):
    return a**b

def remainder (a,b):
    return a%b

calc_history = []
def record_history(calculations):
    calc_history.append(calculations)

def history():
    if calc_history == []:
        print("No past calculations")
    else:
        for i in calc_history:
            print(i)

def select_op(choice):
      if (choice == '#'):
        return -1
      elif (choice == '$'):
        return 0
      elif choice in ('+' , '-' , '*' , '**' , '/' , '%'):

        while (True):
          num1 = str(input("Enter first number: "))
          print (num1)
          if num1.endswith('#'):
            return -1
          if num1.endswith('$'):  
            return 0

          try:
            one = float(num1)
            break
          except ValueError:
            print("Not a valid number, please enter again")  
            continue

        while (True):
          num2 = str(input("Enter second number: "))
          print (num2)
          if num2.endswith('#'):
           return -1
          if num2.endswith('$'):  
           return 0

          try:
            two = float(num2)
            break
          except ValueError:
            print("Not a valid number, please enter again")  
            continue      
      
      
      
        result = 0.0
        last_calculation = ""
        if choice == '+':
          result = add(one,two)
        elif choice == '-':
          result = subtract(one,two)
        elif choice == '*':
          result = multiply(one,two)
        elif choice == '**':
          result = power(one,two)
        elif choice == '/':
          result = devide(one,two)
        elif choice == '%':
          result = remainder(one,two)

        else:
          print("Something went wrong")  
          
        last_calculation = "{0} {1} {2} = {3}".format(one, choice, two, result)
        print(last_calculation)
        record_history(last_calculation)

      elif choice == '?':
        history()    

      else:
        print("Unrecognized operation")


while (True):
     print("Select operation. ")
     print ("1.Add :+")
     print ("2.Subtract :-")
     print ("3.Multiply :*")
     print ("4.Power :**")
     print ("5.Division :/")
     print ("6.Remainder :%")
     print("7.Terminate: # ")
     print("8.Reset    : $ ")
     print("9.History  : ? ")

     choice = input ("Enetr choice (+, -, *, **, /, %) : ")
     print(choice)

     result = select_op(choice)
     if (result == -1):
      print("Done. Terminating")
      exit()
     



