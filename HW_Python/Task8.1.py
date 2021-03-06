ip = {}
arg = input('Give name of file:')
with open(arg) as f:
    myList = [ line.split(' ') for line in f ]
    for c in myList[1::2]:
        if c != myList[-1]: 
            key = c[0]
            if c[9] == '-':
                byte = 0
            else:
                byte = int(c[9])
        val = ip.get(key,0)+byte
        ip[key] = val
for key, val in ip.items():
    print ('{} bytes for {}'.format(val, key))

