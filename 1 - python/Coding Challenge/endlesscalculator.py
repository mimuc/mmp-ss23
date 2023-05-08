start_number = int(input("What is your first number?"))

working_number = start_number

while True:
    next_action = input("What do you want to do next?")
    input_split = next_action.split(" ")

    action = input_split[0]
    number = int(input_split[1])

    if action == "add":
        working_number = working_number + number
    elif action == "subtract":
        working_number = working_number - number
    else:
        print("calculation method "+input_split[0]+" is unknown")

    print("Your result is "+str(working_number))

