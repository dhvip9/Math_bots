# opt = ["+", "-", "**", "*", "/", "!", "(", ")", "[", "]", "^", '$']
# opt = ["(", ")"]
# eq = ["(", "2", "+", "1", "-", "1", ")", "+", "(", "2", "+", "1", "-", "1", ")"]
# eq = list(input(">> "))
bodmas_list = ['0', '0', '0']


def if_bracket(equation):
    split_eq = []
    bracket = 0
    for b in equation:
        if b == "(":
            bracket += 0.5
        elif b == ")":
            bracket += 0.5
    print(bracket)
    for a in range(int(bracket)):
        bracket_index = [0, 0]
        for i in equation:
            if i == "(":
                bracket_index[0] = equation.index(i)
            if i == ")":
                bracket_index[1] = equation.index(i)
                break
        print(bracket_index)
        for j in range(bracket_index[0] + 1, bracket_index[1]):
            split_eq.append(equation[j])
            equation[j] = " "
            equation[bracket_index[1]] = "$"
            equation[bracket_index[0]] = " "
        print(split_eq)
    return equation


def remove_space(equation):
    for _ in range(4):
        for r in equation:
            if r == ' ':
                equation.remove(r)
                # print(equation)
    return equation


def if_bracket_2(equation):
    split_eq = []
    bracket = 0
    for b in equation:
        if b == "[":
            bracket += 0.5
        elif b == "]":
            bracket += 0.5
    print(bracket)
    for a in range(int(bracket)):
        bracket_index = [0, 0]
        for i in equation:
            if i == "[":
                bracket_index[0] = equation.index(i)
            if i == "]":
                bracket_index[1] = equation.index(i)
                break
        print(bracket_index)
        for j in range(bracket_index[0] + 1, bracket_index[1]):
            split_eq.append(equation[j])
            equation[j] = " "
            equation[bracket_index[1]] = "$"
            equation[bracket_index[0]] = " "
        print(split_eq)
    return equation


bracket_eq = if_bracket(list(input(">> ")))
remove_space(bracket_eq)
print(bracket_eq)
bracket_eq_2 = if_bracket_2(bracket_eq)
remove_space(bracket_eq_2)
print(bracket_eq_2)
