print('#IP ADDR: 193.106.31.130')
month={}
arg=input('Give name of file:')
with open(arg) as f:
    myList = [ line.split() for line in f ]
    for c in range(1, len(myList)):
        ip=myList[c][0]
        if ip=='193.106.31.130':
            date1=myList[c][3].split(':')
            date2=date1[0].split('/')
            date_sum=date2[1]+date2[2]
            count=month.get(date_sum,0)+1
            month[date_sum]=count
for key, val in month.items():
    print ('{} – {} req'.format(key, val))

