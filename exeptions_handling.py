# Exception Handling

def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as zerodv:
        print("you can't devide by zero")
        print("Error: ",zerodv)
    except(NameError, TypeError):
        print("pls check your input")
    finally:
        print("finally block is executed")


division(45,15)
division(45,0)
division(45,10)
division(45,"hello")
division(100,15)


file_name = 'data/inputData.txt'

with open(file_name) as input_data:
    contents = input_data.read()
    print(contents)

