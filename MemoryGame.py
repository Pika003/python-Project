import random
import time
N=0
count = 1
print("          ---- Wellcome To Remember Game ----")
while N == 0:
	sum = 0
	arr=[]
	L = [0,1,2,3,4,5,6,7,8,9]
	
	for i in range(count):
		A = int(random.choice(L))
		arr.append(A)
		sum = sum + pow(10, count-i-1) * A
	print("]>> ",arr)
	time.sleep(2.4)
	for i in range(20):
		print("\n")
	K=int(input("]>> "))
	if sum == K :
		print("\n Right Ans\n")
		count = count+1
	else :
		print("\n   Wrong Ans\n You Loss The Game")
		count = count-1
		break
		
	if count == 0 :
		N=1
		break
	elif count == 8:
		N=1
		print(" \n        ----- Congratulation You Win The Game -----\n")
		break
	else :
		N=0