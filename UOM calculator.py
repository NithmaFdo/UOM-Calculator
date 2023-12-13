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
      
        if choice == '+':
          print (add(one,two))
        elif choice == '-':
          print (subtract(one,two))
        elif choice == '*':
          print (multiply(one,two))
        elif choice == '**':
          print (power(one,two))
        elif choice == '/':
          print (devide(one,two))
        elif choice == '%':
          print (remainder(one,two))

        else:
          print("Something went wrong")  

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

     choice = input ("Enetr choice (+, -, *, **, /, %) : ")
     print(choice)

     result = select_op(choice)
     if (result == -1):
      print("Done. Terminating")
      exit()
     



