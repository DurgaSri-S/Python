a=[]
for i in range(1,6):
    print("enter the number",i,":")
    b=int(input())
    a.append(b)
print("unsorted list",a)

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:  
            a[i], a[j] = a[j], a[i]

print("ordered list:",a)   


