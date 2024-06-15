
def rpn(expression):
    operations = ["+", "-", "*", "/"]
    queue = []
    expression_list = expression.split()
    print(expression_list)

    for i, item in enumerate(expression_list):
        if i == 0 and item in operations:
            raise ValueError("no operands enough")
        else:
            if item.isdigit():
                queue.append(item)
            else:
                operand1 = int(queue.pop())
                if len(queue) > 0:
                    operand2 = int(queue.pop())
                else:
                    raise ValueError("invalid expression")

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
                    temp = operand2 / operand1 if operand1 != 0 else float('inf')
                    queue.append(temp)
                else:
                    raise ValueError("error, invalid operation")
    if len(queue) > 1 or len(queue) == 0:
        ValueError("error, result has 2 elements on the list")
    else:
        return queue.pop()