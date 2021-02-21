def listMAX(answer):
    notint=[]
    new_answer=[]
    c=0
    for num in answer:
        if(type(num)!=int):
            notint.append(num)
            c=1
    if c==1:
        print("You've passed some extra elements that I can't parse: ",end=' ')
        return notint
    else:
        answer.sort(reverse = True)
        new_answer=answer[:3]
    return(new_answer)

print("Example 1:")
list1=[1,234,3,77,96,54,33,1111]
print(listMAX(list1))
print("Example 2:")
list1=[1,2,3,66.25,96,54.88,33]
print(listMAX(list1))
print("Example 3:")
list1=[1,2,3,'hola',96,54,33]
print(listMAX(list1))
print("Example 4:")
list1=[3,96]
print(listMAX(list1))
print("Example 5:")
list1=[9]
print(listMAX(list1))

