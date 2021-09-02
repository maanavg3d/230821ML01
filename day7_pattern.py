#########PATTERN 1#######


a = eval(input('Enter Number'))
for i in range(a):
    print('*'*(i + 1))


#########PATTERN 2#########


for i in range(1,a+1):
    print(' '*(a-i),'*'*i,sep = '')


########pattern 3########


##a = eval(input('Enter Number'))
for i in range(1,a+1):
    print('*'*i,' '*(2*(a-i)),'*'*i,sep='')


########pattern 4########

##a = eval(input('Enter Number'))
for i in range(1,a+1):
    for n in range(1,i+1):
        print(n,end='')
    print()

########pattern 5###########


##a = eval(input('Enter Number'))
for i in range(1,a+1):
    print(' '*(a-i),end='')
    for n in range(1,i+1):
        print(n,end='')
    print()

########pattern 6###########

##a = eval(input('Enter Number'))
for i in range(1,a+1):
    print(' '*(a-i),end='')
    for n in range(-i,0):
        print(-n,end='')
    print()

######pattern 7##########

for i in range(1,a+1):
    for n in range(1,i+1):
        print(n,end='')
    print(' '*(2*(a-i)), end='')
    for n in range(1,i+1):
        print(n,end='')
    print()

#######pattern 8##########

for i in range(1,a+1):
    for n in range(1,i+1):
        print(n,end='')
    print(' '*(2*(a-i)), end='')
    for n in range(-i,0):
        print(-n,end='')
    print()


