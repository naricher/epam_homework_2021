user={}
arg=input('Give name of file: ')
with open(arg) as f:
    myList = [ line.split('"') for line in f ]
    for c in range(1, len(myList)):
        agent=myList[c][5]
        count=user.get(agent,0)+1
        user[agent]=count
max_val = max(user.values())
for key, val in user.items():
    if val==max_val:
        print('The most frequent user agent is: {} (count={})'.format(key,val))
