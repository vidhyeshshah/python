a=[]
n=int(input("Number of elements in array:"))
x=int(input("enter number you want to see index:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)
for i in range(0,n):
   if(a[i] == x):
      print("the inex of your element is:",i)
   else:
      print("-1")   