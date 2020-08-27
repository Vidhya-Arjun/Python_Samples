Intializer = 0 # Intializer is a counter helps to denote the starting point
while(Intializer==0):  # Condition to start the program
   
    Minimum = int(input("Enter the Minimum value for prime number generation: "))
    Maximum = int(input("Enter the Maximum value for prime number generation: "))

    if (Maximum > Minimum):  # Checking Minimum is less than Maximum value
        Intializer += 1
        for Number in range(Minimum,Maximum):  # Intializing for loop between the ranges
            count = 0
            for i in range(2,Number//2 + 1): #  When a number gets divided with in any of the number of half of its range it is a composite number
                if(Number%i ==0):
                    count += 1
                    break
            if(count==0 and Number!= 1): # Condition to check whether the number is prime or not
                print(Number) # prints the prime number
    else:   
        print("Minimum value is greater than value, Please enter Minimum value less than Maximum value")
