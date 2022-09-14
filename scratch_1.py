try:
     for i in range(3):
        print(i)
except IndentationError as e:
   print (e)









try:
   while True:
#input is assigned to a string variable check
       check = input('The input provided by the user is being read which is:')
#the data assigned to the string variable is read
       print('Hello', check)
#EOFError exception is caught and the appropriate message is displayed
except EOFError as x:
       print (x)







a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=a+b
print((c))














i=0
while i>6:
    if (i==3):
        break
    print (i)
    i=i+1




















