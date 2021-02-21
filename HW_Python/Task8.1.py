ip={}
arg=input('Give name of file:')
with open(arg) as f:
    myList = [ line.split() for line in f ]   
    for c in range(1, len(myList)):    
        key=myList[c][0]
        byte=int(myList[c][8])
        val=ip.get(key,0)+byte
        ip[key]=val
for key, val in ip.items():
    print ('{} bytes for {}'.format(val, key))

