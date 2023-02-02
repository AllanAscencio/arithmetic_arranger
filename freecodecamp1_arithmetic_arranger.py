print("Welcome to the Arithmetic Arranger, if you need the solution to your math problem don't forget to add the parameter 'tof=True' as the second argument")
user_inp = input("Enter your addition or subtraction math here separating each maths problem by a coma, for example: '20 + 500, 138 - 69': ")


def arithmetic_arranger(problems, tof=False):
    math_list = problems.split(", ")
    # Check if there are more than 5 problems
    if len(math_list) > 5:
        raise "Error: Too many problems."
    else:
        for math_problem in math_list:
            # Check if there are multiplication operators
            if "*" in math_problem:
                print("Error: Operator must be '+' or '-'.")
                break
            # Check if there are division operators
            elif "/" in math_problem:
                print("Error: Operator must be '+' or '-'.")
                break
            else:
                if not tof:
                    top_formatted = []
                    try:
                        if "+" in math_problem:
                            subs_list = math_problem.split(" + ")
                            # Check if there are only digits
                            if subs_list[0].isdigit() and subs_list[1].isdigit():
                                # Check if each operation has more than 4 digits
                                if len(subs_list[0]) > 4 or len(subs_list[1]) > 4:
                                    print("Error: Numbers cannot be more than four digits.")
                                    break
                                else:
                                    top_formatted.append(f"{subs_list[0]:>5}\n+{subs_list[1]:>4}\n-----\n")
                            else:
                                print("Error: Numbers must only contain digits.")
                                break

                        elif "-" in math_problem:
                            subs_list = math_problem.split(" - ")
                            # Check if there are only digits
                            if subs_list[0].isdigit() and subs_list[1].isdigit():
                                # Check if each operation has more than 4 digits
                                if len(subs_list[0]) > 4 or len(subs_list[1]) > 4:
                                    print("Error: Numbers cannot be more than four digits.")
                                    break
                                else:
                                    top_formatted.append(f"{subs_list[0]:>5}\n-{subs_list[1]:>4}\n-----\n")
                            else:
                                print("Error: Numbers must only contain digits.")
                                break

                    finally:
                        print(*top_formatted)

                if tof:  # include a for loop for len of formatted items
                    top_formatted = []
                    if "+" in math_problem:
                        subs_list = math_problem.split(" + ")
                        # Check if there are only digits
                        if subs_list[0].isdigit() and subs_list[1].isdigit():
                            # Check if each operation has more than 4 digits
                            if len(subs_list[0]) > 4 or len(subs_list[1]) > 4:
                                print("Error: Numbers cannot be more than four digits.")
                                break
                            else:
                                # Store formatted items in formatted_list
                                top_formatted.append(f"{subs_list[0]:>5}\n+{subs_list[1]:>4}\n-----\n")
                        # Addition
                        total = int(subs_list[0]) + int(subs_list[1])
                        for i in top_formatted:
                            print(f"{i}{total:>5}\n")

                    elif "-" in math_problem:
                        subs_list = math_problem.split(" - ")
                        # Check if there are only digits
                        if subs_list[0].isdigit() and subs_list[1].isdigit():
                            # Check if each operation has more than 4 digits
                            if len(subs_list[0]) > 4 or len(subs_list[1]) > 4:
                                print("Error: Numbers cannot be more than four digits.")
                                break
                            else:
                                # Store formatted items in formatted_list
                                top_formatted.append(f"{subs_list[0]:>5}\n-{subs_list[1]:>4}\n-----\n")
                        # Subtraction
                        total = int(subs_list[0]) - int(subs_list[1])
                        for i in top_formatted:
                            print(f"{i}{total:>5}\n")


arithmetic_arranger(user_inp, tof=True)
