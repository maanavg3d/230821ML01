Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a = 20; a+=30: a%=3; print(a)
SyntaxError: invalid syntax
>>> a = 20; a+=30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> False and False
False
>>> True and True
True
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False is True
False
>>> False is False
True
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> True>False
True
>>> False>True
False
>>> s1 = 'Nice to have it'
>>> s2 = 'here'
>>> print(s1 + ' ' + s2)
Nice to have it here
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2][0]
'hello'
>>> a.insert[0] = s1
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.insert[0] = s1
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> a.insert[0] == s1
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.insert[0] == s1
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.insert[0] = 'car'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.insert[0] = 'car'
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> a.insert = s1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.insert = s1
AttributeError: 'list' object attribute 'insert' is read-only
>>> a.insert(0,s1)
>>> a.insert(-1,s2)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 'here', 7]
>>> del a[-1]
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 'here']
>>> del a[-1]
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1]
>>> a+= 7
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a+= 7
TypeError: 'int' object is not iterable
>>> a+=[7,[s2]]
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ['here']]
>>> del a[-1]
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.append(s2)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
>>> for i in numbers:
	if i%2 = 0:
		
SyntaxError: invalid syntax
>>> for i in numbers:
	if i != 237:
		if i%2 == 0:
			print(i)

			
386
462
418
344
236
566
978
328
162
758
918
412
566
826
248
866
950
626
104
58
512
24
892
894
742
958
>>> c=[]
>>> numbers.index(237)
21
>>> c = numbers[:21]
>>> c
[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918]
>>> for i in c:
	if i%2 == 0:
		print(i)

		
386
462
418
344
236
566
978
328
162
758
918
>>> '''Tried to solve question 6 without using break command'''
'Tried to solve question 6 without using break command'
>>> #asfas#
>>> #########Ques7#####
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list = set()
>>> color_list_1.union(color_list_2)
{'Red', 'Black', 'White', 'Green'}
>>> color_list_1.union(color_list_2) - color_list_2
{'Black', 'White'}
>>> color_list_1 - color_list_2
{'Black', 'White'}
>>> a = input('Enter string');
Enter string
>>> 