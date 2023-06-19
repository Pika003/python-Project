print("    ------------  My Dairy For Daily Rutin  -------------\n")
oparation=int(input("What You Want :\n1. For See\n2. For Update\n"))
if(oparation==1) :
	A=int(input("Select one option:\n1. For Food\n2. For Exercises\n"))
	if(A==1) :
		f1= open("Food.txt","rt")
		content=f1.read()
		print(content)
		f1.close()
	elif(A==2) :
		f2= open("Exercises.txt","rt")
		contents=f2.read()
		print(contents)
		f2.close()
	else :
		print("Sorry plese check your input")
elif(oparation==2) :
	B=int(input("Select one option:\n1. For Food\n2. For Exercises\n3. For Add another Option\n"))
	print("enter in this formet: , _")
	if(B==1) :
		f3=open("Food.txt","a")
		newfood=input("")
		f3.write(newfood)
		f3.close()
	elif(B==2) :
		f4=open("Exercises.txt","a")
		newexe=input("")
		f4.write(newexe)
		f4.close()
	elif(B==3) :
		print("Sorry this features is not available right now")
	else:
		print("Sorry plese check your input")
else :
	print("Sorry plese check your input")