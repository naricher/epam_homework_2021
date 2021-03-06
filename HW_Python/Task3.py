import sys
print ("#Arguments:", sys.argv[1:])
k = 0
while k == 0:
    answer = input("Enter my favourite word or phrase: ")
    for i in sys.argv[1:]: 
        if i == answer:
            k = 1
    if k <= 0:
        print("No, it's not what I want!")
print("Yes, this is my favorite word! Thank you, bye!")


