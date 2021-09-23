opt = ['+', '-', '*', 'x', '/', '^', '**', 'X', '_', '=', '(', ')', '[', ']', '%']   # | Operation  |
single_opt = ['!']                                                                   # |    List    |
opt_1 = ['+', '-', '*', '**']

print("""| | | | | |     | | | | |   | | | | |
  | |     | |   | |         | |      
  | |     | |   | | | |     | | | |  
  | |     | |   | |         | |      
| | | | | |     | | | | |   | | | | |""")
print("""-------------------------------------------------
 | Welcome! To [ DEE ], The World Of MATHS    | 
 | Exit from 'DEE' Write [ exit ] in Lower Case|
-------------------------------------------------""")
print("1 . [ write Here ]")
count = 1  # for Sequence count

while True:
    user_input = str(input(">> "))
    ans = 0
    number_opt = 0
    for j in user_input:
        if j in single_opt:
            number_opt = 1

    # -----------------------------
    # for Exit
    if user_input == "exit":
        print("| ThankYou! For Visiting [ DEE Maths ] |")
        break
    else:
        # -----------------------------
        # working of operation for single
        if number_opt == 1:
            # Separate values and operation
            numbers = [[], []]    # [0] for operation, [1] for value
            for i in user_input:
                if i in single_opt:
                    numbers[0].append(i)

                elif i in opt:
                    numbers[0].append(i)
                    numbers[1].append(" ")

                else:
                    numbers[1].append(i)

            operator = numbers[0]

            # -----------------------------
            # for combine value in single operations
            raw_value1 = ""
            for i in numbers[1]:
                if i != " ":
                    raw_value1 += i
                else:
                    break
            value = float(raw_value1)

            # ------------------------------
            # for single operation in use
            while True:
                # factorial[!]
                if operator[0] == "!":
                    f = 1
                    value_copy = value
                    final_value_fac = value
                    while f < value_copy:
                        final_value_fac = final_value_fac * f
                        f += 1
                    print("=", final_value_fac)
                    print()
                    count += 1  # for Sequence count
                    print(count, ". [ Write Here ]")
                    break

        # -----------------------------
        # working of operation for Multi
        elif number_opt == 0:
            # Separate values and operation
            numbers = [[], []]    # [0] for operation, [1] for value
            for i in user_input:
                if i in single_opt:
                    numbers[0].append(i)

                elif i in opt:
                    numbers[0].append(i)
                    numbers[1].append(i)

                else:
                    numbers[1].append(i)
            numbers[-1].append("=")
            operator = numbers[0]

            # -----------------------------
            # for combine value in multi operations
            multi_operation = []

            raw_value1 = ""

            for i in numbers[1]:
                if i not in opt:
                    raw_value1 += i

                else:
                    multi_operation.append(raw_value1)
                    multi_operation.append(i)
                    raw_value1 = ""
            multi_operation.remove("=")

            # -----------------------------
            # for BODMAS
            bodmas_list = ['0', '0', '0']
            break_out_flag = False
            for _ in operator:
                # for 0 divisible error
                if break_out_flag:
                    break

                # for sorting raw operation
                raw_sort_operator = []
                for a in multi_operation:
                    if a in opt_1:
                        raw_sort_operator.append(a)
                    elif a == "/":
                        raw_sort_operator.append("%")
                    elif a == "x":
                        raw_sort_operator.append("*")
                    elif a == "^":
                        raw_sort_operator.append("**")

                # for index of operation
                index_operator = []
                for a in multi_operation:
                    if a in opt:
                        index_operator.append(multi_operation.index(a))

                index_operator = [x for _, x in sorted(zip(raw_sort_operator, index_operator))]
                raw_sort_operator.sort()

                # for replace word[% to /]
                sort_operator = []
                for j in raw_sort_operator:
                    if j in opt_1:
                        sort_operator.append(j)
                    if j == "%":
                        sort_operator.append("/")

                # -----------------------------
                # for multi operation in use
                for x, i in zip(index_operator, sort_operator):
                    bodmas_list[0] = multi_operation[x - 1]
                    bodmas_list[1] = multi_operation[x]
                    bodmas_list[2] = multi_operation[1 + x]

                    # Division[/]
                    if i == "/":
                        if bodmas_list[2] == "0" or bodmas_list[2] == "0 " or \
                                bodmas_list[2] == " 0" or bodmas_list[2] == " 0 ":
                            ans = 0
                            print("| WARNING! :- Zero [0] Cannot Divisible Any Number |")
                            break_out_flag = True
                            break
                        else:
                            ans = float(bodmas_list[0]) / float(bodmas_list[2])
                            multi_operation[x - 1] = " "
                            multi_operation[x] = ans
                            multi_operation[1 + x] = " "
                            multi_operation.remove(" ")
                            multi_operation.remove(" ")
                            bodmas_list = ['0', '0', '0']
                            break

                    # multiplication[*]
                    elif i == "*" or i == "x":
                        ans = float(bodmas_list[0]) * float(bodmas_list[2])
                        multi_operation[x - 1] = " "
                        multi_operation[x] = ans
                        multi_operation[1 + x] = " "
                        multi_operation.remove(" ")
                        multi_operation.remove(" ")
                        bodmas_list = ['0', '0', '0']
                        break

                    # power or exponent[^]
                    elif i == "^" or i == "**":
                        ans = float(bodmas_list[0]) ** float(bodmas_list[2])
                        multi_operation[x - 1] = " "
                        multi_operation[x] = ans
                        multi_operation[1 + x] = " "
                        multi_operation.remove(" ")
                        multi_operation.remove(" ")
                        bodmas_list = ['0', '0', '0']
                        break

                    # Addition[+]
                    elif i == "+":
                        ans = float(bodmas_list[0]) + float(bodmas_list[2])
                        multi_operation[x - 1] = " "
                        multi_operation[x] = ans
                        multi_operation[1 + x] = " "
                        multi_operation.remove(" ")
                        multi_operation.remove(" ")
                        bodmas_list = ['0', '0', '0']
                        break

                    # Subtraction[-]
                    elif i == "-":
                        ans = float(bodmas_list[0]) - float(bodmas_list[2])
                        multi_operation[x - 1] = " "
                        multi_operation[x] = ans
                        multi_operation[1 + x] = " "
                        multi_operation.remove(" ")
                        multi_operation.remove(" ")
                        bodmas_list = ['0', '0', '0']
                        break

            print("=", ans)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
