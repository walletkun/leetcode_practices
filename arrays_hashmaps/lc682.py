def calPoints(operations):
    res = []

    for i in range(len(operations)):
        if operations[i] == '+':
            res.append(res[-2] + res[-1])

        elif operations[i] == 'C':
            res.pop()

        elif operations[i] == 'D':
            res.append(res[-1] * 2)
            
        else:
            res.append(int(operations[i]))

    return sum(res)



test = ['5', '2' , 'C', 'D', '+']
print(calPoints(test))

    