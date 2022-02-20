##########question 8 ##########

##a = list('abcdefghijklmnopqrstuvwxyz')
##b = list(input('Enter a String').lower())
##for i in a:
##    for n in b:
##        if i == n:
##            m = True
##            break
##        else:
##            m = False
##    if m == True:
##        continue
##    else:
##        print('not panagram')
##        break
##if m == True:
##    print('panagram')



#######question 9 #########

##a = (input('Enter a number'))
##b = eval(input('Enter range'))
##l = [int(i*a) for i in range(1,b+1)]
##print('Sum of the following pattern {}'.format(l) , '= ',sum(l))

#######question 10 ##########

##s = (input('Enter list'))
##x = s.count('#')
##l = [[i] for i in s.split('#')]
##d ={('m'+str(i)):l[i] for i in range(x+1)}
##print(d)
##nd = {}
##for i in d:
##    nd[i] = [int(n) for n in ((d[i])[0].split())]
##print(nd)

#########question 11###########

##l = input('Enter Words').split(',')
##l.sort()
##s = ','.join(l)
##print(s)


#########question 12##########

##d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
##
##def highest_marks(d):
##    print(d['Student'][d['Marks'].index(max(d['Marks']))])
##
##highest_marks(d)

##########question 13#########

##l = [i for i in input('enter alphanumeric sentence')]
##a = 0
##d = 0
##for i in l:
##    if i.isalpha():
##        a += 1
##    elif i.isalnum():
##        d += 1
##print('LETTERS',a)
##print('DIGITS', d)

#########question 14##########

##d = {'Name': ['Akash', 'soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
##     'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
##     'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
##s = input('Enter subject choice from python, java, C').lower()
##newData = {n:[] for n in d}
##for m,i in enumerate(d['Subject']):
##    if i.lower() == s:
##        {newData[n].append(d[n][m]) for n in d}
##print(newData)        


#########question 15#########

##m = eval(input('Enter number for divisibilty check'))
##n = eval(input('Enter number till which divisibility check is required '))
##   
##def divi(m,n):
##    [print(i) for i in range(1,n+1) if not i%m]
##divi(m,n)

##########question 16#########


##origin = (0,0)
##d = {}
##u, d, l, r = [int(i) for i in (input('enter step values for up,down,left and right respectively')).split(',')]    
##x = (r - l)
##y = (u - d)
##dist = (((x-origin[0])**2 + (y-origin[1])**2)**0.5)
##print('''For the given steps the current position cordinates are (x,y) = {} and
##       Distance from origin is {}'''.format((x,y),dist))

