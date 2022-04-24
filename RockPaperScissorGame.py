#update code in final resul by point
import random
def compare(A,B,C):
	if str1[A]==B:
		print("Draw! Both of You Choose ",str1[A],"\nYou both get 1 points")
	else :
		if str1[A]=="Snake" and B=="Water" :
			print("You Choose Snake and Computer Choose Water\nYou Win!----> You get 2 points")
		elif str1[A]=="Snake" and B=="Gun" :
			print("You Choose Snake and Computer Choose Gun\nSorry You Lose!----> Computer get 2 points")
		elif str1[A]=="Water" and B=="Gun" :
			print("You Choose Water and Computer Choose Gun\nYou Win!----> You get 2 points")
		elif str1[A]=="Water" and B=="Snake" :
			print("You Choose Water and Computer Choose Snake\nSorry You Lose!----> Computer get 2 points")
		elif str1[A]=="Gun" and B=="Snake" :
			print("You Choose Gun and Computer Choose Snake\nYou Win!----> You get 2 points")
		elif str1[A]=="Gun" and B=="Water" :
			print("You Choose Gun and Computer Choose Water\nSorry You Lose!----> Computer get 2 points")

C = 5
while C>0 :
	print("You have ",C," lifes")
	A=int(input("\nEnter Your choose :\n0 for snake\n1 for water\n2 for gun\n"))
	if A != 0 and A!=1 and A!=2 :
		print("Enter valid input")
		break
	str1 = ["Snake","Water","Gun"]
	B = random.choice(str1)
	compare(A,B,C)
	C=C-1
#print("       \n--------- Final Score --------")
#if Y==Co :
#	print(" The Match is Draw")
#elif Y>Co :
#	print(" You Win The Match")
#else :
#	print(" Computer Win The Match")