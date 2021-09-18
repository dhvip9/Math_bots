opt = ['+', '-', '*', 'x', '/', '^', '**', 'X', '_', '=', '(', ')', '[', ']', '%']   # | Opterators |
single_opt = ['!']                                                                   # |    List    |

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

                value = [int(raw_value1), int(raw_value2)]

            else:
                value = [int(raw_value1)]

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
            # for multipal operations
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
            # for working in multipal operations
            short_list = []

            index = 0
            length_list = len(multi_operation)
            for x in opterator:
                for i in multi_operation:
                    if index <= 2:
                        short_list.append(i)
                    index += 1

                    # Division[/]
                if x == "/":
                    if short_list[2] == "0" or short_list[2] == "0 " or short_list[2] == " 0" or short_list[2] == " 0 ":
                        ans = 0
                        short_list.pop(0)
                        short_list.pop(0)
                        short_list.pop(0)
                        multi_operation.pop(0)
                        multi_operation.pop(0)
                        multi_operation.pop(0)
                        multi_operation.insert(0, ans)
                        index = 0
                        print("| WARNING! :- Zero [0] Cannot Divisible Any Number |")
                    else:
                        ans = int(short_list[0]) / int(short_list[2])
                        short_list.pop(0)
                        short_list.pop(0)
                        short_list.pop(0)
                        multi_operation.pop(0)
                        multi_operation.pop(0)
                        multi_operation.pop(0)
                        multi_operation.insert(0, ans)
                        index = 0

                        # multiplication[*]
                elif x == "*":
                    ans = int(short_list[0]) * int(short_list[2])
                    short_list.pop(0)
                    short_list.pop(0)
                    short_list.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.insert(0, ans)
                    index = 0

                    # power or exponent[^]
                elif x == "^" or x == "**":
                    ans = int(short_list[0]) ** int(short_list[2])
                    short_list.pop(0)
                    short_list.pop(0)
                    short_list.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.insert(0, ans)
                    index = 0

                    # Addition[+]
                elif x == "+":
                    ans = int(short_list[0]) + int(short_list[2])
                    short_list.pop(0)
                    short_list.pop(0)
                    short_list.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.insert(0, ans)
                    index = 0

                # Subtraction[-]
                elif x == "-":
                    ans = int(short_list[0]) - int(short_list[2])
                    short_list.pop(0)
                    short_list.pop(0)
                    short_list.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.pop(0)
                    multi_operation.insert(0, ans)
                    index = 0

            print("=", multi_operation[0])
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
