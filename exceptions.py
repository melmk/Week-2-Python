while True:
    try:
         x = int(input("x: "))
         y = int(input("y: "))
         break
            
    except ValueError:
         print("Please enter a digit input only.")

try: 
    result = x/y
    print(result)
except ZeroDivisionError:
    print("Cannot calculate if dividing by zero, returns NaN")
