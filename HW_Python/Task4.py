import os

print("#Type 1 of string formatting")
e="This script has the following PID: {pid}. It was ran by {name} to work happily on {os}-{os_re}".format(pid=os.getpid(),name=os.getlogin(),os=os.name,os_re=os.uname())
print(e)

print("#Type 2 of string formatting")
e="This script has the following PID: %(pid)s. It was ran by %(name)s to work happily on %(os)s-%(os_re)s" %{"pid":os.getpid(),"name":os.getlogin(),"os":os.name,"os_re":os.uname()}
print(e)

print("#Type 3 of string formatting")
pid = os.getpid()
name= os.getlogin()
os_name = os.name
os_re=os.uname()
e=f"This script has the following PID: {pid}. It was ran by {name} to work happily on {os_name}-{os_re}"
print(e)
