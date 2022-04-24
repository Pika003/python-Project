name=input("Enter Your name:  ")
fm=int(input("what is the full marks of a subject: "))
lis=[]
n=int(input("Plese tell me the total no of your subject: "))
for i in range(0, n):
    ele = int(input("plese enter the no one by one:  "))
    lis.append(ele)
print(name," Your marks are: ",lis)
Avg=0
j=0
for i in range(0,n):
	Avg=Avg+lis[j]
	j=j+1

Avg=(Avg/n)
p=(Avg/fm)*100
print(name," Your avg. marks is: ",Avg," out of ",fm)

if p>=30 :
	print("Congratulations you pass your exam by ",p,"% number.")
else :
	print("I am sorry but you could not pass this time.")
	print("Your marks is only ",p,"% number.")