def first_exercise():
    input = "123"
    converted = int(input)
    print(converted * 3)

def second_exercise():
    input = "123.2"
    converted = float(input)
    print(converted * 3.2)

def third_exercise():
    str_obj = "Hello"
    int_obj = 123
    print(str_obj + str(int_obj))

def fourth_exercise():
    first_input = input("1st input: ")
    second_input = input("1st input: ")
    print("The product of " + first_input + " and " + second_input + " is " + str(int(first_input) * int(second_input)))

first_exercise()
second_exercise()
third_exercise()
fourth_exercise()