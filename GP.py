[A,a,B,b,C,c,D,d,E,e,F,f]=[5,5,4,4,3,3,2,2,1,1,0,0] 

while True: 

	try: 

		x = eval(input('Enter the number of course(s) you offered: '))
		if x==0:
			print("You can do better, how come you did no course?\n")
			print("If that was an error, try to enter the actual number this time\n")
			x = eval(input('Enter the number of course(s) you offered: '))
		if x==1:
			print("Your GP is equal to the value of your grade in the course\n")
			print("A,B,C,D,E and F equals to ",A,B,C,D,E,"and",F,"respectively\n")
			last=input("Do you want to calculate another GP? ")
			if last =="Yes":
				print("Ok, continue")
			elif last=="":
				print("Space cannot be empty\n")
				last=input("Do you want to calculate another GP? ")
				x = eval(input('Enter the number of course(s) you offered: '))
				if x==0:
					print("You can do better, how come you did no course?\n")
					print("If that was an error, try to enter the actual number this time\n")
					x = eval(input('Enter the number of courses you offered: '))
			else:
				break
		
		m= eval(input("Enter the unit of the first course: "))
		n=eval(input("Enter your grade in the first course: "))
		y=0 
		z=0
		for i in range(x-2): 
			u = eval(input('Enter the unit of the next course: ')) 
			v = eval(input('Enter the grade you have in the course: ')) 
			print('Your point in this course is: ', u*v)
			y = y+u*v
			z= z+u
		q=eval(input("Enter the unit of the last course: "))
		r=eval(input("Enter the grade you have in the last course: "))
		#Calculate the GP
		
		k=y+m*n+q*r
		l=z+m+q
		gp= k/l
		print('Your GP is: ', gp)
		if gp== 5.0:
			print('{:^55}'.format('SCHOLAR🙌🙌🙌, you have done well!!!'))
		elif 4.5<=gp<5.0:
				print('{:^55}'.format('FIRST CLASS, keep it up!!!'))
		elif 3.5<=gp<4.5:
				print('{:^55}'.format('SECOND CLASS UPPER, Nice one!!! '))
		elif 2.5<=gp<3.5:
				print('SECOND CLASS LOWER, put more effort'.center(55))
		else:
				print('{:^55}'.format('Try HARDER next semester')) 

	except NameError: 

		print('You entered the wrong shit') 

	except SyntaxError: 

		print('You entered the wrong shit') 

	except ValueError: 

		print('You entered the wrong shit') 

	except TypeError: 

		print('You entered the wrong shit')
	last=input("Do you want to calculate another GP? ")
	if last =="Yes":
		print("Ok, continue")
	elif last=="":
		print("Space cannot be empty")
		last=input("Do you want to calculate another GP? ")
		pass
	else:
		break
