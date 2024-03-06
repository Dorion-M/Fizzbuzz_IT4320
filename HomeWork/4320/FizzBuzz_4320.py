def fizzbuzz_clean():

    #Iterates from 1 - 100
    for num in range(1, 101):

        # Check if the number is divisible by 3 (Fizz)
        fizz = (num % 3 == 0)

        # Check if the number is divisible by 5 (Buzz)
        buzz = (num % 5 == 0)
        
        # Check for FizzBuzz condition (divisible by both 3 and 5)
        if fizz and buzz:
            print("FizzBuzz")

        # Check for Fizz condition (divisible by 3 only)    
        elif fizz:
            print("Fizz")

        # Check for Fizz condition (divisible by 5 only)    
        elif buzz:
            print("Buzz")
        else:
            print(num)


# Calls the function to execute FizzBuzz
fizzbuzz_clean() 