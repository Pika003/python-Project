import random
import time
import os

def rol():
	L = [1,2,3,4,5,6]
	A = int(random.choice(L))
	return A
	
def win(a):
    os.system('clear')
    print("\n             --------+ "+a+" Win the game +--------\n");
    print("               -------+ ∆  EXIT  ∆ +-------   \n")
    exit()

def player1(TP1,TP2,ppp1,ppp2):
    while TP1 != 10 :
        p1 = int(input("       "+ppp1+": "))
        if p1 == 1:
            pp1=rol()
            print("       "+ppp1+" got "+str(pp1))
            TP1 = TP1+pp1
            
            if TP1 == 10 :
            	time.sleep(1)
            	win(ppp1)
            elif TP1>10 :
                TP1 = TP1-pp1;
                print("       Sorry your point don't add at this time\n")
                time.sleep(1)
                os.system('clear')
                display(ppp1,ppp2,TP1,TP2)
                player2(TP1,TP2,ppp1,ppp2)
                
            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            player2(TP1,TP2,ppp1,ppp2)
        elif p1 == 2 :
            TP1 = TP1 + 1
            print("       Skip this time\n")
            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            
            if TP1 == 10 :
            	time.sleep(1)
            	win(ppp1)
            else :
            	player2(TP1,TP2,ppp1,ppp2)
        else :
            print("       You Enter Wrong Option\n")
            print("       You don't get any point\n\n")
            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            player2(TP1,TP2,ppp1,ppp2)
            
            
def player2(TP1,TP2,ppp1,ppp2):
    while TP2 != 10 :
        p2  = int(input("       "+ppp2+": "))
        if p2 == 1 :
            pp2=rol()
            print("       "+ppp2+" got "+str(pp2))
            TP2 = TP2+pp2
            
            if TP2 == 10 :
            	time.sleep(1)
            	win(ppp2)
            elif TP2>10 :
                TP2 = TP2-pp2;
                print("       Sorry your point don't add at this time\n")
                time.sleep(1)
                os.system('clear')
                display(ppp1,ppp2,TP1,TP2)
                player1(TP1,TP2,ppp1,ppp2)

            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            player1(TP1,TP2,ppp1,ppp2)
        elif p2 == 2 :
            TP2 = TP2 + 1
            print("       Skip this time\n")
            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            
            if TP2 == 10 :
            	time.sleep(1)
            	win(ppp2)
            else :
            	player1(TP1,TP2,ppp1,ppp2)
        else :
            print("       You Enter Wrong Option\n")
            print("       You don't get any point\n\n")
            time.sleep(1)
            os.system('clear')
            display(ppp1,ppp2,TP1,TP2)
            player1(TP1,TP2,ppp1,ppp2)


def display(ppp1,ppp2,TP1,TP2):
    print("\n           -----------+ LUDU [] GAME +-------------   \n");
    print("                       -------------")
    print("    Instruction        |    1 0    |       Score Board ")
    print("    -----------        -------------       -----------")
    print("    1: For rol         | 9 | 8 | 7 |       "+ppp1+": "+str(TP1))
    print("    2: For skip        -------------       "+ppp2+": "+str(TP2))
    print("                       | 6 | 5 | 4 |  ")
    print("                       ------------- ")
    print("                       | 3 | 2 | 1 | ")
    print("                       ------------- ")
    
    
    
TP1=int(00)
TP2=int(00)
print("\n           -----------+ LUDU [] GAME +-------------   \n");
print("\n ∆ RULES:\n         • Reached 10 point fast to win the game\n         • Dice has unique value 1 to 6\n         • If You Skip You get only 1 point\n")
print(" ∆ Instruction:")
print("         • Press 1: For rol the dice")
print("         • Press 2: For skip\n")
print(" ∆ Players:")
ppp1 =input("         • Enter Player1 Name:  ")
ppp2 = input("         • Enter Player2 Name:  ")
print("\n           --------- Lets Play The Game -----------\n\n")
time.sleep(1)
os.system('clear')
display(ppp1,ppp2,TP1,TP2)
player1(TP1,TP2,ppp1,ppp2)