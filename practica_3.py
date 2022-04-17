def task1 (orig: str):
    new = []
    for elem in orig.split():
        if elem in "+-*":
            a = new.pop()
            b = new.pop()
            if elem == '+':
                result = a+b
            elif elem == '-':
                result = a-b
            else:
                result = a*b
            new.append(result)
        else:
            new.append(int(elem))
    return(new.pop())
# print(task1(input("Введите команду в постфиксной записи: ")))

def calc(expr):
    stack = []
    for token in expr.split():
        if token.isnumeric():
            stack.append(token)
            #print(stack)
        else:
            if token in ['+', '-', '*', '/']:
                a, b = stack.pop(), stack.pop()
                c = eval(b + token + a)
                stack.append(str(c))
    return stack.pop()
# print(calc("1 2 3 * + 2 -"))

def task2(strok: str) -> bool:
    stec_1 = []
    stec_2 = []
    stec_3 = []
    for elem in strok:
        if elem in "()":
            if elem in "(":
                stec_1.append("(")
            elif len(stec_1) > 0:
                stec_1.pop()
            else:
                return False
        if elem in "{}":
            if elem in "{":
                stec_2.append("{")
            elif len(stec_2) > 0:
                stec_2.pop()
            else:
                return False
        if elem in "[]":
            if elem in "[":
                stec_3.append("[")
            elif len(stec_3) > 0:
                stec_3.pop()
            else:
                return False
    if len(stec_1) == 0 and len(stec_2) == 0 and len(stec_3) == 0:
        return True
    else:
        return False
# print(task2("( ) { [ ] ( ] { } }"))

def check_delimiter(s):
    delimiter = {
        ')':'(',
        ']':'[',
        '}':'{',
        }
    stack = []
    for token in s.split():
        if token not in delimiter:
            stack.append(token)
        else:
            if not stack:
                return False
            else:
                if delimiter[token] == stack.pop():
                    pass
                else:
                    return False
    return True
print(task2("( ) { [ ] ( ] { } }"))


def task3(var1:str, var2:str):
    file = open(var1, "r", encoding="utf8")
    stroki = file.readlines()
    file.close()
    file = open(var2, "w", encoding="utf8")
    num = 0
    for line in stroki:
        num += 1
        file.write(str(num)+ " " + line)
    file.close()
    return f"Выполнено!"
# print(task3('text.txt', 'update text.txt'))
