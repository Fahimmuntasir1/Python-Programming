n = int(input('Enter number even or odd : '))
if n%2 ==0:
	if n in range(2,6):
		print('Not Weird')
	elif n in range(6, 21):
		print('Weird')
	elif n>20:
		print('Weird')
else:
	print('Weird')