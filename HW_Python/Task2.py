def even_number(listt):
    new_list = []
    k = 0
    if hasattr(listt, '__iter__'): 
        for num in listt:
            if(type(num) != int):
                print("Sorry,I find word")  
                k = 1
        if k != 1:
            for num in listt:   
                if num %2 == 0:
                    if num != 254:
                        new_list.append(num)
                    else:
                        print("Sorry,I find 254. So ", end=' ')
                        break
            print("New List=", new_list)
    else:
        print("Sorry,this object is not iterable")
    
list1 = [1,2,3,4,5,6,7,8,9,100,88]
even_number(list1)
list1 = [1,2,3,"hola",5,6,7,8,9,100,88]
even_number(list1)
list1 = [1,2,3,4,5,254,7,8,9,100,88]
even_number(list1)
list1 = 1
even_number(list1)

