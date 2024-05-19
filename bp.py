active=input("wanna use what? ")
#diamond
if active=="diamond":
    def half_one(tall):
        x=1
        space=tall
        for i in range(tall):
            space-=1
            print(" "*space+"*"*x)
            x+=2
    def half_two(tall):
        x=tall*2-3
        space=1
        for i in range(tall):
            print(" "*space+"*"*x)
            x-=2
            space+=1
    tall=int(input("high(this will be x2): "))
    half_one(tall)
    half_two(tall)
#block
if active=="block":
    length=int(input("length??? "))
    for i in range(length):
        print("[]"*length)
#circle
if active=="circle":
    ls=int(input("mc circle (number>1): "))
    space1=0
    for i in range(1,ls):
        space1+=i
    space1+=ls-1
    space2=ls
    print(" "*space1+"o"*ls)
    a=ls**2+(ls-2)*2
    b=a//2
    if a<=b*2:
        a=int(a/2)
        c=0
    elif a>b*2:
        a=int((a-1)/2)
        c=1
    def half_one():
        global space1,space2,ls,c
        d=ls-1
        space1-=d
        for i in range(ls-1):
            print(" "*space1+"o"*d+" "*space2+"o"*d)
            space2+=d*2
            d-=1
            space1-=d
        for i in range(2,ls):
            space1-=1
            for j in range(i):
                print(" "*space1+"o"+" "*space2+"o")
            space2+=2
        if c==0:
            for i in range(int(ls/2)):
                print("o"+" "*space2+"o")
        elif c==1:
            for i in range(int((ls-1)/2)+1):
                print("o"+" "*space2+"o")
    def half_two():
        global space1,space2,ls,c
        if c==0:
            for i in range(int(ls/2)):
                print("o"+" "*space2+"o")
        elif c==1:
            for i in range(int((ls-1)/2)):
                print("o"+" "*space2+"o")

    half_one()
    half_two()