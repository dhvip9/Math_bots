opt = ['+', '-', '*', 'x', '/', '^', '**', 'X', '_', '=', '(', ')', '[', ']', '%']   # | Opterators |
single_opt = ['!']                                                                   # |    List    |
opt_1 = ['+', '-', '*', '**']

print("""| | | | | |     | | | | |   | | | | |
  | |     | |   | |         | |      
  | |     | |   | | | |     | | | |  
  | |     | |   | |         | |      
| | | | | |     | | | | |   | | | | |""")
print("""-------------------------------------------------
 | Wellcome! To [ DEE ], The World Of MATHS    | 
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
        # working of operation of single
        if number_opt == 1:
            # Separate values and opterators
            numbers = [[], []]    # [0] for opterators, [1] for value
            for i in user_input:
                if i in single_opt:
                    numbers[0].append(i)

                elif i in opt:
                    numbers[0].append(i)
                    numbers[1].append(" ")

                else:
                    numbers[1].append(i)

            opterator = numbers[0]
            # -----------------------------
            # working of operation of single
            # L.H.S. Number
            raw_value1 = ""
            for i in numbers[1]:
                if i != " ":
                    raw_value1 += i
                else:
                    break

            # -----------------------------
            # R.H.S Number
            raw_value2 = ""
            if opterator[0] in opt:
                rhs_num = numbers[1]
                reves_value2 = ""
                index = -1
                reves_index = -1

                for j in reversed(rhs_num):
                    if j != " ":
                        reves_value2 += rhs_num[index]
                        index -= 1
                    else:
                        break

                for i in reves_value2:
                    raw_value2 += reves_value2[reves_index]
                    reves_index -= 1

                value = [float(raw_value1), float(raw_value2)]

            else:
                value = [float(raw_value1)]

            # ------------------------------
            # working of operation of use_single
            while True:

                # factorial[!]
                if opterator[0] == "!":
                    f = 1
                    value_copy = value[0]
                    final_value_fac = value[0]
                    while f < value_copy:
                        final_value_fac = final_value_fac * f
                        f += 1
                    print("=", final_value_fac)
                    print()
                    count += 1  # for Sequence count
                    print(count, ". [ Write Here ]")
                    break

        # -----------------------------
        # working of operation of Multipal
        elif number_opt == 0:
            # Separate values and opterators
            numbers = [[], []]    # [0] for opterators, [1] for value
            for i in user_input:
                if i in single_opt:
                    numbers[0].append(i)

                elif i in opt:
                    numbers[0].append(i)
                    numbers[1].append(i)

                else:
                    numbers[1].append(i)
            numbers[-1].append("=")
            opterator = numbers[0]

            # -----------------------------
            # for multi operations
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
            for _ in opterator:
                # for 0 divisible error
                if break_out_flag:
                    break

                # for sorting raw operation
                raw_sort_operater = []
                for a in multi_operation:
                    if a in opt_1:
                        raw_sort_operater.append(a)
                    elif a == "/":
                        raw_sort_operater.append("%")
                    elif a == "x":
                        raw_sort_operater.append("*")
                    elif a == "^":
                        raw_sort_operater.append("**")

                # for index of operater
                index_operater = []
                for a in multi_operation:
                    if a in opt:
                        index_operater.append(multi_operation.index(a))

                index_operater = [x for _, x in sorted(zip(raw_sort_operater, index_operater))]
                raw_sort_operater.sort()

                # for replace word[% to /]
                sort_operater = []
                for j in raw_sort_operater:
                    if j in opt_1:
                        sort_operater.append(j)
                    if j == "%":
                        sort_operater.append("/")

                # -----------------------------
                # for multi operation in use
                for x, i in zip(index_operater, sort_operater):
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
                            multi_operation[x - 1] = " "
                            multi_operation[x] = ans
                            multi_operation[1 + x] = " "
                            multi_operation.remove(" ")
                            multi_operation.remove(" ")
                            bodmas_list = ['0', '0', '0']
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
