def dictionary (answer):
    d = {}
    for i in answer:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    return d

print(dictionary(input("Enter string for dictionary: ")))
