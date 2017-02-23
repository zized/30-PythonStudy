length = 2
width = 3
print('area is', length * width)


number = 23
guess = 20 #int(raw_input('Enter an integer : '))

if guess == number:
    print('Congratulations, you guessed it.') # New block starts here
    print ("(but you do not win any prizes!)" )# New block ends here
elif guess < number:
    print ('No, it is a little higher than that' )# Another block
    # You can do whatever you want in a block ...
else:
    print ('No, it is a little lower than that') 
    # you must have guess > number to reach here

print ('Done')
# This last statement is always executed, after the if statement is executed 



for i in range(1,5,2):
    print(i)



def sayHello(message, times =1):
    print(message * times)
    
sayHello('hello',5)





def someFunction():
    pass 


print(someFunction(()))

