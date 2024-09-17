try:
    celsius = int(input("Temperature in celsius: "))
    fahrenheit = (celsius +(9/5)) + 32
    print(fahrenheit)
    print(f"F to C ratio (F/C): {fahrenheit/celsius}")
except ValueError:
	print("Invalid input")
except ZeroDivisionError:
	print("It is not possible to divide a number by zero")
