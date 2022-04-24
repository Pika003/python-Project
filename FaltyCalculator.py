#Make a cheting calculator
#sum of (2+3) and (4-2) is fake
op=input("Enter oparation + - * / \n")
A=int(input("Enter 1st no: "))
B=int(input("Enter 2nd no: "))
if(op == "+"):
	if(A==2):
		if(B==3):
			print("sum of two no is: 7")
		else:
			print("sum of two no:",(A+B))
	else:
		print("sum of two no:",(A+B))
elif(op == "-"):
	if(A==4):
		if(B==2):
			print("sub of two no is 5")
		else:
			print("sub of two no is",(A-B))
	else:
		print("sub of two no is",(A-B))
elif(op == "*"):
	print("multiple of two no is",(A*B))
elif(op == "/"):
	if(B==0):
		print("Infinite value return")
	else:
		print("devition of two no is",(A/B))
else:
	print("Enter a valid oparation")