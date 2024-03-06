#Print numbers from 1 to 100
#For multiples of 3, replace the number with 'Fizz'
#For multiples of 5, replace the number with 'Buzz'
#For multiples of both, replace the number with 'FizzBuzz'

def fizzbuzz_clean():
    
    for num in range(1, 101):
        fizz = (num % 3 == 0)
        buzz = (num % 5 == 0)
        
        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(num)

fizzbuzz_clean() 