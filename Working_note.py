from MathBot import user_input
import Logo_Info


def raw_equation():
    numbers = [[], []]  # [0] for operators, [1] for value
    for i in user_input:
        if i in Logo_Info.opt:
            numbers[1].append(i)

        elif i in Logo_Info.single_opt:
            numbers[1].append(i)

        else:
            numbers[1].append(i)
    numbers[-1].append("=")
    return numbers[1]


def operator():
    numbers = [[], []]  # [0] for operators, [1] for value
    for i in user_input:
        if i in Logo_Info.single_opt:
            numbers[0].append(i)

        elif i in Logo_Info.opt:
            numbers[0].append(i)
    return numbers[0]
