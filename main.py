operations = ["+", "-", "*", "/"]


def rpn(expression):
    queue = []
    expression_list = expression.split()
    print(expression_list)

    for i, item in enumerate(expression_list):
        if i == 0 and item in operations:
            print("no operands enough")
            break
        else:
            if item.isdigit():
                queue.append(item)
            else:
                operand1 = int(queue.pop())
                if len(queue) > 0:
                    operand2 = int(queue.pop())
                else:
                    print("invalid expression")
                    break

                if item == "+":
                    temp = operand2 + operand1
                    queue.append(temp)
                elif item == "-":
                    temp = operand2 - operand1
                    queue.append(temp)
                elif item == "*":
                    temp = operand2 * operand1
                    queue.append(temp)
                elif item == "/":
                    temp = operand2 / operand1
                    queue.append(temp)
                else:
                    print('error, invalid operation')
            print(queue)
    print(queue)
    if (len(queue) > 1 or len(queue) == 0):
        print("error, result has 2 elements on the list")
    else:
        return queue.pop()


if __name__ == "__main__":
    result = rpn("5 8 + + 5 * 5 /")
    print(result)