def rpn_cal(expression):
        """
           Évalue une expression en notation polonaise inverse (NPI).

           Args:
               expression (str): L'expression en NPI à évaluer.

           Returns:
               float: Le résultat de l'évaluation de l'expression.

           Raises:
               ValueError: Si l'expression est invalide ou contient des caractères non supportés.
        """

        operations = ["+", "-", "*", "/"]
        queue = []
        for i, item in enumerate(expression.split()):
            if not item.isdigit() and item not in operations:
                raise ValueError("Expression must contain space between or  must not contain characters..")

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
                        if operand1 == 0:
                            raise ValueError("error, can't divide by zero")
                        temp = operand2 / operand1
                        queue.append(temp)
                    else:
                        raise ValueError("error, invalid operation")
        if len(queue) > 1 or len(queue) == 0:
            raise ValueError("error, result has 2 elements on the list")
        else:
            return queue.pop()
