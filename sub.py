import Logo_Variable
import Bot


def raw_equation():
    numbers = [[], []]  # [0] for operators, [1] for value
    for i in Bot.user_input:
        if i in Logo_Variable.opt:
            numbers[1].append(i)

        elif i in Logo_Variable.single_opt:
            numbers[1].append(i)

        else:
            numbers[1].append(i)
    numbers[-1].append("=")
    return numbers[1]


def operator():
    numbers = [[], []]  # [0] for operators, [1] for value
    for i in Bot.user_input:
        if i in Logo_Variable.single_opt:
            numbers[0].append(i)

        elif i in Logo_Variable.opt:
            numbers[0].append(i)
    return numbers[0]


def equation():
    multi_operation = []
    raw_value1 = ""
    for i in raw_equation():
        if i not in Logo_Variable.opt and i not in Logo_Variable.single_opt:
            raw_value1 += i
        else:
            multi_operation.append(raw_value1)
            multi_operation.append(i)
            raw_value1 = ""
    multi_operation.remove("=")
    for j in multi_operation:
        if j == '':
            multi_operation.remove(j)
        if j == ' ':
            multi_operation.remove(j)
    return multi_operation


def sort_operation():
    raw_sort_operater = []
    for a in Bot.final_equation:
        if a in Logo_Variable.opt_1:
            raw_sort_operater.append(a)
        if a == "/":
            raw_sort_operater.append("%")
        if a == "x":
            raw_sort_operater.append("*")
        if a == "^":
            raw_sort_operater.append("$")

    # for index of operater
    index_operater = []
    for a in Bot.final_equation:
        if a in Logo_Variable.opt_1:
            index_operater.append(Bot.final_equation.index(a))
        elif a == "/":
            index_operater.append(Bot.final_equation.index(a))
        elif a == "^":
            index_operater.append(Bot.final_equation.index(a))
        elif a == "x":
            index_operater.append(Bot.final_equation.index(a))
    index_operater = [x for _, x in sorted(zip(raw_sort_operater, index_operater))]
    raw_sort_operater.sort()

    # for replace word[% to /]
    sort_operater = []
    for j in raw_sort_operater:
        if j in Logo_Variable.opt_1:
            sort_operater.append(j)
        if j == "%":
            sort_operater.append("/")
        if j == "$":
            sort_operater.append("^")
    return index_operater, sort_operater, raw_sort_operater


def clear_value(index, ans):
    Bot.final_equation[index - 1] = " "
    Bot.final_equation[index] = ans
    Bot.final_equation[1 + index] = " "
    Bot.final_equation.remove(" ")
    Bot.final_equation.remove(" ")


def clear_single(index, ans):
    Bot.final_equation[index - 1] = " "
    Bot.final_equation[index] = ans
    Bot.final_equation.remove(" ")


def last_value(last_operator):
    if last_operator == "/":
        Bot.digit_2 = float(Bot.bodmas_list[2])
    if last_operator == "*" or last_operator == "x":
        Bot.digit_2 = float(Bot.bodmas_list[2])
    if last_operator == "^" or last_operator == "**":
        Bot.digit_2 = float(Bot.bodmas_list[2])
    if last_operator == "+":
        Bot.digit_2 = float(Bot.bodmas_list[2])
    if last_operator == "-":
        Bot.digit_2 = float(Bot.bodmas_list[2])
    return Bot.digit_2


def equal_operator(use_operator):
    if use_operator == "/":
        Bot.Ans = Bot.Ans / Bot.Second_value
    elif use_operator == "*" or use_operator == "x":
        Bot.Ans = Bot.Ans * Bot.Second_value
    elif use_operator == "^" or use_operator == "**":
        Bot.Ans = Bot.Ans ** Bot.Second_value
    elif use_operator == "+":
        Bot.Ans = Bot.Ans + Bot.Second_value
    elif use_operator == "-":
        Bot.Ans = Bot.Ans - Bot.Second_value
    return Bot.Ans
