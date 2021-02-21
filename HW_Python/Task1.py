answer=input("Enter numbers: ")
list = [int(x) for x in answer.split(',')]
print(list)
tuplee = tuple(int(x) for x in answer.split(','))
print(tuplee)
