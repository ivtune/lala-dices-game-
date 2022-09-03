print("WELCOME LALA DICES GAME\nBEST OF FIVE")
z=1
fp=0
gp=0
def start ():
    from random import randint


    a=randint(1,6)
    b=randint(1,6)
    c=randint(1,6)
    d=randint(1,6)
    f=a+b
    g=c+d
    n=input("player 1\npress enter to roll")
    print("1st die:",a,"2nd die:",b,)
    print("sum=",f)
    v=input("player 2\npress enter to roll")
    print("1st die:",c,"2nd die",d)
    print("sum=",g)
    if f>g:
        print("player 1 gain's one point!") and fp+1
    elif f==g:
        print("both players gain one point!") and fp+1 and gp+1
    elif f<g:
        print("player 2 gain's one point") and gp+1
    else:
        print("error please refresh")
    
while z<=5 :       
  start()
  z+=1
if fp>gp :
    print("End\n player 1 win's!")
elif fp==gp :
    print("End\nboth players draw !")
else:
    print("End\nplayer 2 win's ! ")