# print(sorted(["+", "-", "**", "*", "/", "!", "(", ")", "[", "]", "^", '$']))
opt = ["(", ")"]
split_eq = []
bracket = 0
# eq = ["(", "2", "+", "1", "-", "1", ")", "+", "(", "2", "+", "1", "-", "1", ")"]
eq = list(input(">> "))

for b in eq:
    if b == "(":
        bracket += 0.5
    if b == ")":
        bracket += 0.5


for a in range(int(bracket)):
    bracket_index = [0, 0]
    for i in eq:
        if i == "(":
            bracket_index[0] = eq.index(i)
        if i == ")":
            bracket_index[1] = eq.index(i)
            break
    for j in range(bracket_index[0] + 1, bracket_index[1]):
        split_eq.append(eq[j])
        eq[j] = " "
        eq[bracket_index[1]] = "$"
        eq[bracket_index[0]] = " "


for _ in range(4):
    for r in eq:
        if r == ' ':
            eq.remove(r)
            print(eq)


print(eq)
print(bracket)
print(split_eq)

