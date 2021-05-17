a=[1,2,3]
for data in a:
    if data < 2:
        print(f"{data}<2")
    else:
        print(f"{data}>=2")

a1="hello"
a2="hello"
print(a1,id(a1))
print(a2,id(a2))
print(a1==a2)
print(a1 is a2)

if 1 in a:
    print("haoye")
if 4 not in a:
    print("haoya")

emptylist=[]
if not emptylist:
    print("kongde")