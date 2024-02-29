SPACE = 3
WIDTH = (SPACE + 1) * 10 + 1
print(WIDTH * "-")
y = 0
while y < 10:
    x = 1
    print("|", end="")
    while x <= 10:
        answer = str(y * 10 + x)
        spaces = SPACE - len(answer)
        print(spaces * " " + answer, end="|")
        x += 1
    print()
    y += 1
print(WIDTH * "-")