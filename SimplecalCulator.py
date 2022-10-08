
#program of Simple Calculator (Using Fucntions)

#Prgram Code Created by Shivsagar Mishra

#created functions
def addition(a,b):
       print('Addition is ',a+b)
def substraction(a,b):
       print('Subtraction is ',a-b)
def multiplication(a,b):
       print('Multiplication ',a*b)
def dividation(a,b):
       print('dividation is ',a/b)

while True:
   print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit')
   c= int(input('Enter your choice: '))
   #Exit Operation
   if(c==5):
      print(quit)
      print("Exiting....")
      quit()

   else:
      #Taking input from User
      a=int(input("Enter First Number:"))
      b=int(input("Enter Second Numebr:"))
      
      #Performing Calculations
      if c==1:
         addition(a,b)
      elif c==2:
         substraction(a,b)
      elif c==3:
         multiplication(a,b)
      elif c==4:
         dividation(a,b)
      else:
         print("Enter Valid Choice !")
      
      #For Continue
      cont=int(input("Do you want to continue? 1.yes\t 2.no:"))
      if cont==1:
         continue
      elif cont==2:
         break
      else:
         print("Please Enter a Valid choice Between 1 or 2")


'''
output

1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
Enter your choice: 3
Enter First Number:34
Enter Second Numebr:23
Multiplication  782
Do you want to continue? 1.yes   2.no:2

'''
         
