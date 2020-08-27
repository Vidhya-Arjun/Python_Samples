Intializer = 0
while(Intializer==0):  
    Minimum = int(input("Enter the Minimum value for prime number generation: "))
    Maximum = int(input("Enter the Maximum value for prime number generation: "))
    Divident = int(input("Enter the non-zero divident"))

    if (Maximum > Minimum): 
        Intializer += 1
        for Number in range(Minimum,Maximum):
                if(Number% Divident ==0):
                    print(Number)   
    else:   
        print("Minimum value is greater than value, Please enter Minimum value less than Maximum value")
